from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models.btw_class_c import *


@receiver(post_save, sender=BTWClassC)
def create_btw_class_c_objects_instance(sender, instance, created, **kwargs):
    if instance:
        try:
            instance.btw_cab_safety_class_c
        except BTWCabSafetyClassC.DoesNotExist:
            BTWCabSafetyClassC.objects.create(btw=instance)

        try:
            instance.btw_start_engine_class_c
        except BTWStartEngineClassC.DoesNotExist:
            BTWStartEngineClassC.objects.create(btw=instance)

        try:
            instance.btw_engine_operation_class_c
        except BTWEngineOperationClassC.DoesNotExist:
            BTWEngineOperationClassC.objects.create(btw=instance)

        try:
            instance.btw_clutch_and_transmission_class_c
        except BTWClutchAndTransmissionClassC.DoesNotExist:
            BTWClutchAndTransmissionClassC.objects.create(btw=instance)

        try:
            instance.btw_brakes_and_stoppings_class_c
        except BTWBrakesAndStoppingsClassC.DoesNotExist:
            BTWBrakesAndStoppingsClassC.objects.create(btw=instance)

        try:
            instance.btw_eye_movement_and_mirror_class_c
        except BTWEyeMovementAndMirrorClassC.DoesNotExist:
            BTWEyeMovementAndMirrorClassC.objects.create(btw=instance)

        try:
            instance.btw_recognizes_hazards_class_c
        except BTWRecognizesHazardsClassC.DoesNotExist:
            BTWRecognizesHazardsClassC.objects.create(btw=instance)

        try:
            instance.btw_lights_and_signals_class_c
        except BTWLightsAndSignalsClassC.DoesNotExist:
            BTWLightsAndSignalsClassC.objects.create(btw=instance)

        try:
            instance.btw_steering_class_c
        except BTWSteeringClassC.DoesNotExist:
            BTWSteeringClassC.objects.create(btw=instance)

        try:
            instance.btw_backing_class_c
        except BTWBackingClassC.DoesNotExist:
            BTWBackingClassC.objects.create(btw=instance)

        try:
            instance.btw_speed_class_c
        except BTWSpeedClassC.DoesNotExist:
            BTWSpeedClassC.objects.create(btw=instance)

        try:
            instance.btw_intersections_class_c
        except BTWIntersectionsClassC.DoesNotExist:
            BTWIntersectionsClassC.objects.create(btw=instance)

        try:
            instance.btw_turning_class_c
        except BTWTurningClassC.DoesNotExist:
            BTWTurningClassC.objects.create(btw=instance)

        try:
            instance.btw_parking_class_c
        except BTWParkingClassC.DoesNotExist:
            BTWParkingClassC.objects.create(btw=instance)

        try:
            instance.btw_hills_class_c
        except BTWHillsClassC.DoesNotExist:
            BTWHillsClassC.objects.create(btw=instance)

        try:
            instance.btw_passing_class_c
        except BTWPassingClassC.DoesNotExist:
            BTWPassingClassC.objects.create(btw=instance)

        try:
            instance.btw_general_safety_and_dot_adherence_class_c
        except BTWGeneralSafetyAndDOTAdherenceClassC.DoesNotExist:
            BTWGeneralSafetyAndDOTAdherenceClassC.objects.create(btw=instance)
