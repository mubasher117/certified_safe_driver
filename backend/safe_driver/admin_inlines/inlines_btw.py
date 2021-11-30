from django.contrib import admin

# Register your models here.
from safe_driver.models import *


btw_inlines = []


class BTWCabSafetyInline(admin.TabularInline):
    model = BTWCabSafety


btw_inlines += [BTWCabSafetyInline]


class BTWStartEngineInline(admin.TabularInline):
    model = BTWStartEngine


btw_inlines += [BTWStartEngineInline]


class BTWEngineOperationInline(admin.TabularInline):
    model = BTWEngineOperation


btw_inlines += [BTWEngineOperationInline]


class BTWClutchAndTransmissionInline(admin.TabularInline):
    model = BTWClutchAndTransmission


btw_inlines += [BTWClutchAndTransmissionInline]


class BTWCouplingInline(admin.TabularInline):
    model = BTWCoupling


btw_inlines += [BTWCouplingInline]


class BTWUncouplingInline(admin.TabularInline):
    model = BTWUncoupling


btw_inlines += [BTWUncouplingInline]


class BTWBrakesAndStoppingsInline(admin.TabularInline):
    model = BTWBrakesAndStoppings


btw_inlines += [BTWBrakesAndStoppingsInline]


class BTWEyeMovementAndMirrorInline(admin.TabularInline):
    model = BTWEyeMovementAndMirror


btw_inlines += [BTWEyeMovementAndMirrorInline]


class BTWRecognizesHazardsInline(admin.TabularInline):
    model = BTWRecognizesHazards


btw_inlines += [BTWRecognizesHazardsInline]


class BTWLightsAndSignalsInline(admin.TabularInline):
    model = BTWLightsAndSignals


btw_inlines += [BTWLightsAndSignalsInline]


class BTWSteeringInline(admin.TabularInline):
    model = BTWSteering


btw_inlines += [BTWSteeringInline]


class BTWBackingInline(admin.TabularInline):
    model = BTWBacking


btw_inlines += [BTWBackingInline]


class BTWSpeedInline(admin.TabularInline):
    model = BTWSpeed


btw_inlines += [BTWSpeedInline]


class BTWIntersectionsInline(admin.TabularInline):
    model = BTWIntersections


btw_inlines += [BTWIntersectionsInline]


class BTWTurningInline(admin.TabularInline):
    model = BTWTurning


btw_inlines += [BTWTurningInline]


class BTWParkingInline(admin.TabularInline):
    model = BTWParking


btw_inlines += [BTWParkingInline]


class BTWMultipleTrailersInline(admin.TabularInline):
    model = BTWMultipleTrailers


btw_inlines += [BTWMultipleTrailersInline]


class BTWHillsInline(admin.TabularInline):
    model = BTWHills


btw_inlines += [BTWHillsInline]


class BTWPassingInline(admin.TabularInline):
    model = BTWPassing


btw_inlines += [BTWPassingInline]


class BTWGeneralSafetyAndDOTAdherenceInline(admin.TabularInline):
    model = BTWGeneralSafetyAndDOTAdherence


btw_inlines += [BTWGeneralSafetyAndDOTAdherenceInline]
