from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models.btw_class_p import *


@receiver(post_save, sender=BTWClassP)
def create_btw_class_p_objects_instance(sender, instance, created, **kwargs):
    if instance:
        try:
            instance.btw_cab_safety_class_p
        except BTWCabSafetyClassP.DoesNotExist:
            BTWCabSafetyClassP.objects.create(btw=instance)

        try:
            instance.btw_start_engine_class_p
        except BTWStartEngineClassP.DoesNotExist:
            BTWStartEngineClassP.objects.create(btw=instance)

        try:
            instance.btw_engine_operation_class_p
        except BTWEngineOperationClassP.DoesNotExist:
            BTWEngineOperationClassP.objects.create(btw=instance)

        try:
            instance.btw_passenger_safety_class_p
        except BTWPassengerSafetyClassP.DoesNotExist:
            BTWPassengerSafetyClassP.objects.create(btw=instance)

        try:
            instance.btw_brakes_and_stopping_class_p
        except BTWBrakesAndStoppingsClassP.DoesNotExist:
            BTWBrakesAndStoppingsClassP.objects.create(btw=instance)

        try:
            instance.btw_eye_movement_and_mirror_class_p
        except BTWEyeMovementAndMirrorClassP.DoesNotExist:
            BTWEyeMovementAndMirrorClassP.objects.create(btw=instance)

        try:
            instance.btw_recognizes_hazards_class_p
        except BTWRecognizesHazardsClassP.DoesNotExist:
            BTWRecognizesHazardsClassP.objects.create(btw=instance)

        try:
            instance.btw_lights_and_signals_class_p
        except BTWLightsAndSignalsClassP.DoesNotExist:
            BTWLightsAndSignalsClassP.objects.create(btw=instance)

        try:
            instance.btw_steering_class_p
        except BTWSteeringClassP.DoesNotExist:
            BTWSteeringClassP.objects.create(btw=instance)

        try:
            instance.btw_backing_class_p
        except BTWBackingClassP.DoesNotExist:
            BTWBackingClassP.objects.create(btw=instance)

        try:
            instance.btw_speed_class_p
        except BTWSpeedClassP.DoesNotExist:
            BTWSpeedClassP.objects.create(btw=instance)

        # 12
        try:
            instance.btw_intersections_class_p
        except BTWIntersectionsClassP.DoesNotExist:
            BTWIntersectionsClassP.objects.create(btw=instance)

        # 13
        try:
            instance.btw_turning_class_p
        except BTWTurningClassP.DoesNotExist:
            BTWTurningClassP.objects.create(btw=instance)

        # 14
        try:
            instance.btw_parking_class_p
        except BTWParkingClassP.DoesNotExist:
            BTWParkingClassP.objects.create(btw=instance)

        # 15
        try:
            instance.btw_hills_class_p
        except BTWHillsClassP.DoesNotExist:
            BTWHillsClassP.objects.create(btw=instance)

        # 16
        try:
            instance.btw_passing_class_p
        except BTWPassingClassP.DoesNotExist:
            BTWPassingClassP.objects.create(btw=instance)

        # 17
        try:
            instance.btw_railroad_crossing_class_p
        except BTWRailroadCrossingClassP.DoesNotExist:
            BTWRailroadCrossingClassP.objects.create(btw=instance)

        # 18
        try:
            instance.btw_general_safety_class_p
        except BTWGeneralSafetyAndDOTAdherenceClassP.DoesNotExist:
            BTWGeneralSafetyAndDOTAdherenceClassP.objects.create(btw=instance)

        # 19
        try:
            instance.btw_internal_environment_class_p
        except BTWInternalEnvironmentClassP.DoesNotExist:
            BTWInternalEnvironmentClassP.objects.create(btw=instance)
