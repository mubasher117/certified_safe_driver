from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models.btw_class_a import *


@receiver(post_save, sender=BTWClassA)
def create_btw_class_a_objects_instance(sender, instance, created, **kwargs):
    if instance:
        try:
            instance.btw_cab_safety_class_a
        except BTWCabSafetyClassA.DoesNotExist:
            BTWCabSafetyClassA.objects.create(btw=instance)

        try:
            instance.btw_start_engine_class_a
        except BTWStartEngineClassA.DoesNotExist:
            BTWStartEngineClassA.objects.create(btw=instance)

        try:
            instance.btw_engine_operation_class_a
        except BTWEngineOperationClassA.DoesNotExist:
            BTWEngineOperationClassA.objects.create(btw=instance)

        try:
            instance.btw_clutch_and_transmission_class_a
        except BTWClutchAndTransmissionClassA.DoesNotExist:
            BTWClutchAndTransmissionClassA.objects.create(btw=instance)

        try:
            instance.btw_coupling_class_a
        except BTWCouplingClassA.DoesNotExist:
            BTWCouplingClassA.objects.create(btw=instance)

        try:
            instance.btw_uncoupling_class_a
        except BTWUncouplingClassA.DoesNotExist:
            BTWUncouplingClassA.objects.create(btw=instance)

        try:
            instance.btw_brakes_and_stopping_class_a
        except BTWBrakesAndStoppingsClassA.DoesNotExist:
            BTWBrakesAndStoppingsClassA.objects.create(btw=instance)

        try:
            instance.btw_eye_movement_and_mirror_class_a
        except BTWEyeMovementAndMirrorClassA.DoesNotExist:
            BTWEyeMovementAndMirrorClassA.objects.create(btw=instance)

        try:
            instance.btw_recognizes_hazards_class_a
        except BTWRecognizesHazardsClassA.DoesNotExist:
            BTWRecognizesHazardsClassA.objects.create(btw=instance)

        try:
            instance.btw_lights_and_signals_class_a
        except BTWLightsAndSignalsClassA.DoesNotExist:
            BTWLightsAndSignalsClassA.objects.create(btw=instance)

        try:
            instance.btw_steering_class_a
        except BTWSteeringClassA.DoesNotExist:
            BTWSteeringClassA.objects.create(btw=instance)

        try:
            instance.btw_backing_class_a
        except BTWBackingClassA.DoesNotExist:
            BTWBackingClassA.objects.create(btw=instance)

        try:
            instance.btw_speed_class_a
        except BTWSpeedClassA.DoesNotExist:
            BTWSpeedClassA.objects.create(btw=instance)

        try:
            instance.btw_intersections_class_a
        except BTWIntersectionsClassA.DoesNotExist:
            BTWIntersectionsClassA.objects.create(btw=instance)

        try:
            instance.btw_turning_class_a
        except BTWTurningClassA.DoesNotExist:
            BTWTurningClassA.objects.create(btw=instance)

        try:
            instance.btw_parking_class_a
        except BTWParkingClassA.DoesNotExist:
            BTWParkingClassA.objects.create(btw=instance)

        try:
            instance.btw_multiple_trailers_class_a
        except BTWMultipleTrailersClassA.DoesNotExist:
            BTWMultipleTrailersClassA.objects.create(btw=instance)

        try:
            instance.btw_hills_class_a
        except BTWHillsClassA.DoesNotExist:
            BTWHillsClassA.objects.create(btw=instance)

        try:
            instance.btw_passing_class_a
        except BTWPassingClassA.DoesNotExist:
            BTWPassingClassA.objects.create(btw=instance)

        try:
            instance.btw_general_safety_and_dot_adherence_class_a
        except BTWGeneralSafetyAndDOTAdherenceClassA.DoesNotExist:
            BTWGeneralSafetyAndDOTAdherenceClassA.objects.create(btw=instance)
