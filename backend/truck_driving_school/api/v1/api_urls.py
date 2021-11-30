from django.urls import path
from .views import *

app_name = 'truck_driving_school'
urlpatterns = [
    path('dqf-requirements-items/', DQFRequirementListView.as_view()),
    path('trainee-book-items/', TraineeBookItemListView.as_view()),
]
