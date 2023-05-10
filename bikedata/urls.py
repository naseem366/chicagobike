from django.urls import path
from .views import *

urlpatterns = [
    path('sivyasikestatus',DivyaBikeStatus.as_view()),
]