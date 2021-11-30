from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models.pretrips_class_c import *


@receiver(post_save, sender=PreTripClassC)
def create_pretrip_class_c_objects(sender, instance, created, **kwargs):
    if instance:
        try:
            instance.pretrip_insidecab_class_c
        except PreTripInsideCabClassC.DoesNotExist:
            PreTripInsideCabClassC.objects.create(pre_trip_class_c=instance)

        try:
            instance.pretrip_engine_compartment_class_c
        except PreTripEngineCompartmentClassC.DoesNotExist:
            PreTripEngineCompartmentClassC.objects.create(pre_trip_class_c=instance)

        try:
            instance.pretrip_vehicle_front_class_c
        except PreTripVehicleFrontClassC.DoesNotExist:
            PreTripVehicleFrontClassC.objects.create(pre_trip_class_c=instance)

        try:
            instance.pretrip_both_sides_vehicle_class_c
        except PreTripBothSidesVehiclesClassC.DoesNotExist:
            PreTripBothSidesVehiclesClassC.objects.create(pre_trip_class_c=instance)

        try:
            instance.pretrip_vehicle_rear_class_c
        except PreTripVehicleRearClassC.DoesNotExist:
            PreTripVehicleRearClassC.objects.create(pre_trip_class_c=instance)

        try:
            instance.pretrip_cargo_area_class_c
        except PreTripCargoAreaClassC.DoesNotExist:
            PreTripCargoAreaClassC.objects.create(pre_trip_class_c=instance)

        try:
            instance.pretrip_posttrip_class_c
        except PreTripPostTripClassC.DoesNotExist:
            PreTripPostTripClassC.objects.create(pre_trip_class_c=instance)
