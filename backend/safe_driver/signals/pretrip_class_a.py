from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models.pretrips_class_a import *


@receiver(post_save, sender=PreTripClassA)
def create_pretrip_class_a_objects(sender, instance, created, **kwargs):
    if instance:
        try:
            instance.pretrip_insidecab_class_a
        except PreTripInsideCabClassA.DoesNotExist:
            PreTripInsideCabClassA.objects.create(pre_trip_class_a=instance)

        try:
            instance.pretrip_coals_class_a
        except PreTripCOALSClassA.DoesNotExist:
            PreTripCOALSClassA.objects.create(pre_trip_class_a=instance)

        try:
            instance.pretrip_engine_compartment_class_a
        except PreTripEngineCompartmentClassA.DoesNotExist:
            PreTripEngineCompartmentClassA.objects.create(pre_trip_class_a=instance)

        try:
            instance.pretrip_vehicle_front_class_a
        except PreTripVehicleFrontClassA.DoesNotExist:
            PreTripVehicleFrontClassA.objects.create(pre_trip_class_a=instance)

        try:
            instance.pretrip_both_sides_vehicle_class_a
        except PreTripBothSidesVehiclesClassA.DoesNotExist:
            PreTripBothSidesVehiclesClassA.objects.create(pre_trip_class_a=instance)

        try:
            instance.pretrip_vehicle_or_tractor_rear_class_a
        except PreTripVehicleOrTractorRearClassA.DoesNotExist:
            PreTripVehicleOrTractorRearClassA.objects.create(pre_trip_class_a=instance)

        try:
            instance.pretrip_front_trailer_box_class_a
        except PreTripFrontTrailerBoxClassA.DoesNotExist:
            PreTripFrontTrailerBoxClassA.objects.create(pre_trip_class_a=instance)

        try:
            instance.pretrip_driver_side_trailer_box_class_a
        except PreTripDriverSideTrailerBoxClassA.DoesNotExist:
            PreTripDriverSideTrailerBoxClassA.objects.create(pre_trip_class_a=instance)

        try:
            instance.pretrip_rear_trailer_box_class_a
        except PreTripRearTrailerBoxClassA.DoesNotExist:
            PreTripRearTrailerBoxClassA.objects.create(pre_trip_class_a=instance)

        try:
            instance.pretrip_passenger_side_trailer_box_class_a
        except PreTripPassengerSideTrailerBoxClassA.DoesNotExist:
            PreTripPassengerSideTrailerBoxClassA.objects.create(pre_trip_class_a=instance)

        try:
            instance.pretrip_dolly_class_a
        except PreTripDollyClassA.DoesNotExist:
            PreTripDollyClassA.objects.create(pre_trip_class_a=instance)

        try:
            instance.pretrip_posttrip_class_a
        except PreTripPostTripClassA.DoesNotExist:
            PreTripPostTripClassA.objects.create(pre_trip_class_a=instance)
