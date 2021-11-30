from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from ..admin_inlines.inlines_pretrips_class_a import *
from ..models.pretrips_class_a import *

pre_trips_inline = [PreTripInsideCabClassAInline, PreTripCOALSClassAInline, PreTripEngineCompartmentClassAInline,
                    PreTripVehicleFrontClassAInline, PreTripBothSidesVehiclesClassAInline,
                    PreTripVehicleOrTractorRearClassAInline,
                    PreTripFrontTrailerBoxClassAInline, PreTripDriverSideTrailerBoxClassAInline,
                    PreTripRearTrailerBoxClassAInline,
                    PreTripPassengerSideTrailerBoxClassAInline, PreTripDollyClassAInline,
                    PreTripPostTripClassAInline]


@admin.register(PreTripClassA)
class PreTripAdminClassA(admin.ModelAdmin):
    list_display = ['test', 'test_student', 'date', 'start_time', 'end_time', 'company_rep_name', 'created']
    inlines = pre_trips_inline

    autocomplete_fields = ('test',)
    search_fields = ['test', 'date', 'start_time', 'end_time', 'company_rep_name', ]
    list_select_related = ['test', 'test__student']

    def test_student(self, instance):
        return '%s' % instance.test.student.full_name

    test_student.short_description = 'Student'
