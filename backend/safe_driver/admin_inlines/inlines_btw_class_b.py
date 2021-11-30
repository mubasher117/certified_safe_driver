from django.contrib import admin

from ..models.btw_class_b import *


class BTWCabSafetyClassBInline(admin.TabularInline):
    model = BTWCabSafetyClassB


class BTWStartEngineClassBInline(admin.TabularInline):
    model = BTWStartEngineClassB


class BTWEngineOperationClassBInline(admin.TabularInline):
    model = BTWEngineOperationClassB


class BTWClutchAndTransmissionClassBInline(admin.TabularInline):
    model = BTWClutchAndTransmissionClassB


class BTWBrakesAndStoppingsClassBInline(admin.TabularInline):
    model = BTWBrakesAndStoppingsClassB


class BTWEyeMovementAndMirrorClassBInline(admin.TabularInline):
    model = BTWEyeMovementAndMirrorClassB


class BTWRecognizesHazardsClassBInline(admin.TabularInline):
    model = BTWRecognizesHazardsClassB


class BTWLightsAndSignalsClassBInline(admin.TabularInline):
    model = BTWLightsAndSignalsClassB


class BTWSteeringClassBInline(admin.TabularInline):
    model = BTWSteeringClassB


class BTWBackingClassBInline(admin.TabularInline):
    model = BTWBackingClassB


class BTWSpeedClassBInline(admin.TabularInline):
    model = BTWSpeedClassB


class BTWIntersectionsClassBInline(admin.TabularInline):
    model = BTWIntersectionsClassB


class BTWTurningClassBInline(admin.TabularInline):
    model = BTWTurningClassB


class BTWParkingClassBInline(admin.TabularInline):
    model = BTWParkingClassB


class BTWHillsClassBInline(admin.TabularInline):
    model = BTWHillsClassB


class BTWPassingClassBInline(admin.TabularInline):
    model = BTWPassingClassB


class BTWGeneralSafetyAndDOTAdherenceClassBInline(admin.TabularInline):
    model = BTWGeneralSafetyAndDOTAdherenceClassB


btw_inlines = [BTWCabSafetyClassBInline, BTWEngineOperationClassBInline, BTWClutchAndTransmissionClassBInline,
               BTWBrakesAndStoppingsClassBInline,
               BTWEyeMovementAndMirrorClassBInline, BTWRecognizesHazardsClassBInline,
               BTWSteeringClassBInline, BTWBackingClassBInline, BTWSpeedClassBInline,
               BTWIntersectionsClassBInline, BTWTurningClassBInline, BTWParkingClassBInline,
               BTWHillsClassBInline, BTWHillsClassBInline, BTWPassingClassBInline,
               BTWGeneralSafetyAndDOTAdherenceClassBInline
               ]
