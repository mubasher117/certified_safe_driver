from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from ..admin_inlines.inlines_pretrips_class_p import *
from ..models.pretrips_class_p import *

pre_trips_inline = [PreTripInsideCabClassPInline, PreTripCOALSClassPInline, PreTripEngineCompartmentClassPInline,
                    PreTripVehicleFrontClassPInline, PreTripBothSidesVehiclesClassPInline,
                    PreTripHandyCapClassPInline, PreTripRearOfVehicleClassPInline, PreTripPostTripClassPInline,
                    PreTripCargoAreaClassPInline, PreTripRampClassPInline, PreTripInteriorOperationClassPInline]


@admin.register(PreTripClassP)
class PreTripAdminClassP(admin.ModelAdmin):
    list_display = ['test', 'test_student', 'date', 'start_time', 'end_time', 'company_rep_name', 'created']
    inlines = pre_trips_inline

    autocomplete_fields = ('test',)
    search_fields = ['test', 'date', 'start_time', 'end_time', 'company_rep_name', ]
    list_select_related = ['test', 'test__student']

    def test_student(self, instance):
        return '%s' % instance.test.student.full_name

    test_student.short_description = 'Student'
