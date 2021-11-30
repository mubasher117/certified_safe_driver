from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models.pretrips_bus import *


@receiver(post_save, sender=PreTripBus)
def create_pretrip_bus_objects(sender, instance, created, **kwargs):
    if instance:
        try:
            PreTripInsideCabBus.objects.create(pre_trip_bus=instance)
        except:
            pass
        try:
            PreTripCOALSBus.objects.create(pre_trip_bus=instance)
        except:
            pass

        try:
            PreTripEngineCompartmentBus.objects.create(pre_trip_bus=instance)
        except:
            pass

        try:
            PreTripVehicleFrontBus.objects.create(pre_trip_bus=instance)
        except:
            pass

        try:
            PreTripBothSidesVehiclesBus.objects.create(pre_trip_bus=instance)
        except:
            pass

        try:
            PreTripHandyCapBus.objects.create(pre_trip_bus=instance)
        except:
            pass

        try:
            PreTripRearOfVehicleBus.objects.create(pre_trip_bus=instance)
        except:
            pass

        try:
            PreTripPostTripBus.objects.create(pre_trip_bus=instance)
        except:
            pass

        try:
            instance.pretrip_cargo_area_bus
        except PreTripCargoAreaBus.DoesNotExist:
            PreTripCargoAreaBus.objects.create(pre_trip_bus=instance)

        try:
            instance.pretrip_ramp_bus
        except PreTripRampBus.DoesNotExist:
            PreTripRampBus.objects.create(pre_trip_bus=instance)

        try:
            instance.pretrip_interior_operation_bus
        except PreTripInteriorOperationBus.DoesNotExist:
            PreTripInteriorOperationBus.objects.create(pre_trip_bus=instance)
