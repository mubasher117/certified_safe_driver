import json

from rest_framework import serializers
from safe_driver.api.v1.mixins import SerializerFiledAttributesMixin, DBTableNameMixin
from safe_driver.api.v1.serializers import StudentTestSerializer, StudentDetailSerializer
from safe_driver.image_functions import base64_to_image_content
from safe_driver.models.btw_class_c import *
from users.api.v1.serializers import UserStudentSerializer


class BTWCabSafetyClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWCabSafetyClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWStartEngineClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWStartEngineClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWEngineOperationClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWEngineOperationClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWClutchAndTransmissionClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWClutchAndTransmissionClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWBrakesAndStoppingsClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWBrakesAndStoppingsClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWEyeMovementAndMirrorClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWEyeMovementAndMirrorClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWRecognizesHazardsClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWRecognizesHazardsClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWLightsAndSignalsClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWLightsAndSignalsClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWSteeringClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWSteeringClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWBackingClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWBackingClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWSpeedClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWSpeedClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWIntersectionsClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWIntersectionsClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWTurningClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWTurningClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWParkingClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWParkingClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWHillsClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWHillsClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWPassingClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWPassingClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWGeneralSafetyAndDOTAdherenceClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWGeneralSafetyAndDOTAdherenceClassC
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWClassCSerializer(DBTableNameMixin, serializers.ModelSerializer):
    # student = UserStudentSerializer(read_only=True)
    test = StudentTestSerializer(read_only=True)
    cab_safety = BTWCabSafetyClassCSerializer(source='btw_cab_safety_class_c')
    start_engine = BTWStartEngineClassCSerializer(source='btw_start_engine_class_c')
    engine_operation = BTWEngineOperationClassCSerializer(source='btw_engine_operation_class_c')
    clutch_and_transmission = BTWClutchAndTransmissionClassCSerializer(source='btw_clutch_and_transmission_class_c')
    brakes_and_stopping = BTWBrakesAndStoppingsClassCSerializer(source='btw_brakes_and_stoppings_class_c')
    eye_movement_and_mirror = BTWEyeMovementAndMirrorClassCSerializer(source='btw_eye_movement_and_mirror_class_c')
    recognizes_hazards = BTWRecognizesHazardsClassCSerializer(source='btw_recognizes_hazards_class_c')
    lights_and_signals = BTWLightsAndSignalsClassCSerializer(source='btw_lights_and_signals_class_c')
    steering = BTWSteeringClassCSerializer(source='btw_steering_class_c')
    backing = BTWBackingClassCSerializer(source='btw_backing_class_c')
    speed = BTWSpeedClassCSerializer(source='btw_speed_class_c')
    intersections = BTWIntersectionsClassCSerializer(source='btw_intersections_class_c')
    turning = BTWTurningClassCSerializer(source='btw_turning_class_c', )
    parking = BTWParkingClassCSerializer(source='btw_parking_class_c', )
    hills = BTWHillsClassCSerializer(source='btw_hills_class_c', )
    passing = BTWPassingClassCSerializer(source='btw_passing_class_c', )
    general_safety_and_dot_adherence = BTWGeneralSafetyAndDOTAdherenceClassCSerializer(
        source='btw_general_safety_and_dot_adherence_class_c')

    map_data = serializers.JSONField(required=False, write_only=True)
    map_image = serializers.CharField(required=False)

    driver_signature = serializers.CharField(required=False, write_only=True)
    evaluator_signature = serializers.CharField(required=False, write_only=True)
    company_rep_signature = serializers.CharField(required=False, write_only=True)

    def to_representation(self, instance):
        res = super(BTWClassCSerializer, self).to_representation(instance)
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
        model = BTWClassC
        fields = '__all__'

    def update(self, instance, validated_data):
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

        if 'btw_cab_safety_class_c' in validated_data:
            btw_cab_safety_class_c = validated_data.pop('btw_cab_safety_class_c')
            try:
                BTWCabSafetyClassCSerializer().update(instance.btw_cab_safety_class_c,
                                                      btw_cab_safety_class_c)
            except BTWCabSafetyClassC.DoesNotExist:
                BTWCabSafetyClassC.objects.create(btw=instance, **btw_cab_safety_class_c)

        if 'btw_start_engine_class_c' in validated_data:
            btw_start_engine_class_c = validated_data.pop('btw_start_engine_class_c')
            try:
                BTWStartEngineClassCSerializer().update(instance.btw_start_engine_class_c, btw_start_engine_class_c)
            except BTWStartEngineClassC.DoesNotExist:
                BTWStartEngineClassC.objects.create(btw=instance, **btw_start_engine_class_c)

        if 'btw_engine_operation_class_c' in validated_data:
            btw_engine_operation_class_c = validated_data.pop('btw_engine_operation_class_c')
            try:
                BTWEngineOperationClassCSerializer().update(instance.btw_engine_operation_class_c,
                                                            btw_engine_operation_class_c)
            except BTWEngineOperationClassC.DoesNotExist:
                BTWEngineOperationClassC.objects.create(btw=instance, **btw_engine_operation_class_c)

        if 'btw_clutch_and_transmission_class_c' in validated_data:
            btw_clutch_and_transmission_class_c = validated_data.pop('btw_clutch_and_transmission_class_c')
            try:
                BTWClutchAndTransmissionClassCSerializer().update(instance.btw_clutch_and_transmission_class_c,
                                                                  btw_clutch_and_transmission_class_c)
            except BTWClutchAndTransmissionClassC.DoesNotExist:
                BTWClutchAndTransmissionClassC.objects.create(btw=instance, **btw_clutch_and_transmission_class_c)

        if 'btw_brakes_and_stoppings_class_c' in validated_data:
            btw_brakes_and_stoppings_class_c = validated_data.pop('btw_brakes_and_stoppings_class_c')
            try:
                BTWBrakesAndStoppingsClassCSerializer().update(instance.btw_brakes_and_stoppings_class_c,
                                                               btw_brakes_and_stoppings_class_c)
            except BTWBrakesAndStoppingsClassC.DoesNotExist:
                BTWBrakesAndStoppingsClassC.objects.create(btw=instance, **btw_brakes_and_stoppings_class_c)

        if 'btw_eye_movement_and_mirror_class_c' in validated_data:
            btw_eye_movement_and_mirror_class_c = validated_data.pop('btw_eye_movement_and_mirror_class_c')
            try:
                BTWEyeMovementAndMirrorClassCSerializer().update(instance.btw_eye_movement_and_mirror_class_c,
                                                                 btw_eye_movement_and_mirror_class_c)
            except BTWEyeMovementAndMirrorClassC.DoesNotExist:
                BTWEyeMovementAndMirrorClassC.objects.create(btw=instance, **btw_eye_movement_and_mirror_class_c)

        if 'btw_recognizes_hazards_class_c' in validated_data:
            btw_recognizes_hazards_class_c = validated_data.pop('btw_recognizes_hazards_class_c')
            try:
                BTWRecognizesHazardsClassCSerializer().update(instance.btw_recognizes_hazards_class_c,
                                                              btw_recognizes_hazards_class_c)
            except BTWRecognizesHazardsClassC.DoesNotExist:
                BTWRecognizesHazardsClassC.objects.create(btw=instance, **btw_recognizes_hazards_class_c)

        if 'btw_lights_and_signals_class_c' in validated_data:

            btw_lights_and_signals_class_c = validated_data.pop('btw_lights_and_signals_class_c')
            try:
                BTWLightsAndSignalsClassCSerializer().update(instance.btw_lights_and_signals_class_c,
                                                             btw_lights_and_signals_class_c)
            except BTWLightsAndSignalsClassC.DoesNotExist:
                BTWLightsAndSignalsClassC.objects.create(btw=instance, **btw_lights_and_signals_class_c)

        if 'btw_steering_class_c' in validated_data:
            btw_steering_class_c = validated_data.pop('btw_steering_class_c')
            try:
                BTWSteeringClassCSerializer().update(instance.btw_steering_class_c, btw_steering_class_c)
            except BTWSteeringClassC.DoesNotExist:
                BTWSteeringClassC.objects.create(btw=instance, **btw_steering_class_c)

        if 'btw_backing_class_c' in validated_data:
            btw_backing_class_c = validated_data.pop('btw_backing_class_c')
            try:
                BTWBackingClassCSerializer().update(instance.btw_backing_class_c, btw_backing_class_c)
            except BTWBackingClassC.DoesNotExist:
                BTWBackingClassC.objects.create(btw=instance, **btw_backing_class_c)

        if 'btw_speed_class_c' in validated_data:
            btw_speed_class_c = validated_data.pop('btw_speed_class_c')
            try:
                BTWSpeedClassCSerializer().update(instance.btw_speed_class_c, btw_speed_class_c)
            except BTWSpeedClassC.DoesNotExist:
                BTWSpeedClassC.objects.create(btw=instance, **btw_speed_class_c)

        if 'btw_intersections_class_c' in validated_data:
            btw_intersections_class_c = validated_data.pop('btw_intersections_class_c')
            try:
                BTWIntersectionsClassCSerializer().update(instance.btw_intersections_class_c,
                                                          btw_intersections_class_c)
            except BTWIntersectionsClassC.DoesNotExist:
                BTWIntersectionsClassC.objects.create(btw=instance, **btw_intersections_class_c)

        if 'btw_turning_class_c' in validated_data:
            btw_turning_class_c = validated_data.pop('btw_turning_class_c')
            try:
                BTWTurningClassCSerializer().update(instance.btw_turning_class_c, btw_turning_class_c)
            except BTWTurningClassC.DoesNotExist:
                BTWTurningClassC.objects.create(btw=instance, **btw_turning_class_c)

        if 'btw_parking_class_c' in validated_data:
            btw_parking_class_c = validated_data.pop('btw_parking_class_c')
            try:
                BTWParkingClassCSerializer().update(instance.btw_parking_class_c, btw_parking_class_c)
            except BTWParkingClassC.DoesNotExist:
                BTWParkingClassC.objects.create(btw=instance, **btw_parking_class_c)

        if 'btw_hills_class_c' in validated_data:
            btw_hills_class_c = validated_data.pop('btw_hills_class_c')
            try:
                BTWHillsClassCSerializer().update(instance.btw_hills_class_c, btw_hills_class_c)
            except BTWHillsClassC.DoesNotExist:
                BTWHillsClassC.objects.create(btw=instance, **btw_hills_class_c)

        if 'btw_passing_class_c' in validated_data:
            btw_passing_class_c = validated_data.pop('btw_passing_class_c')
            try:
                BTWPassingClassCSerializer().update(instance.btw_passing_class_c, btw_passing_class_c)
            except BTWPassingClassC.DoesNotExist:
                BTWPassingClassC.objects.create(btw=instance, **btw_passing_class_c)

        if 'btw_general_safety_and_dot_adherence_class_c' in validated_data:
            btw_general_safety_and_dot_adherence_class_c = validated_data.pop(
                'btw_general_safety_and_dot_adherence_class_c')
            try:
                BTWGeneralSafetyAndDOTAdherenceClassCSerializer().update(
                    instance.btw_general_safety_and_dot_adherence_class_c, btw_general_safety_and_dot_adherence_class_c)
            except BTWGeneralSafetyAndDOTAdherenceClassC.DoesNotExist:
                BTWGeneralSafetyAndDOTAdherenceClassC.objects.create(btw=instance,
                                                                     **btw_general_safety_and_dot_adherence_class_c)

        return super(BTWClassCSerializer, self).update(instance, validated_data)
