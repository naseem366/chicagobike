# chicagobike

Divvy Bikes(https://divvybikes.com/) is a bike sharing facility provided by the city of Chicago for its residents. As
this is a popular service, the city provides bike sharing data open to developers for
continuous innovation, system planning etc. They generally share the data adhering to
the specification listed here(https://gbfs.mobilitydata.org/).

Among other things, the following are two JSON feeds that are quite useful.

station_status (info about the bike docking stations)
- https://gbfs.divvybikes.com/gbfs/en/station_status.json
free_bike_status (info about each individual bik)
- https://gbfs.divvybikes.com/gbfs/en/free_bike_status.json

Assignment:

Please build a REST API wrapper on the top of both of these API which when pinged
gives the following info as a json response

1. Total Docks Avl (use station url)
2. Total Bikes Avl (use station url)
3. Total Station Active (use station url)
4. Total Bikes that is reserved (use free bike url)
