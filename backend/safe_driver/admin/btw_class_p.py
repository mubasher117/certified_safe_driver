from ..admin_inlines.inlines_btw_class_p import *
# from ..models.btw_class_p import *

btw_inlines = [BTWCabSafetyClassPInline, BTWStartEngineClassPInline, BTWEngineOperationClassPInline,
               BTWPassengerSafetyClassPInline, BTWBrakesAndStoppingsClassPInline, BTWEyeMovementAndMirrorClassPInline,
               BTWRecognizesHazardsClassPInline, BTWSteeringClassPInline, BTWBackingClassPInline, BTWSpeedClassPInline,
               BTWLightsAndSignalsClassPInline, BTWIntersectionsClassPInline, BTWTurningClassPInline,
               BTWParkingClassPInline, BTWHillsClassPInline, BTWPassingClassPInline, BTWRailroadCrossingClassPInline,
               BTWGeneralSafetyAndDOTAdherenceClassPInline, BTWInternalEnvironmentClassPInline
               ]


@admin.register(BTWClassP)
class BTWClassPAdmin(admin.ModelAdmin):
    list_display = ['test', 'test_student', 'date', 'start_time', 'end_time', 'company_rep_name', 'created']
    inlines = btw_inlines

    autocomplete_fields = ('test',)
    search_fields = ['test', 'date', 'start_time', 'end_time', 'company_rep_name', ]
    list_select_related = ['test', 'test__student']

    def test_student(self, instance):
        return '%s' % instance.test.student.full_name

    test_student.short_description = 'Student'
