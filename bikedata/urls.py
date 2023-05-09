from django.urls import path
from .views import *

urlpatterns = [
    path('DivyaBikeStatus',DivyaBikeStatus.as_view()),
]