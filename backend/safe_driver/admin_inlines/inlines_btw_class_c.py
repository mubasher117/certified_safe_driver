from django.contrib import admin

from ..models.btw_class_c import *


class BTWCabSafetyClassCInline(admin.TabularInline):
    model = BTWCabSafetyClassC


class BTWStartEngineClassCInline(admin.TabularInline):
    model = BTWStartEngineClassC


class BTWEngineOperationClassCInline(admin.TabularInline):
    model = BTWEngineOperationClassC


class BTWClutchAndTransmissionClassCInline(admin.TabularInline):
    model = BTWClutchAndTransmissionClassC


class BTWBrakesAndStoppingsClassCInline(admin.TabularInline):
    model = BTWBrakesAndStoppingsClassC


class BTWEyeMovementAndMirrorClassCInline(admin.TabularInline):
    model = BTWEyeMovementAndMirrorClassC


class BTWRecognizesHazardsClassCInline(admin.TabularInline):
    model = BTWRecognizesHazardsClassC


class BTWLightsAndSignalsClassCInline(admin.TabularInline):
    model = BTWLightsAndSignalsClassC


class BTWSteeringClassCInline(admin.TabularInline):
    model = BTWSteeringClassC


class BTWBackingClassCInline(admin.TabularInline):
    model = BTWBackingClassC


class BTWSpeedClassCInline(admin.TabularInline):
    model = BTWSpeedClassC


class BTWIntersectionsClassCInline(admin.TabularInline):
    model = BTWIntersectionsClassC


class BTWTurningClassCInline(admin.TabularInline):
    model = BTWTurningClassC


class BTWParkingClassCInline(admin.TabularInline):
    model = BTWParkingClassC


class BTWHillsClassCInline(admin.TabularInline):
    model = BTWHillsClassC


class BTWPassingClassCInline(admin.TabularInline):
    model = BTWPassingClassC


class BTWGeneralSafetyAndDOTAdherenceClassCInline(admin.TabularInline):
    model = BTWGeneralSafetyAndDOTAdherenceClassC


btw_inlines = [BTWCabSafetyClassCInline, BTWEngineOperationClassCInline, BTWClutchAndTransmissionClassCInline,
               BTWBrakesAndStoppingsClassCInline,
               BTWEyeMovementAndMirrorClassCInline, BTWRecognizesHazardsClassCInline,
               BTWSteeringClassCInline, BTWBackingClassCInline, BTWSpeedClassCInline,
               BTWIntersectionsClassCInline, BTWTurningClassCInline, BTWParkingClassCInline,
               BTWHillsClassCInline, BTWHillsClassCInline, BTWPassingClassCInline,
               BTWGeneralSafetyAndDOTAdherenceClassCInline
               ]
