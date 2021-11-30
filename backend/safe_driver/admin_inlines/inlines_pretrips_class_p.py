from django.contrib import admin
from ..models.pretrips_class_p import *


class PreTripInsideCabClassPInline(admin.TabularInline):
    model = PreTripInsideCabClassP


class PreTripCOALSClassPInline(admin.TabularInline):
    model = PreTripCOALSClassP


class PreTripEngineCompartmentClassPInline(admin.TabularInline):
    model = PreTripEngineCompartmentClassP


class PreTripVehicleFrontClassPInline(admin.TabularInline):
    model = PreTripVehicleFrontClassP


class PreTripBothSidesVehiclesClassPInline(admin.TabularInline):
    model = PreTripBothSidesVehiclesClassP


class PreTripRearOfVehicleClassPInline(admin.TabularInline):
    model = PreTripRearOfVehicleClassP


class PreTripCargoAreaClassPInline(admin.TabularInline):
    model = PreTripCargoAreaClassP


class PreTripRampClassPInline(admin.TabularInline):
    model = PreTripRampClassP


class PreTripInteriorOperationClassPInline(admin.TabularInline):
    model = PreTripInteriorOperationClassP


class PreTripHandyCapClassPInline(admin.TabularInline):
    model = PreTripHandyCapClassP


class PreTripPostTripClassPInline(admin.TabularInline):
    model = PreTripPostTripClassP
