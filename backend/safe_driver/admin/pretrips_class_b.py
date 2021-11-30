from ..admin_inlines.inlines_pretrips_class_b import *
from ..models.pretrips_class_b import *

pre_trips_inline = [PreTripInsideCabClassBInline, PreTripCOALSClassBInline, PreTripEngineCompartmentClassBInline,
                    PreTripVehicleFrontClassBInline, PreTripBothSidesVehiclesClassBInline,
                    PreTripVehicleOrTractorRearClassBInline, PreTripCargoAreaClassBInline,
                    PreTripBoxHeaderBoardClassBInline, PreTripDriverSideBoxClassBInline,
                    PreTripPassengerSideBoxClassBInline, PreTripPostTripClassBInline]


@admin.register(PreTripClassB)
class PreTripAdminClassB(admin.ModelAdmin):
    list_display = ['test', 'test_student', 'date', 'start_time', 'end_time', 'company_rep_name', 'created']
    inlines = pre_trips_inline

    autocomplete_fields = ('test',)
    search_fields = ['test', 'date', 'start_time', 'end_time', 'company_rep_name', ]
    list_select_related = ['test', 'test__student']

    def test_student(self, instance):
        return '%s' % instance.test.student.full_name

    test_student.short_description = 'Student'
