import json

from rest_framework import serializers
from safe_driver.api.v1.mixins import SerializerFiledAttributesMixin, DBTableNameMixin
from safe_driver.api.v1.serializers import StudentTestSerializer, StudentDetailSerializer
from safe_driver.image_functions import base64_to_image_content
from safe_driver.models.btw_class_p import *
from users.api.v1.serializers import UserStudentSerializer


class BTWCabSafetyClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWCabSafetyClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWStartEngineClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWStartEngineClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWEngineOperationClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWEngineOperationClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWBrakesAndStoppingsClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWBrakesAndStoppingsClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWPassengerSafetyClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWPassengerSafetyClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWEyeMovementAndMirrorClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWEyeMovementAndMirrorClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWRecognizesHazardsClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWRecognizesHazardsClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWLightsAndSignalsClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWLightsAndSignalsClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWSteeringClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWSteeringClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWBackingClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWBackingClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWSpeedClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWSpeedClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


# 12
class BTWIntersectionsClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWIntersectionsClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


# 13
class BTWTurningClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWTurningClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


# 14
class BTWParkingClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWParkingClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


# 15
class BTWHillsClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWHillsClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


# 16
class BTWPassingClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWPassingClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


# 17
class BTWRailroadCrossingClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWRailroadCrossingClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


# 18
class BTWGeneralSafetyAndDOTAdherenceClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWGeneralSafetyAndDOTAdherenceClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


