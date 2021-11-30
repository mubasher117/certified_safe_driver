from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from ..admin_inlines.inlines_pretrips_bus import *
from ..models.pretrips_bus import *

pre_trips_inline = [PreTripInsideCabBusInline, PreTripCOALSBusInline, PreTripEngineCompartmentBusInline,
                    PreTripVehicleFrontBusInline, PreTripBothSidesVehiclesBusInline,
                    PreTripHandyCapBusInline, PreTripRearOfVehicleBusInline, PreTripPostTripBusInline,
                    PreTripCargoAreaBusInline, PreTripRampBusInline, PreTripInteriorOperationBusInline]


@admin.register(PreTripBus)
class PreTripAdminBus(admin.ModelAdmin):
    list_display = ['test', 'test_student', 'date', 'start_time', 'end_time', 'company_rep_name', 'created']
    inlines = pre_trips_inline

    autocomplete_fields = ('test',)
    search_fields = ['test', 'date', 'start_time', 'end_time', 'company_rep_name', ]
    list_select_related = ['test', 'test__student']

    def test_student(self, instance):
        return '%s' % instance.test.student.full_name

    test_student.short_description = 'Student'
