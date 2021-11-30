import json

from rest_framework import serializers
from safe_driver.api.v1.mixins import SerializerFiledAttributesMixin, DBTableNameMixin
from safe_driver.api.v1.serializers import StudentTestSerializer, StudentDetailSerializer
from safe_driver.image_functions import base64_to_image_content
from safe_driver.models.btw_class_a import *
from users.api.v1.serializers import UserStudentSerializer


class BTWCabSafetyClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWCabSafetyClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWStartEngineClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWStartEngineClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWEngineOperationClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWEngineOperationClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWClutchAndTransmissionClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWClutchAndTransmissionClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWCouplingClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWCouplingClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWUncouplingClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWUncouplingClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWBrakesAndStoppingsClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWBrakesAndStoppingsClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWEyeMovementAndMirrorClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWEyeMovementAndMirrorClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWRecognizesHazardsClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWRecognizesHazardsClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWLightsAndSignalsClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWLightsAndSignalsClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWSteeringClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWSteeringClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWBackingClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWBackingClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWSpeedClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWSpeedClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWIntersectionsClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWIntersectionsClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWTurningClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWTurningClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWParkingClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWParkingClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWMultipleTrailersClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWMultipleTrailersClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWHillsClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWHillsClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWPassingClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWPassingClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWGeneralSafetyAndDOTAdherenceClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWGeneralSafetyAndDOTAdherenceClassA
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWClassASerializer(DBTableNameMixin, serializers.ModelSerializer):
    # student = UserStudentSerializer(read_only=True)
    test = StudentTestSerializer(read_only=True)
    cab_safety = BTWCabSafetyClassASerializer(source='btw_cab_safety_class_a')
    start_engine = BTWStartEngineClassASerializer(source='btw_start_engine_class_a')
    engine_operation = BTWEngineOperationClassASerializer(source='btw_engine_operation_class_a')
    clutch_and_transmission = BTWClutchAndTransmissionClassASerializer(source='btw_clutch_and_transmission_class_a')
    coupling = BTWCouplingClassASerializer(source='btw_coupling_class_a', )
    uncoupling = BTWUncouplingClassASerializer(source='btw_uncoupling_class_a')
    brakes_and_stopping = BTWBrakesAndStoppingsClassASerializer(source='btw_brakes_and_stopping_class_a')
    eye_movement_and_mirror = BTWEyeMovementAndMirrorClassASerializer(source='btw_eye_movement_and_mirror_class_a')
    recognizes_hazards = BTWRecognizesHazardsClassASerializer(source='btw_recognizes_hazards_class_a')
    lights_and_signals = BTWLightsAndSignalsClassASerializer(source='btw_lights_and_signals_class_a')
    steering = BTWSteeringClassASerializer(source='btw_steering_class_a')
    backing = BTWBackingClassASerializer(source='btw_backing_class_a')
    speed = BTWSpeedClassASerializer(source='btw_speed_class_a')
    intersections = BTWIntersectionsClassASerializer(source='btw_intersections_class_a')
    turning = BTWTurningClassASerializer(source='btw_turning_class_a', )
    parking = BTWParkingClassASerializer(source='btw_parking_class_a', )
    multiple_trailers = BTWMultipleTrailersClassASerializer(source='btw_multiple_trailers_class_a', )
    hills = BTWHillsClassASerializer(source='btw_hills_class_a', )
    passing = BTWPassingClassASerializer(source='btw_passing_class_a', )
    general_safety_and_dot_adherence = BTWGeneralSafetyAndDOTAdherenceClassASerializer(
        source='btw_general_safety_and_dot_adherence_class_a')

    map_data = serializers.JSONField(required=False, write_only=True)
    map_image = serializers.CharField(required=False)

    driver_signature = serializers.CharField(required=False, write_only=True)
    evaluator_signature = serializers.CharField(required=False, write_only=True)
    company_rep_signature = serializers.CharField(required=False, write_only=True)

    def to_representation(self, instance):
        res = super(BTWClassASerializer, self).to_representation(instance)
        res['student'] = StudentDetailSerializer(instance.test.student).data
        if instance.map_image:
            res['map_image'] = instance.map_image.url
        else:
            res['map_image'] = None

        if instance.driver_signature:
            res['driver_signature'] = instance.driver_signature.url
        else:
            res['driver_signature'] = None
        if instance.evaluator_signature:
            res['evaluator_signature'] = instance.evaluator_signature.url
        else:
            res['evaluator_signature'] = None

        if instance.company_rep_signature:
            res['company_rep_signature'] = instance.company_rep_signature.url
        else:
            res['company_rep_signature'] = None

        if instance.map_data:
            res['map_data'] = json.loads(instance.map_data)
        else:
            res['map_data'] = None
        return res

    class Meta:
        model = BTWClassA
        fields = '__all__'

    def update(self, instance, validated_data):
        # print(validated_data)
        if 'map_data' in validated_data:
            map_data = validated_data.pop('map_data')
            validated_data['map_data'] = json.dumps(map_data)

        if 'map_image' in validated_data:
            map_image = validated_data.pop('map_image')
            image_content_file = base64_to_image_content(map_image)
            validated_data['map_image'] = image_content_file

        if 'driver_signature' in validated_data:
            driver_signature = validated_data.pop('driver_signature')
            image_content_file = base64_to_image_content(driver_signature)
            validated_data['driver_signature'] = image_content_file

        if 'evaluator_signature' in validated_data:
            driver_signature = validated_data.pop('evaluator_signature')
            image_content_file = base64_to_image_content(driver_signature)
            validated_data['evaluator_signature'] = image_content_file

        if 'company_rep_signature' in validated_data:
            driver_signature = validated_data.pop('company_rep_signature')
            image_content_file = base64_to_image_content(driver_signature)
            validated_data['company_rep_signature'] = image_content_file

        if 'btw_cab_safety_class_a' in validated_data:
            btw_cab_safety_class_a = validated_data.pop('btw_cab_safety_class_a')
            try:
                BTWCabSafetyClassASerializer().update(instance.btw_cab_safety_class_a,
                                                      btw_cab_safety_class_a)
            except BTWCabSafetyClassA.DoesNotExist:
                BTWCabSafetyClassA.objects.create(btw=instance, **btw_cab_safety_class_a)

        if 'btw_start_engine_class_a' in validated_data:
            btw_start_engine_class_a = validated_data.pop('btw_start_engine_class_a')
            try:
                BTWStartEngineClassASerializer().update(instance.btw_start_engine_class_a, btw_start_engine_class_a)
            except BTWStartEngineClassA.DoesNotExist:
                BTWStartEngineClassA.objects.create(btw=instance, **btw_start_engine_class_a)

        if 'btw_engine_operation_class_a' in validated_data:
            btw_engine_operation_class_a = validated_data.pop('btw_engine_operation_class_a')
            try:
                BTWEngineOperationClassASerializer().update(instance.btw_engine_operation_class_a,
                                                            btw_engine_operation_class_a)
            except BTWEngineOperationClassA.DoesNotExist:
                BTWEngineOperationClassA.objects.create(btw=instance, **btw_engine_operation_class_a)

        if 'btw_clutch_and_transmission_class_a' in validated_data:
            btw_clutch_and_transmission_class_a = validated_data.pop('btw_clutch_and_transmission_class_a')
            try:
                BTWClutchAndTransmissionClassASerializer().update(instance.btw_clutch_and_transmission_class_a,
                                                                  btw_clutch_and_transmission_class_a)
            except BTWClutchAndTransmissionClassA.DoesNotExist:
                BTWClutchAndTransmissionClassA.objects.create(btw=instance, **btw_clutch_and_transmission_class_a)

        if 'btw_coupling_class_a' in validated_data:
            btw_coupling_class_a = validated_data.pop('btw_coupling_class_a')
            # print(btw_coupling_class_a)
            try:
                BTWCouplingClassASerializer().update(instance.btw_coupling_class_a, btw_coupling_class_a)
            except BTWCouplingClassA.DoesNotExist:
                BTWCouplingClassA.objects.create(btw=instance, **btw_coupling_class_a)

        if 'btw_uncoupling_class_a' in validated_data:
            btw_uncoupling_class_a = validated_data.pop('btw_uncoupling_class_a')
            try:
                BTWUncouplingClassASerializer().update(instance.btw_uncoupling_class_a, btw_uncoupling_class_a)
            except BTWUncouplingClassA.DoesNotExist:
                BTWUncouplingClassA.objects.create(btw=instance, **btw_uncoupling_class_a)

        if 'btw_brakes_and_stopping_class_a' in validated_data:
            btw_brakes_and_stopping_class_a = validated_data.pop('btw_brakes_and_stopping_class_a')
            try:
                BTWBrakesAndStoppingsClassASerializer().update(instance.btw_brakes_and_stopping_class_a,
                                                               btw_brakes_and_stopping_class_a)
            except BTWBrakesAndStoppingsClassA.DoesNotExist:
                BTWBrakesAndStoppingsClassA.objects.create(btw=instance, **btw_brakes_and_stopping_class_a)

        if 'btw_eye_movement_and_mirror_class_a' in validated_data:
            btw_eye_movement_and_mirror_class_a = validated_data.pop('btw_eye_movement_and_mirror_class_a')
            try:
                BTWEyeMovementAndMirrorClassASerializer().update(instance.btw_eye_movement_and_mirror_class_a,
                                                                 btw_eye_movement_and_mirror_class_a)
            except BTWEyeMovementAndMirrorClassA.DoesNotExist:
                BTWEyeMovementAndMirrorClassA.objects.create(btw=instance, **btw_eye_movement_and_mirror_class_a)

        if 'btw_recognizes_hazards_class_a' in validated_data:
            btw_recognizes_hazards_class_a = validated_data.pop('btw_recognizes_hazards_class_a')
            try:
                BTWRecognizesHazardsClassASerializer().update(instance.btw_recognizes_hazards_class_a,
                                                              btw_recognizes_hazards_class_a)
            except BTWRecognizesHazardsClassA.DoesNotExist:
                BTWRecognizesHazardsClassA.objects.create(btw=instance, **btw_recognizes_hazards_class_a)

        if 'btw_lights_and_signals_class_a' in validated_data:

            btw_lights_and_signals_class_a = validated_data.pop('btw_lights_and_signals_class_a')
            try:
                BTWLightsAndSignalsClassASerializer().update(instance.btw_lights_and_signals_class_a,
                                                             btw_lights_and_signals_class_a)
            except BTWLightsAndSignalsClassA.DoesNotExist:
                BTWLightsAndSignalsClassA.objects.create(btw=instance, **btw_lights_and_signals_class_a)

        if 'btw_steering_class_a' in validated_data:
            btw_steering_class_a = validated_data.pop('btw_steering_class_a')
            try:
                BTWSteeringClassASerializer().update(instance.btw_steering_class_a, btw_steering_class_a)
            except BTWSteeringClassA.DoesNotExist:
                BTWSteeringClassA.objects.create(btw=instance, **btw_steering_class_a)

        if 'btw_backing_class_a' in validated_data:
            btw_backing_class_a = validated_data.pop('btw_backing_class_a')
            try:
                BTWBackingClassASerializer().update(instance.btw_backing_class_a, btw_backing_class_a)
            except BTWBackingClassA.DoesNotExist:
                BTWBackingClassA.objects.create(btw=instance, **btw_backing_class_a)

        if 'btw_speed_class_a' in validated_data:
            btw_speed_class_a = validated_data.pop('btw_speed_class_a')
            try:
                BTWSpeedClassASerializer().update(instance.btw_speed_class_a, btw_speed_class_a)
            except BTWSpeedClassA.DoesNotExist:
                BTWSpeedClassA.objects.create(btw=instance, **btw_speed_class_a)

        if 'btw_intersections_class_a' in validated_data:
            btw_intersections_class_a = validated_data.pop('btw_intersections_class_a')
            try:
                BTWIntersectionsClassASerializer().update(instance.btw_intersections_class_a,
                                                          btw_intersections_class_a)
            except BTWIntersectionsClassA.DoesNotExist:
                BTWIntersectionsClassA.objects.create(btw=instance, **btw_intersections_class_a)

        if 'btw_turning_class_a' in validated_data:
            btw_turning_class_a = validated_data.pop('btw_turning_class_a')
            try:
                BTWTurningClassASerializer().update(instance.btw_turning_class_a, btw_turning_class_a)
            except BTWTurningClassA.DoesNotExist:
                BTWTurningClassA.objects.create(btw=instance, **btw_turning_class_a)

        if 'btw_parking_class_a' in validated_data:
            btw_parking_class_a = validated_data.pop('btw_parking_class_a')
            try:
                BTWParkingClassASerializer().update(instance.btw_parking_class_a, btw_parking_class_a)
            except BTWParkingClassA.DoesNotExist:
                BTWParkingClassA.objects.create(btw=instance, **btw_parking_class_a)

        if 'btw_multiple_trailers_class_a' in validated_data:
            btw_multiple_trailers_class_a = validated_data.pop('btw_multiple_trailers_class_a')
            try:
                BTWMultipleTrailersClassASerializer().update(instance.btw_multiple_trailers_class_a,
                                                             btw_multiple_trailers_class_a)
            except BTWMultipleTrailersClassA.DoesNotExist:
                BTWMultipleTrailersClassA.objects.create(btw=instance, **btw_multiple_trailers_class_a)

        if 'btw_hills_class_a' in validated_data:
            btw_hills_class_a = validated_data.pop('btw_hills_class_a')
            try:
                BTWHillsClassASerializer().update(instance.btw_hills_class_a, btw_hills_class_a)
            except BTWHillsClassA.DoesNotExist:
                BTWHillsClassA.objects.create(btw=instance, **btw_hills_class_a)

        if 'btw_passing_class_a' in validated_data:
            btw_passing_class_a = validated_data.pop('btw_passing_class_a')
            try:
                BTWPassingClassASerializer().update(instance.btw_passing_class_a, btw_passing_class_a)
            except BTWPassingClassA.DoesNotExist:
                BTWPassingClassA.objects.create(btw=instance, **btw_passing_class_a)

        if 'btw_general_safety_and_dot_adherence_class_a' in validated_data:
            btw_general_safety_and_dot_adherence_class_a = validated_data.pop(
                'btw_general_safety_and_dot_adherence_class_a')
            try:
                BTWGeneralSafetyAndDOTAdherenceClassASerializer().update(
                    instance.btw_general_safety_and_dot_adherence_class_a, btw_general_safety_and_dot_adherence_class_a)
            except BTWGeneralSafetyAndDOTAdherenceClassA.DoesNotExist:
                BTWGeneralSafetyAndDOTAdherenceClassA.objects.create(btw=instance,
                                                                     **btw_general_safety_and_dot_adherence_class_a)

        return super(BTWClassASerializer, self).update(instance, validated_data)