# 19
class BTWInternalEnvironmentClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWInternalEnvironmentClassP
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    # student = UserStudentSerializer(read_only=True)
    test = StudentTestSerializer(read_only=True)

    cab_safety = BTWCabSafetyClassPSerializer(source='btw_cab_safety_class_p')
    start_engine = BTWStartEngineClassPSerializer(source='btw_start_engine_class_p')
    engine_operation = BTWEngineOperationClassPSerializer(source='btw_engine_operation_class_p')
    brakes_and_stopping = BTWBrakesAndStoppingsClassPSerializer(source='btw_brakes_and_stopping_class_p')
    passenger_safety = BTWPassengerSafetyClassPSerializer(source='btw_passenger_safety_class_p')
    eye_movement_and_mirror = BTWEyeMovementAndMirrorClassPSerializer(source='btw_eye_movement_and_mirror_class_p')
    recognizes_hazards = BTWRecognizesHazardsClassPSerializer(source='btw_recognizes_hazards_class_p')
    lights_and_signals = BTWLightsAndSignalsClassPSerializer(source='btw_lights_and_signals_class_p')
    steering = BTWSteeringClassPSerializer(source='btw_steering_class_p')
    backing = BTWBackingClassPSerializer(source='btw_backing_class_p')
    speed = BTWSpeedClassPSerializer(source='btw_speed_class_p')

    intersections = BTWIntersectionsClassPSerializer(source='btw_intersections_class_p')
    turning = BTWTurningClassPSerializer(source='btw_turning_class_p')
    parking = BTWParkingClassPSerializer(source='btw_parking_class_p')
    hills = BTWHillsClassPSerializer(source='btw_hills_class_p')
    passing = BTWPassingClassPSerializer(source='btw_passing_class_p')
    railroad_crossing = BTWRailroadCrossingClassPSerializer(source='btw_railroad_crossing_class_p')
    general_safety = BTWGeneralSafetyAndDOTAdherenceClassPSerializer(source='btw_general_safety_class_p')
    internal_environment = BTWInternalEnvironmentClassPSerializer(source='btw_internal_environment_class_p')

    map_data = serializers.JSONField(required=False, write_only=True)
    map_image = serializers.CharField(required=False)

    driver_signature = serializers.CharField(required=False, write_only=True)
    evaluator_signature = serializers.CharField(required=False, write_only=True)
    company_rep_signature = serializers.CharField(required=False, write_only=True)

    def to_representation(self, instance):
        res = super(self.__class__, self).to_representation(instance)
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
        model = BTWClassP
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

        if 'btw_cab_safety_class_p' in validated_data:
            btw_cab_safety_class_p = validated_data.pop('btw_cab_safety_class_p')
            try:
                BTWCabSafetyClassPSerializer().update(instance.btw_cab_safety_class_p,
                                                      btw_cab_safety_class_p)
            except BTWCabSafetyClassP.DoesNotExist:
                BTWCabSafetyClassP.objects.create(btw=instance, **btw_cab_safety_class_p)

        if 'btw_start_engine_class_p' in validated_data:
            btw_start_engine_class_p = validated_data.pop('btw_start_engine_class_p')
            try:
                BTWStartEngineClassPSerializer().update(instance.btw_start_engine_class_p, btw_start_engine_class_p)
            except BTWStartEngineClassP.DoesNotExist:
                BTWStartEngineClassP.objects.create(btw=instance, **btw_start_engine_class_p)

        if 'btw_engine_operation_class_p' in validated_data:
            btw_engine_operation_class_p = validated_data.pop('btw_engine_operation_class_p')
            try:
                BTWEngineOperationClassPSerializer().update(instance.btw_engine_operation_class_p,
                                                            btw_engine_operation_class_p)
            except BTWEngineOperationClassP.DoesNotExist:
                BTWEngineOperationClassP.objects.create(btw=instance, **btw_engine_operation_class_p)

        if 'btw_passenger_safety_class_p' in validated_data:
            btw_passenger_safety_class_p = validated_data.pop('btw_passenger_safety_class_p')
            try:
                BTWPassengerSafetyClassPSerializer().update(instance.btw_passenger_safety_class_p,
                                                            btw_passenger_safety_class_p)
            except BTWPassengerSafetyClassP.DoesNotExist:
                BTWPassengerSafetyClassP.objects.create(btw=instance, **btw_passenger_safety_class_p)

        if 'btw_brakes_and_stopping_class_p' in validated_data:
            btw_brakes_and_stopping_class_p = validated_data.pop('btw_brakes_and_stopping_class_p')
            try:
                BTWBrakesAndStoppingsClassPSerializer().update(instance.btw_brakes_and_stopping_class_p,
                                                               btw_brakes_and_stopping_class_p)
            except BTWBrakesAndStoppingsClassP.DoesNotExist:
                BTWBrakesAndStoppingsClassP.objects.create(btw=instance, **btw_brakes_and_stopping_class_p)

        if 'btw_eye_movement_and_mirror_class_p' in validated_data:
            btw_eye_movement_and_mirror_class_p = validated_data.pop('btw_eye_movement_and_mirror_class_p')
            try:
                BTWEyeMovementAndMirrorClassPSerializer().update(instance.btw_eye_movement_and_mirror_class_p,
                                                                 btw_eye_movement_and_mirror_class_p)
            except BTWEyeMovementAndMirrorClassP.DoesNotExist:
                BTWEyeMovementAndMirrorClassP.objects.create(btw=instance, **btw_eye_movement_and_mirror_class_p)

        if 'btw_recognizes_hazards_class_p' in validated_data:
            btw_recognizes_hazards_class_p = validated_data.pop('btw_recognizes_hazards_class_p')
            try:
                BTWRecognizesHazardsClassPSerializer().update(instance.btw_recognizes_hazards_class_p,
                                                              btw_recognizes_hazards_class_p)
            except BTWRecognizesHazardsClassP.DoesNotExist:
                BTWRecognizesHazardsClassP.objects.create(btw=instance, **btw_recognizes_hazards_class_p)

        if 'btw_lights_and_signals_class_p' in validated_data:

            btw_lights_and_signals_class_p = validated_data.pop('btw_lights_and_signals_class_p')
            try:
                BTWLightsAndSignalsClassPSerializer().update(instance.btw_lights_and_signals_class_p,
                                                             btw_lights_and_signals_class_p)
            except BTWLightsAndSignalsClassP.DoesNotExist:
                BTWLightsAndSignalsClassP.objects.create(btw=instance, **btw_lights_and_signals_class_p)

        if 'btw_steering_class_p' in validated_data:
            btw_steering_class_p = validated_data.pop('btw_steering_class_p')
            try:
                BTWSteeringClassPSerializer().update(instance.btw_steering_class_p, btw_steering_class_p)
            except BTWSteeringClassP.DoesNotExist:
                BTWSteeringClassP.objects.create(btw=instance, **btw_steering_class_p)

        if 'btw_backing_class_p' in validated_data:
            btw_backing_class_p = validated_data.pop('btw_backing_class_p')
            try:
                BTWBackingClassPSerializer().update(instance.btw_backing_class_p, btw_backing_class_p)
            except BTWBackingClassP.DoesNotExist:
                BTWBackingClassP.objects.create(btw=instance, **btw_backing_class_p)

        if 'btw_speed_class_p' in validated_data:
            btw_speed_class_p = validated_data.pop('btw_speed_class_p')
            try:
                BTWSpeedClassPSerializer().update(instance.btw_speed_class_p, btw_speed_class_p)
            except BTWSpeedClassP.DoesNotExist:
                BTWSpeedClassP.objects.create(btw=instance, **btw_speed_class_p)

        if 'btw_intersections_class_p' in validated_data:
            btw_intersections_class_p = validated_data.pop('btw_intersections_class_p')
            try:
                BTWIntersectionsClassPSerializer().update(instance.btw_intersections_class_p, btw_intersections_class_p)
            except BTWIntersectionsClassP.DoesNotExist:
                BTWIntersectionsClassP.objects.create(btw=instance, **btw_intersections_class_p)

        if 'btw_turning_class_p' in validated_data:
            btw_turning_class_p = validated_data.pop('btw_turning_class_p')
            try:
                BTWTurningClassPSerializer().update(instance.btw_turning_class_p, btw_turning_class_p)
            except BTWTurningClassP.DoesNotExist:
                BTWTurningClassP.objects.create(btw=instance, **btw_turning_class_p)

        if 'btw_parking_class_p' in validated_data:
            btw_parking_class_p = validated_data.pop('btw_parking_class_p')
            try:
                BTWParkingClassPSerializer().update(instance.btw_parking_class_p, btw_parking_class_p)
            except BTWIntersectionsClassP.DoesNotExist:
                BTWParkingClassP.objects.create(btw=instance, **btw_parking_class_p)

        if 'btw_hills_class_p' in validated_data:
            btw_hills_class_p = validated_data.pop('btw_hills_class_p')
            try:
                BTWHillsClassPSerializer().update(instance.btw_hills_class_p, btw_hills_class_p)
            except BTWHillsClassP.DoesNotExist:
                BTWHillsClassP.objects.create(btw=instance, **btw_hills_class_p)

        if 'btw_passing_class_p' in validated_data:
            btw_passing_class_p = validated_data.pop('btw_passing_class_p')
            try:
                BTWPassingClassPSerializer().update(instance.btw_passing_class_p, btw_passing_class_p)
            except BTWPassingClassP.DoesNotExist:
                BTWPassingClassP.objects.create(btw=instance, **btw_passing_class_p)

        if 'btw_railroad_crossing_class_p' in validated_data:
            btw_railroad_crossing_class_p = validated_data.pop('btw_railroad_crossing_class_p')
            try:
                BTWRailroadCrossingClassPSerializer().update(instance.btw_railroad_crossing_class_p,
                                                             btw_railroad_crossing_class_p)
            except BTWRailroadCrossingClassP.DoesNotExist:
                BTWRailroadCrossingClassP.objects.create(btw=instance, **btw_railroad_crossing_class_p)

        if 'btw_general_safety_class_p' in validated_data:
            btw_general_safety_class_p = validated_data.pop('btw_general_safety_class_p')
            try:
                BTWGeneralSafetyAndDOTAdherenceClassPSerializer().update(instance.btw_general_safety_class_p,
                                                                         btw_general_safety_class_p)
            except BTWGeneralSafetyAndDOTAdherenceClassP.DoesNotExist:
                BTWGeneralSafetyAndDOTAdherenceClassP.objects.create(btw=instance, **btw_general_safety_class_p)

        if 'btw_internal_environment_class_p' in validated_data:
            btw_internal_environment_class_p = validated_data.pop('btw_internal_environment_class_p')
            try:
                BTWInternalEnvironmentClassPSerializer().update(instance.btw_internal_environment_class_p,
                                                                btw_internal_environment_class_p)
            except BTWInternalEnvironmentClassP.DoesNotExist:
                BTWInternalEnvironmentClassP.objects.create(btw=instance, **btw_internal_environment_class_p)

        return super(BTWClassPSerializer, self).update(instance, validated_data)
