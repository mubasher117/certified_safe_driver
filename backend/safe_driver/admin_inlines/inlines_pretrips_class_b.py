from django.contrib import admin
from ..models.pretrips_class_b import *


class PreTripInsideCabClassBInline(admin.TabularInline):
    model = PreTripInsideCabClassB


class PreTripCOALSClassBInline(admin.TabularInline):
    model = PreTripCOALSClassB


class PreTripEngineCompartmentClassBInline(admin.TabularInline):
    model = PreTripEngineCompartmentClassB


class PreTripVehicleFrontClassBInline(admin.TabularInline):
    model = PreTripVehicleFrontClassB


class PreTripBothSidesVehiclesClassBInline(admin.TabularInline):
    model = PreTripBothSidesVehiclesClassB


class PreTripVehicleOrTractorRearClassBInline(admin.TabularInline):
    model = PreTripVehicleOrTractorRearClassB


class PreTripBoxHeaderBoardClassBInline(admin.TabularInline):
    model = PreTripBoxHeaderBoardClassB


class PreTripDriverSideBoxClassBInline(admin.TabularInline):
    model = PreTripDriverSideBoxClassB


class PreTripCargoAreaClassBInline(admin.TabularInline):
    model = PreTripCargoAreaClassB


class PreTripPassengerSideBoxClassBInline(admin.TabularInline):
    model = PreTripPassengerSideBoxClassB


class PreTripPostTripClassBInline(admin.TabularInline):
    model = PreTripPostTripClassB
