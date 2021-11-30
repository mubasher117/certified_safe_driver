from django.contrib import admin
from safe_driver.models import (
    PASBacking, PASBrakesAndStoppings, PASCabSafety, PASEngineOperation, PASEyeMovementAndMirror,
    PASGeneralSafetyAndDOTAdherence, PASHills, PASIntersections, PASLightsAndSignals, PASParking, PASPassengerSafety,
    PASPassing, PASRailroadCrossing, PASRecognizesHazards, PASSpeed, PASStartEngine, PASSteering, PASTurning,
)

pas_inlines = []


class PASBackingInline(admin.TabularInline):
    model = PASBacking


pas_inlines += [PASBackingInline]


class PASBrakesAndStoppingsInline(admin.TabularInline):
    model = PASBrakesAndStoppings


pas_inlines += [PASBrakesAndStoppingsInline]


class PASCabSafetyInline(admin.TabularInline):
    model = PASCabSafety


pas_inlines += [PASCabSafetyInline]


class PASEyeMovementAndMirrorInline(admin.TabularInline):
    model = PASEyeMovementAndMirror


pas_inlines += [PASEyeMovementAndMirrorInline]


class PASEngineOperationInline(admin.TabularInline):
    model = PASEngineOperation


pas_inlines += [PASEngineOperationInline]


class PASGeneralSafetyAndDOTAdherenceInline(admin.TabularInline):
    model = PASGeneralSafetyAndDOTAdherence


pas_inlines += [PASGeneralSafetyAndDOTAdherenceInline]


class PASHillsInline(admin.TabularInline):
    model = PASHills


pas_inlines += [PASHillsInline]


class PASIntersectionsInline(admin.TabularInline):
    model = PASIntersections


pas_inlines += [PASIntersectionsInline]


class PASLightsAndSignalsInline(admin.TabularInline):
    model = PASLightsAndSignals


pas_inlines += [PASLightsAndSignalsInline]


class PASParkingInline(admin.TabularInline):
    model = PASParking


pas_inlines += [PASParkingInline]


class PASPassengerSafetyInline(admin.TabularInline):
    model = PASPassengerSafety


pas_inlines += [PASPassengerSafetyInline]


class PASPassingInline(admin.TabularInline):
    model = PASPassing


pas_inlines += [PASPassingInline]


class PASRailroadCrossingInline(admin.TabularInline):
    model = PASRailroadCrossing


pas_inlines += [PASRailroadCrossingInline]


class PASRecognizesHazardsInline(admin.TabularInline):
    model = PASRecognizesHazards


pas_inlines += [PASRecognizesHazardsInline]


class PASTurningInline(admin.TabularInline):
    model = PASTurning


pas_inlines += [PASTurningInline]


class PASSteeringInline(admin.TabularInline):
    model = PASSteering


pas_inlines += [PASSteeringInline]


class PASStartEngineInline(admin.TabularInline):
    model = PASStartEngine


pas_inlines += [PASStartEngineInline]


class PASSpeedInline(admin.TabularInline):
    model = PASSpeed


pas_inlines += [PASSpeedInline]
