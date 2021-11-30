import json

from rest_framework import serializers
from safe_driver.api.v1.mixins import SerializerFiledAttributesMixin, DBTableNameMixin
from safe_driver.api.v1.serializers import (StudentTestSerializer, StudentDetailSerializer)
from safe_driver.image_functions import base64_to_image_content
from safe_driver.models.btw_class_b import *
from users.api.v1.serializers import (UserStudentSerializer)


class BTWCabSafetyClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWCabSafetyClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWStartEngineClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWStartEngineClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWEngineOperationClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWEngineOperationClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWClutchAndTransmissionClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWClutchAndTransmissionClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWBrakesAndStoppingsClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWBrakesAndStoppingsClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWEyeMovementAndMirrorClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWEyeMovementAndMirrorClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWRecognizesHazardsClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWRecognizesHazardsClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWLightsAndSignalsClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWLightsAndSignalsClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWSteeringClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWSteeringClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWBackingClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWBackingClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWSpeedClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWSpeedClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWIntersectionsClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWIntersectionsClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWTurningClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWTurningClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWParkingClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWParkingClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWHillsClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWHillsClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWPassingClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWPassingClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWGeneralSafetyAndDOTAdherenceClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWGeneralSafetyAndDOTAdherenceClassB
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWClassBSerializer(DBTableNameMixin, serializers.ModelSerializer):
    # student = UserStudentSerializer(read_only=True)
    test = StudentTestSerializer(read_only=True)
    cab_safety = BTWCabSafetyClassBSerializer(source='btw_cab_safety_class_b')
    start_engine = BTWStartEngineClassBSerializer(source='btw_start_engine_class_b')
    engine_operation = BTWEngineOperationClassBSerializer(source='btw_engine_operation_class_b')
    clutch_and_transmission = BTWClutchAndTransmissionClassBSerializer(source='btw_clutch_and_transmission_class_b')
    brakes_and_stopping = BTWBrakesAndStoppingsClassBSerializer(source='btw_brakes_and_stoppings_class_b')
    eye_movement_and_mirror = BTWEyeMovementAndMirrorClassBSerializer(source='btw_eye_movement_and_mirror_class_b')
    recognizes_hazards = BTWRecognizesHazardsClassBSerializer(source='btw_recognizes_hazards_class_b')
    lights_and_signals = BTWLightsAndSignalsClassBSerializer(source='btw_lights_and_signals_class_b')
    steering = BTWSteeringClassBSerializer(source='btw_steering_class_b')
    backing = BTWBackingClassBSerializer(source='btw_backing_class_b')
    speed = BTWSpeedClassBSerializer(source='btw_speed_class_b')
    intersections = BTWIntersectionsClassBSerializer(source='btw_intersections_class_b')
    turning = BTWTurningClassBSerializer(source='btw_turning_class_b', )
    parking = BTWParkingClassBSerializer(source='btw_parking_class_b', )
    hills = BTWHillsClassBSerializer(source='btw_hills_class_b', )
    passing = BTWPassingClassBSerializer(source='btw_passing_class_b', )
    general_safety_and_dot_adherence = BTWGeneralSafetyAndDOTAdherenceClassBSerializer(
        source='btw_general_safety_and_dot_adherence_class_b')

    map_data = serializers.JSONField(required=False, write_only=True)
    map_image = serializers.CharField(required=False)

    driver_signature = serializers.CharField(required=False, write_only=True)
    evaluator_signature = serializers.CharField(required=False, write_only=True)
    company_rep_signature = serializers.CharField(required=False, write_only=True)

    def to_representation(self, instance):
        res = super(BTWClassBSerializer, self).to_representation(instance)
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
        model = BTWClassB
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

        if 'btw_cab_safety_class_b' in validated_data:
            btw_cab_safety_class_b = validated_data.pop('btw_cab_safety_class_b')
            try:
                BTWCabSafetyClassBSerializer().update(instance.btw_cab_safety_class_b,
                                                      btw_cab_safety_class_b)
            except BTWCabSafetyClassB.DoesNotExist:
                BTWCabSafetyClassB.objects.create(btw=instance, **btw_cab_safety_class_b)

        if 'btw_start_engine_class_b' in validated_data:
            btw_start_engine_class_b = validated_data.pop('btw_start_engine_class_b')
            try:
                BTWStartEngineClassBSerializer().update(instance.btw_start_engine_class_b, btw_start_engine_class_b)
            except BTWStartEngineClassB.DoesNotExist:
                BTWStartEngineClassB.objects.create(btw=instance, **btw_start_engine_class_b)

        if 'btw_engine_operation_class_b' in validated_data:
            btw_engine_operation_class_b = validated_data.pop('btw_engine_operation_class_b')
            try:
                BTWEngineOperationClassBSerializer().update(instance.btw_engine_operation_class_b,
                                                            btw_engine_operation_class_b)
            except BTWEngineOperationClassB.DoesNotExist:
                BTWEngineOperationClassB.objects.create(btw=instance, **btw_engine_operation_class_b)

        if 'btw_clutch_and_transmission_class_b' in validated_data:
            btw_clutch_and_transmission_class_b = validated_data.pop('btw_clutch_and_transmission_class_b')
            try:
                BTWClutchAndTransmissionClassBSerializer().update(instance.btw_clutch_and_transmission_class_b,
                                                                  btw_clutch_and_transmission_class_b)
            except BTWClutchAndTransmissionClassB.DoesNotExist:
                BTWClutchAndTransmissionClassB.objects.create(btw=instance, **btw_clutch_and_transmission_class_b)

        if 'btw_brakes_and_stoppings_class_b' in validated_data:
            btw_brakes_and_stoppings_class_b = validated_data.pop('btw_brakes_and_stoppings_class_b')
            try:
                BTWBrakesAndStoppingsClassBSerializer().update(instance.btw_brakes_and_stoppings_class_b,
                                                               btw_brakes_and_stoppings_class_b)
            except BTWBrakesAndStoppingsClassB.DoesNotExist:
                BTWBrakesAndStoppingsClassB.objects.create(btw=instance, **btw_brakes_and_stoppings_class_b)

        if 'btw_eye_movement_and_mirror_class_b' in validated_data:
            btw_eye_movement_and_mirror_class_b = validated_data.pop('btw_eye_movement_and_mirror_class_b')
            try:
                BTWEyeMovementAndMirrorClassBSerializer().update(instance.btw_eye_movement_and_mirror_class_b,
                                                                 btw_eye_movement_and_mirror_class_b)
            except BTWEyeMovementAndMirrorClassB.DoesNotExist:
                BTWEyeMovementAndMirrorClassB.objects.create(btw=instance, **btw_eye_movement_and_mirror_class_b)

        if 'btw_recognizes_hazards_class_b' in validated_data:
            btw_recognizes_hazards_class_b = validated_data.pop('btw_recognizes_hazards_class_b')
            try:
                BTWRecognizesHazardsClassBSerializer().update(instance.btw_recognizes_hazards_class_b,
                                                              btw_recognizes_hazards_class_b)
            except BTWRecognizesHazardsClassB.DoesNotExist:
                BTWRecognizesHazardsClassB.objects.create(btw=instance, **btw_recognizes_hazards_class_b)

        if 'btw_lights_and_signals_class_b' in validated_data:

            btw_lights_and_signals_class_b = validated_data.pop('btw_lights_and_signals_class_b')
            try:
                BTWLightsAndSignalsClassBSerializer().update(instance.btw_lights_and_signals_class_b,
                                                             btw_lights_and_signals_class_b)
            except BTWLightsAndSignalsClassB.DoesNotExist:
                BTWLightsAndSignalsClassB.objects.create(btw=instance, **btw_lights_and_signals_class_b)

        if 'btw_steering_class_b' in validated_data:
            btw_steering_class_b = validated_data.pop('btw_steering_class_b')
            try:
                BTWSteeringClassBSerializer().update(instance.btw_steering_class_b, btw_steering_class_b)
            except BTWSteeringClassB.DoesNotExist:
                BTWSteeringClassB.objects.create(btw=instance, **btw_steering_class_b)

        if 'btw_backing_class_b' in validated_data:
            btw_backing_class_b = validated_data.pop('btw_backing_class_b')
            try:
                BTWBackingClassBSerializer().update(instance.btw_backing_class_b, btw_backing_class_b)
            except BTWBackingClassB.DoesNotExist:
                BTWBackingClassB.objects.create(btw=instance, **btw_backing_class_b)

        if 'btw_speed_class_b' in validated_data:
            btw_speed_class_b = validated_data.pop('btw_speed_class_b')
            try:
                BTWSpeedClassBSerializer().update(instance.btw_speed_class_b, btw_speed_class_b)
            except BTWSpeedClassB.DoesNotExist:
                BTWSpeedClassB.objects.create(btw=instance, **btw_speed_class_b)

        if 'btw_intersections_class_b' in validated_data:
            btw_intersections_class_b = validated_data.pop('btw_intersections_class_b')
            try:
                BTWIntersectionsClassBSerializer().update(instance.btw_intersections_class_b,
                                                          btw_intersections_class_b)
            except BTWIntersectionsClassB.DoesNotExist:
                BTWIntersectionsClassB.objects.create(btw=instance, **btw_intersections_class_b)

        if 'btw_turning_class_b' in validated_data:
            btw_turning_class_b = validated_data.pop('btw_turning_class_b')
            try:
                BTWTurningClassBSerializer().update(instance.btw_turning_class_b, btw_turning_class_b)
            except BTWTurningClassB.DoesNotExist:
                BTWTurningClassB.objects.create(btw=instance, **btw_turning_class_b)

        if 'btw_parking_class_b' in validated_data:
            btw_parking_class_b = validated_data.pop('btw_parking_class_b')
            try:
                BTWParkingClassBSerializer().update(instance.btw_parking_class_b, btw_parking_class_b)
            except BTWParkingClassB.DoesNotExist:
                BTWParkingClassB.objects.create(btw=instance, **btw_parking_class_b)

        if 'btw_hills_class_b' in validated_data:
            btw_hills_class_b = validated_data.pop('btw_hills_class_b')
            try:
                BTWHillsClassBSerializer().update(instance.btw_hills_class_b, btw_hills_class_b)
            except BTWHillsClassB.DoesNotExist:
                BTWHillsClassB.objects.create(btw=instance, **btw_hills_class_b)

        if 'btw_passing_class_b' in validated_data:
            btw_passing_class_b = validated_data.pop('btw_passing_class_b')
            try:
                BTWPassingClassBSerializer().update(instance.btw_passing_class_b, btw_passing_class_b)
            except BTWPassingClassB.DoesNotExist:
                BTWPassingClassB.objects.create(btw=instance, **btw_passing_class_b)

        if 'btw_general_safety_and_dot_adherence_class_b' in validated_data:
            btw_general_safety_and_dot_adherence_class_b = validated_data.pop(
                'btw_general_safety_and_dot_adherence_class_b')
            try:
                BTWGeneralSafetyAndDOTAdherenceClassBSerializer().update(
                    instance.btw_general_safety_and_dot_adherence_class_b, btw_general_safety_and_dot_adherence_class_b)
            except BTWGeneralSafetyAndDOTAdherenceClassB.DoesNotExist:
                BTWGeneralSafetyAndDOTAdherenceClassB.objects.create(btw=instance,
                                                                     **btw_general_safety_and_dot_adherence_class_b)

        return super(BTWClassBSerializer, self).update(instance, validated_data)
