from django.urls import path

from .chart_views import *

urlpatterns = [
    path('students-by-month/', ChartNumberOfStudentsByMonths.as_view()),
]
