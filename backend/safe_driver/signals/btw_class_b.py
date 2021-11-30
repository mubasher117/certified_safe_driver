from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models.btw_class_b import *


@receiver(post_save, sender=BTWClassB)
def create_btw_class_b_objects_instance(sender, instance, created, **kwargs):
    if instance:
        try:
            instance.btw_cab_safety_class_b
        except BTWCabSafetyClassB.DoesNotExist:
            BTWCabSafetyClassB.objects.create(btw=instance)

        try:
            instance.btw_start_engine_class_b
        except BTWStartEngineClassB.DoesNotExist:
            BTWStartEngineClassB.objects.create(btw=instance)

        try:
            instance.btw_engine_operation_class_b
        except BTWEngineOperationClassB.DoesNotExist:
            BTWEngineOperationClassB.objects.create(btw=instance)

        try:
            instance.btw_clutch_and_transmission_class_b
        except BTWClutchAndTransmissionClassB.DoesNotExist:
            BTWClutchAndTransmissionClassB.objects.create(btw=instance)

        try:
            instance.btw_brakes_and_stoppings_class_b
        except BTWBrakesAndStoppingsClassB.DoesNotExist:
            BTWBrakesAndStoppingsClassB.objects.create(btw=instance)

        try:
            instance.btw_eye_movement_and_mirror_class_b
        except BTWEyeMovementAndMirrorClassB.DoesNotExist:
            BTWEyeMovementAndMirrorClassB.objects.create(btw=instance)

        try:
            instance.btw_recognizes_hazards_class_b
        except BTWRecognizesHazardsClassB.DoesNotExist:
            BTWRecognizesHazardsClassB.objects.create(btw=instance)

        try:
            instance.btw_lights_and_signals_class_b
        except BTWLightsAndSignalsClassB.DoesNotExist:
            BTWLightsAndSignalsClassB.objects.create(btw=instance)

        try:
            instance.btw_steering_class_b
        except BTWSteeringClassB.DoesNotExist:
            BTWSteeringClassB.objects.create(btw=instance)

        try:
            instance.btw_backing_class_b
        except BTWBackingClassB.DoesNotExist:
            BTWBackingClassB.objects.create(btw=instance)

        try:
            instance.btw_speed_class_b
        except BTWSpeedClassB.DoesNotExist:
            BTWSpeedClassB.objects.create(btw=instance)

        try:
            instance.btw_intersections_class_b
        except BTWIntersectionsClassB.DoesNotExist:
            BTWIntersectionsClassB.objects.create(btw=instance)

        try:
            instance.btw_turning_class_b
        except BTWTurningClassB.DoesNotExist:
            BTWTurningClassB.objects.create(btw=instance)

        try:
            instance.btw_parking_class_b
        except BTWParkingClassB.DoesNotExist:
            BTWParkingClassB.objects.create(btw=instance)
        try:
            instance.btw_hills_class_b
        except BTWHillsClassB.DoesNotExist:
            BTWHillsClassB.objects.create(btw=instance)

        try:
            instance.btw_passing_class_b
        except BTWPassingClassB.DoesNotExist:
            BTWPassingClassB.objects.create(btw=instance)

        try:
            instance.btw_general_safety_and_dot_adherence_class_b
        except BTWGeneralSafetyAndDOTAdherenceClassB.DoesNotExist:
            BTWGeneralSafetyAndDOTAdherenceClassB.objects.create(btw=instance)
