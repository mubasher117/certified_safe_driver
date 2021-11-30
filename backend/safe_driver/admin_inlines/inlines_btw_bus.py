from django.contrib import admin

from ..models.btw_bus import *


class BTWCabSafetyBusInline(admin.TabularInline):
    model = BTWCabSafetyBus


class BTWStartEngineBusInline(admin.TabularInline):
    model = BTWStartEngineBus


class BTWEngineOperationBusInline(admin.TabularInline):
    model = BTWEngineOperationBus


class BTWPassengerSafetyBusInline(admin.TabularInline):
    model = BTWPassengerSafetyBus


class BTWBrakesAndStoppingsBusInline(admin.TabularInline):
    model = BTWBrakesAndStoppingsBus


class BTWEyeMovementAndMirrorBusInline(admin.TabularInline):
    model = BTWEyeMovementAndMirrorBus


class BTWRecognizesHazardsBusInline(admin.TabularInline):
    model = BTWRecognizesHazardsBus


class BTWLightsAndSignalsBusInline(admin.TabularInline):
    model = BTWLightsAndSignalsBus


class BTWSteeringBusInline(admin.TabularInline):
    model = BTWSteeringBus


class BTWBackingBusInline(admin.TabularInline):
    model = BTWBackingBus


class BTWSpeedBusInline(admin.TabularInline):
    model = BTWSpeedBus


# 12
class BTWIntersectionsBusInline(admin.TabularInline):
    model = BTWIntersectionsBus


# 13
class BTWTurningBusInline(admin.TabularInline):
    model = BTWTurningBus


# 15
class BTWParkingBusInline(admin.TabularInline):
    model = BTWParkingBus


# 15
class BTWHillsBusInline(admin.TabularInline):
    model = BTWHillsBus


# 16
class BTWPassingBusInline(admin.TabularInline):
    model = BTWPassingBus


# 17
class BTWRailroadCrossingBusInline(admin.TabularInline):
    model = BTWRailroadCrossingBus


# 18
class BTWGeneralSafetyAndDOTAdherenceBusInline(admin.TabularInline):
    model = BTWGeneralSafetyAndDOTAdherenceBus


# 19
class BTWInternalEnvironmentBusInline(admin.TabularInline):
    model = BTWInternalEnvironmentBus
