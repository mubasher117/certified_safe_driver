from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models.pretrips_class_p import *


@receiver(post_save, sender=PreTripClassP)
def create_pretrip_class_p_objects(sender, instance, created, **kwargs):
    if instance:
        try:
            instance.pretrip_insidecab_class_p
        except PreTripInsideCabClassP.DoesNotExist:
            PreTripInsideCabClassP.objects.create(pre_trip_class_p=instance)
        try:
            instance.pretrip_coals_class_p
        except PreTripCOALSClassP.DoesNotExist:
            PreTripCOALSClassP.objects.create(pre_trip_class_p=instance)

        try:
            instance.pretrip_engine_compartment_class_p
        except PreTripEngineCompartmentClassP.DoesNotExist:
            PreTripEngineCompartmentClassP.objects.create(pre_trip_class_p=instance)

        try:
            instance.pretrip_vehicle_front_class_p
        except PreTripVehicleFrontClassP.DoesNotExist:
            PreTripVehicleFrontClassP.objects.create(pre_trip_class_p=instance)

        try:
            instance.pretrip_both_sides_vehicle_class_p
        except PreTripBothSidesVehiclesClassP.DoesNotExist:
            PreTripBothSidesVehiclesClassP.objects.create(pre_trip_class_p=instance)

        try:
            instance.pretrip_handycap_class_p
        except PreTripHandyCapClassP.DoesNotExist:
            PreTripHandyCapClassP.objects.create(pre_trip_class_p=instance)

        try:
            instance.pretrip_rear_of_vehicle_class_p
        except PreTripRearOfVehicleClassP.DoesNotExist:
            PreTripRearOfVehicleClassP.objects.create(pre_trip_class_p=instance)

        try:
            instance.pretrip_posttrip_class_p
        except PreTripPostTripClassP.DoesNotExist:
            PreTripPostTripClassP.objects.create(pre_trip_class_p=instance)

        try:
            instance.pretrip_cargo_area_class_p
        except PreTripCargoAreaClassP.DoesNotExist:
            PreTripCargoAreaClassP.objects.create(pre_trip_class_p=instance)

        try:
            instance.pretrip_ramp_class_p
        except PreTripRampClassP.DoesNotExist:
            PreTripRampClassP.objects.create(pre_trip_class_p=instance)

        try:
            instance.pretrip_interior_operation_class_p
        except PreTripInteriorOperationClassP.DoesNotExist:
            PreTripInteriorOperationClassP.objects.create(pre_trip_class_p=instance)
