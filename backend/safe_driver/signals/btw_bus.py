from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models.btw_bus import *


@receiver(post_save, sender=BTWBus)
def create_btw_bus_objects_instance(sender, instance, created, **kwargs):
    if instance:
        try:
            instance.btw_cab_safety_bus
        except BTWCabSafetyBus.DoesNotExist:
            BTWCabSafetyBus.objects.create(btw=instance)

        try:
            instance.btw_start_engine_bus
        except BTWStartEngineBus.DoesNotExist:
            BTWStartEngineBus.objects.create(btw=instance)

        try:
            instance.btw_engine_operation_bus
        except BTWEngineOperationBus.DoesNotExist:
            BTWEngineOperationBus.objects.create(btw=instance)

        try:
            instance.btw_passenger_safety_bus
        except BTWPassengerSafetyBus.DoesNotExist:
            BTWPassengerSafetyBus.objects.create(btw=instance)

        try:
            instance.btw_brakes_and_stopping_bus
        except BTWBrakesAndStoppingsBus.DoesNotExist:
            BTWBrakesAndStoppingsBus.objects.create(btw=instance)

        try:
            instance.btw_eye_movement_and_mirror_bus
        except BTWEyeMovementAndMirrorBus.DoesNotExist:
            BTWEyeMovementAndMirrorBus.objects.create(btw=instance)

        try:
            instance.btw_recognizes_hazards_bus
        except BTWRecognizesHazardsBus.DoesNotExist:
            BTWRecognizesHazardsBus.objects.create(btw=instance)

        try:
            instance.btw_lights_and_signals_bus
        except BTWLightsAndSignalsBus.DoesNotExist:
            BTWLightsAndSignalsBus.objects.create(btw=instance)

        try:
            instance.btw_steering_bus
        except BTWSteeringBus.DoesNotExist:
            BTWSteeringBus.objects.create(btw=instance)

        try:
            instance.btw_backing_bus
        except BTWBackingBus.DoesNotExist:
            BTWBackingBus.objects.create(btw=instance)

        try:
            instance.btw_speed_bus
        except BTWSpeedBus.DoesNotExist:
            BTWSpeedBus.objects.create(btw=instance)

        # 12
        try:
            instance.btw_intersections_bus
        except BTWIntersectionsBus.DoesNotExist:
            BTWIntersectionsBus.objects.create(btw=instance)

        # 13
        try:
            instance.btw_turning_bus
        except BTWTurningBus.DoesNotExist:
            BTWTurningBus.objects.create(btw=instance)

        # 14
        try:
            instance.btw_parking_bus
        except BTWParkingBus.DoesNotExist:
            BTWParkingBus.objects.create(btw=instance)

        # 15
        try:
            instance.btw_hills_bus
        except BTWHillsBus.DoesNotExist:
            BTWHillsBus.objects.create(btw=instance)

        # 16
        try:
            instance.btw_passing_bus
        except BTWPassingBus.DoesNotExist:
            BTWPassingBus.objects.create(btw=instance)

        # 17
        try:
            instance.btw_railroad_crossing_bus
        except BTWRailroadCrossingBus.DoesNotExist:
            BTWRailroadCrossingBus.objects.create(btw=instance)

        # 18
        try:
            instance.btw_general_safety_bus
        except BTWGeneralSafetyAndDOTAdherenceBus.DoesNotExist:
            BTWGeneralSafetyAndDOTAdherenceBus.objects.create(btw=instance)

        # 19
        try:
            instance.btw_internal_environment_bus
        except BTWInternalEnvironmentBus.DoesNotExist:
            BTWInternalEnvironmentBus.objects.create(btw=instance)

