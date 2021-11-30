from django.contrib import admin
from ..models.pretrips_bus import *


class PreTripInsideCabBusInline(admin.TabularInline):
    model = PreTripInsideCabBus


class PreTripCOALSBusInline(admin.TabularInline):
    model = PreTripCOALSBus


class PreTripEngineCompartmentBusInline(admin.TabularInline):
    model = PreTripEngineCompartmentBus


class PreTripVehicleFrontBusInline(admin.TabularInline):
    model = PreTripVehicleFrontBus


class PreTripBothSidesVehiclesBusInline(admin.TabularInline):
    model = PreTripBothSidesVehiclesBus


class PreTripRearOfVehicleBusInline(admin.TabularInline):
    model = PreTripRearOfVehicleBus


class PreTripCargoAreaBusInline(admin.TabularInline):
    model = PreTripCargoAreaBus


class PreTripRampBusInline(admin.TabularInline):
    model = PreTripRampBus


class PreTripInteriorOperationBusInline(admin.TabularInline):
    model = PreTripInteriorOperationBus


class PreTripHandyCapBusInline(admin.TabularInline):
    model = PreTripHandyCapBus


class PreTripPostTripBusInline(admin.TabularInline):
    model = PreTripPostTripBus
