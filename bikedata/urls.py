from django.urls import path
from .views import *

urlpatterns = [
    path('divyasikestatus',DivyaBikeStatus.as_view()),
]