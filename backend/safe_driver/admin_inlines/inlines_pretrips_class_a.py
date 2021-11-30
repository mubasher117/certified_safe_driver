from django.contrib import admin
from ..models.pretrips_class_a import *


class PreTripInsideCabClassAInline(admin.TabularInline):
    model = PreTripInsideCabClassA


class PreTripCOALSClassAInline(admin.TabularInline):
    model = PreTripCOALSClassA


class PreTripEngineCompartmentClassAInline(admin.TabularInline):
    model = PreTripEngineCompartmentClassA


class PreTripVehicleFrontClassAInline(admin.TabularInline):
    model = PreTripVehicleFrontClassA


class PreTripBothSidesVehiclesClassAInline(admin.TabularInline):
    model = PreTripBothSidesVehiclesClassA


class PreTripVehicleOrTractorRearClassAInline(admin.TabularInline):
    model = PreTripVehicleOrTractorRearClassA


class PreTripFrontTrailerBoxClassAInline(admin.TabularInline):
    model = PreTripFrontTrailerBoxClassA


class PreTripDriverSideTrailerBoxClassAInline(admin.TabularInline):
    model = PreTripDriverSideTrailerBoxClassA


class PreTripRearTrailerBoxClassAInline(admin.TabularInline):
    model = PreTripRearTrailerBoxClassA


class PreTripPassengerSideTrailerBoxClassAInline(admin.TabularInline):
    model = PreTripPassengerSideTrailerBoxClassA


class PreTripDollyClassAInline(admin.TabularInline):
    model = PreTripDollyClassA


class PreTripPostTripClassAInline(admin.TabularInline):
    model = PreTripPostTripClassA
