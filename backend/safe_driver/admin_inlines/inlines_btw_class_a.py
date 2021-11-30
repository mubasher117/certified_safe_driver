from django.contrib import admin

from ..models.btw_class_a import *


class BTWCabSafetyClassAInline(admin.TabularInline):
    model = BTWCabSafetyClassA


class BTWStartEngineClassAInline(admin.TabularInline):
    model = BTWStartEngineClassA


class BTWEngineOperationClassAInline(admin.TabularInline):
    model = BTWEngineOperationClassA


class BTWClutchAndTransmissionClassAInline(admin.TabularInline):
    model = BTWClutchAndTransmissionClassA


class BTWCouplingClassAInline(admin.TabularInline):
    model = BTWCouplingClassA


class BTWUncouplingClassAInline(admin.TabularInline):
    model = BTWUncouplingClassA


class BTWBrakesAndStoppingsClassAInline(admin.TabularInline):
    model = BTWBrakesAndStoppingsClassA


class BTWEyeMovementAndMirrorClassAInline(admin.TabularInline):
    model = BTWEyeMovementAndMirrorClassA


class BTWRecognizesHazardsClassAInline(admin.TabularInline):
    model = BTWRecognizesHazardsClassA


class BTWLightsAndSignalsClassAInline(admin.TabularInline):
    model = BTWLightsAndSignalsClassA


class BTWSteeringClassAInline(admin.TabularInline):
    model = BTWSteeringClassA


class BTWBackingClassAInline(admin.TabularInline):
    model = BTWBackingClassA


class BTWSpeedClassAInline(admin.TabularInline):
    model = BTWSpeedClassA


class BTWIntersectionsClassAInline(admin.TabularInline):
    model = BTWIntersectionsClassA


class BTWTurningClassAInline(admin.TabularInline):
    model = BTWTurningClassA


class BTWParkingClassAInline(admin.TabularInline):
    model = BTWParkingClassA


class BTWMultipleTrailersClassAInline(admin.TabularInline):
    model = BTWMultipleTrailersClassA


class BTWHillsClassAInline(admin.TabularInline):
    model = BTWHillsClassA


class BTWPassingClassAInline(admin.TabularInline):
    model = BTWPassingClassA


class BTWGeneralSafetyAndDOTAdherenceClassAInline(admin.TabularInline):
    model = BTWGeneralSafetyAndDOTAdherenceClassA


btw_inlines = [BTWCabSafetyClassAInline, BTWEngineOperationClassAInline, BTWClutchAndTransmissionClassAInline,
               BTWCouplingClassAInline, BTWUncouplingClassAInline, BTWBrakesAndStoppingsClassAInline,
               BTWEyeMovementAndMirrorClassAInline, BTWRecognizesHazardsClassAInline,
               BTWSteeringClassAInline, BTWBackingClassAInline, BTWSpeedClassAInline,
               BTWIntersectionsClassAInline, BTWTurningClassAInline, BTWParkingClassAInline,
               BTWMultipleTrailersClassAInline, BTWMultipleTrailersClassAInline,
               BTWHillsClassAInline, BTWHillsClassAInline, BTWPassingClassAInline,
               BTWGeneralSafetyAndDOTAdherenceClassAInline
               ]
