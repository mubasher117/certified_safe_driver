from django.contrib import admin
from ..models.pretrips_class_c import *


class PreTripInsideCabClassCInline(admin.TabularInline):
    model = PreTripInsideCabClassC


class PreTripEngineCompartmentClassCInline(admin.TabularInline):
    model = PreTripEngineCompartmentClassC


class PreTripVehicleFrontClassCInline(admin.TabularInline):
    model = PreTripVehicleFrontClassC


class PreTripBothSidesVehiclesClassCInline(admin.TabularInline):
    model = PreTripBothSidesVehiclesClassC


class PreTripVehicleRearClassCInline(admin.TabularInline):
    model = PreTripVehicleRearClassC


class PreTripCargoAreaClassCInline(admin.TabularInline):
    model = PreTripCargoAreaClassC


class PreTripPostTripClassCInline(admin.TabularInline):
    model = PreTripPostTripClassC
