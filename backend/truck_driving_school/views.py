from django.shortcuts import render

from django.views.generic import ListView
from .models import *


class DriverTrainigRecordList(ListView):
    model = DriverTrainigRecord
    template_name = 'truck_driving_school/training_records.html'
    context_object_name = 'records'

    def get_queryset(self):
        return DriverTrainigRecord.objects.select_related('test', 'location')
