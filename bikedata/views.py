import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


# The station status Url
station_url = 'https://gbfs.divvybikes.com/gbfs/en/station_status.json'

# The free bike status Url
free_bike_url = 'https://gbfs.divvybikes.com/gbfs/en/free_bike_status.json'

class DivyaBikeStatus(APIView):
    def get(self,request):

        # Station status
        station_status = requests.get(station_url)
        station_status_data = station_status.json()
        
        # Bike status
        free_bike_status = requests.get(free_bike_url)
        free_bike_status_data = free_bike_status.json()

        total_docks_avl = 0
        total_bikes_avl = 0
        total_bikes_reserved = 0
        total_stations_active = 0

        for station in station_status_data['data']['stations']:
            total_docks_avl += station['num_docks_available']
            total_bikes_avl += station['num_bikes_available']
            if station['station_status'] == 'active':
                total_stations_active += 1

# Reserved_status counts

        for bike in free_bike_status_data['data']['bikes']:
            if bike['is_reserved']:
                total_bikes_reserved += 1


        divvy_status = {
            'total_docks_available': total_docks_avl,
            'total_bikes_available': total_bikes_avl,
            'total_stations_active': total_stations_active,
            'total_bikes_reserved': total_bikes_reserved
        }

        return Response({'message':'success','data':divvy_status},status=HTTP_200_OK)
