from django.contrib import admin

# Register your models here.
from safe_driver.models import *

# VTR Models Inline
vrt_inilines = []


class VRTPreTripInline(admin.TabularInline):
    model = VRTPreTrip


vrt_inilines += [VRTPreTripInline]


class VRTCouplingInline(admin.TabularInline):
    model = VRTCoupling


vrt_inilines += [VRTCouplingInline]


class VRTUncouplingInline(admin.TabularInline):
    model = VRTUncoupling


vrt_inilines += [VRTUncouplingInline]


class VRTEngineOperationsInline(admin.TabularInline):
    model = VRTEngineOperations


vrt_inilines += [VRTEngineOperationsInline]


class VRTStartEngineInline(admin.TabularInline):
    model = VRTStartEngine


vrt_inilines += [VRTStartEngineInline]


class VRTUseClutchInline(admin.TabularInline):
    model = VRTUseClutch


vrt_inilines += [VRTUseClutchInline]


class VRTUseOfTransmissionInline(admin.TabularInline):
    model = VRTUseOfTransmission


vrt_inilines += [VRTUseOfTransmissionInline]


class VRTUseOfBrakesInline(admin.TabularInline):
    model = VRTUseOfBrakes


vrt_inilines += [VRTUseOfBrakesInline]


class VRTBackingInline(admin.TabularInline):
    model = VRTBacking


vrt_inilines += [VRTBackingInline]


class VRTParkingInline(admin.TabularInline):
    model = VRTParking


vrt_inilines += [VRTParkingInline]


class VRTDrivingHabitsInline(admin.TabularInline):
    model = VRTDrivingHabits


vrt_inilines += [VRTDrivingHabitsInline]


class VRTPostTripInline(admin.TabularInline):
    model = VRTPostTrip


vrt_inilines += [VRTPostTripInline]
