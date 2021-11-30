from django.urls import path, include
from .views import *

app_name = 'truck_driving_school'
urlpatterns = [
    path('training-records/', DriverTrainigRecordList.as_view()),
]
