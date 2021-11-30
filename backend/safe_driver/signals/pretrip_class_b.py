from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models.pretrips_class_b import *


@receiver(post_save, sender=PreTripClassB)
def create_pretrip_class_b_objects(sender, instance, created, **kwargs):
    if instance:
        try:
            instance.pretrip_insidecab_class_b
        except PreTripInsideCabClassB.DoesNotExist:
            PreTripInsideCabClassB.objects.create(pre_trip_class_b=instance)
        try:
            instance.pretrip_coals_class_b
        except PreTripCOALSClassB.DoesNotExist:
            PreTripCOALSClassB.objects.create(pre_trip_class_b=instance)

        try:
            instance.pretrip_engine_compartment_class_b
        except PreTripEngineCompartmentClassB.DoesNotExist:
            PreTripEngineCompartmentClassB.objects.create(pre_trip_class_b=instance)

        try:
            instance.pretrip_vehicle_front_class_b
        except PreTripVehicleFrontClassB.DoesNotExist:
            PreTripVehicleFrontClassB.objects.create(pre_trip_class_b=instance)

        try:
            instance.pretrip_both_sides_vehicle_class_b
        except PreTripBothSidesVehiclesClassB.DoesNotExist:
            PreTripBothSidesVehiclesClassB.objects.create(pre_trip_class_b=instance)

        try:
            instance.pretrip_vehicle_or_tractor_rear_class_b
        except PreTripVehicleOrTractorRearClassB.DoesNotExist:
            PreTripVehicleOrTractorRearClassB.objects.create(pre_trip_class_b=instance)

        try:
            instance.pretrip_cargo_area_class_b
        except PreTripCargoAreaClassB.DoesNotExist:
            PreTripCargoAreaClassB.objects.create(pre_trip_class_b=instance)

        try:
            instance.pretrip_driver_side_box_class_b
        except PreTripDriverSideBoxClassB.DoesNotExist:
            PreTripDriverSideBoxClassB.objects.create(pre_trip_class_b=instance)

        try:
            instance.pretrip_box_header_board_class_b
        except PreTripBoxHeaderBoardClassB.DoesNotExist:
            PreTripBoxHeaderBoardClassB.objects.create(pre_trip_class_b=instance)

        try:
            instance.pretrip_passenger_side_box_class_b
        except PreTripPassengerSideBoxClassB.DoesNotExist:
            PreTripPassengerSideBoxClassB.objects.create(pre_trip_class_b=instance)

        try:
            instance.pretrip_posttrip_class_b
        except PreTripPostTripClassB.DoesNotExist:
            PreTripPostTripClassB.objects.create(pre_trip_class_b=instance)
