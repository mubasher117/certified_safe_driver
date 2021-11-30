from ..admin_inlines.inlines_btw_bus import *
from ..models.btw_bus import *

btw_inlines = [BTWCabSafetyBusInline, BTWStartEngineBusInline, BTWEngineOperationBusInline, BTWPassengerSafetyBusInline,
               BTWBrakesAndStoppingsBusInline, BTWEyeMovementAndMirrorBusInline, BTWRecognizesHazardsBusInline,
               BTWSteeringBusInline, BTWBackingBusInline, BTWSpeedBusInline, BTWLightsAndSignalsBusInline,
               BTWIntersectionsBusInline, BTWTurningBusInline, BTWParkingBusInline, BTWHillsBusInline,
               BTWPassingBusInline, BTWRailroadCrossingBusInline, BTWGeneralSafetyAndDOTAdherenceBusInline,
               BTWInternalEnvironmentBusInline
               ]


@admin.register(BTWBus)
class BTWClassAAdmin(admin.ModelAdmin):
    list_display = ['test', 'test_student', 'date', 'start_time', 'end_time', 'company_rep_name', 'created']
    inlines = btw_inlines

    autocomplete_fields = ('test',)
    search_fields = ['test', 'date', 'start_time', 'end_time', 'company_rep_name', ]
    list_select_related = ['test', 'test__student']

    def test_student(self, instance):
        return '%s' % instance.test.student.full_name

    test_student.short_description = 'Student'
