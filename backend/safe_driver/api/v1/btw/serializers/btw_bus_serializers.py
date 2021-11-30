import json

from rest_framework import serializers
from safe_driver.api.v1.mixins import SerializerFiledAttributesMixin, DBTableNameMixin
from safe_driver.api.v1.serializers import StudentTestSerializer, StudentDetailSerializer
from safe_driver.image_functions import base64_to_image_content
from safe_driver.models.btw_bus import *
from users.api.v1.serializers import UserStudentSerializer


class BTWCabSafetyBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWCabSafetyBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWStartEngineBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWStartEngineBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWEngineOperationBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWEngineOperationBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWBrakesAndStoppingsBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWBrakesAndStoppingsBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWPassengerSafetyBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWPassengerSafetyBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWEyeMovementAndMirrorBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWEyeMovementAndMirrorBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWRecognizesHazardsBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWRecognizesHazardsBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWLightsAndSignalsBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWLightsAndSignalsBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWSteeringBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWSteeringBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWBackingBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWBackingBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWSpeedBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWSpeedBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


# 12
class BTWIntersectionsBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWIntersectionsBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


# 13
class BTWTurningBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWTurningBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


# 14
class BTWParkingBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWParkingBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


# 15
class BTWHillsBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWHillsBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


# 16
class BTWPassingBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWPassingBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


# 17
class BTWRailroadCrossingBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWRailroadCrossingBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


# 18
class BTWGeneralSafetyAndDOTAdherenceBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWGeneralSafetyAndDOTAdherenceBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


# 19
class BTWInternalEnvironmentBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWInternalEnvironmentBus
        fields = '__all__'
        extra_kwargs = {
            'btw': {
                'read_only': True
            }
        }


class BTWBusSerializer(DBTableNameMixin, serializers.ModelSerializer):
    # student = UserStudentSerializer(read_only=True)
    test = StudentTestSerializer(read_only=True)

    cab_safety = BTWCabSafetyBusSerializer(source='btw_cab_safety_bus')
    start_engine = BTWStartEngineBusSerializer(source='btw_start_engine_bus')
    engine_operation = BTWEngineOperationBusSerializer(source='btw_engine_operation_bus')
    brakes_and_stopping = BTWBrakesAndStoppingsBusSerializer(source='btw_brakes_and_stopping_bus')
    passenger_safety = BTWPassengerSafetyBusSerializer(source='btw_passenger_safety_bus')
    eye_movement_and_mirror = BTWEyeMovementAndMirrorBusSerializer(source='btw_eye_movement_and_mirror_bus')
    recognizes_hazards = BTWRecognizesHazardsBusSerializer(source='btw_recognizes_hazards_bus')
    lights_and_signals = BTWLightsAndSignalsBusSerializer(source='btw_lights_and_signals_bus')
    steering = BTWSteeringBusSerializer(source='btw_steering_bus')
    backing = BTWBackingBusSerializer(source='btw_backing_bus')
    speed = BTWSpeedBusSerializer(source='btw_speed_bus')

    intersections = BTWIntersectionsBusSerializer(source='btw_intersections_bus')
    turning = BTWTurningBusSerializer(source='btw_turning_bus')
    parking = BTWParkingBusSerializer(source='btw_parking_bus')
    hills = BTWHillsBusSerializer(source='btw_hills_bus')
    passing = BTWPassingBusSerializer(source='btw_passing_bus')
    railroad_crossing = BTWRailroadCrossingBusSerializer(source='btw_railroad_crossing_bus')
    general_safety = BTWGeneralSafetyAndDOTAdherenceBusSerializer(source='btw_general_safety_bus')
    internal_environment = BTWInternalEnvironmentBusSerializer(source='btw_internal_environment_bus')

    map_data = serializers.JSONField(required=False, write_only=True)
    map_image = serializers.CharField(required=False)

    driver_signature = serializers.CharField(required=False, write_only=True)
    evaluator_signature = serializers.CharField(required=False, write_only=True)
    company_rep_signature = serializers.CharField(required=False, write_only=True)

    def to_representation(self, instance):
        res = super(BTWBusSerializer, self).to_representation(instance)
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
        model = BTWBus
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

        if 'btw_cab_safety_bus' in validated_data:
            btw_cab_safety_bus = validated_data.pop('btw_cab_safety_bus')
            try:
                BTWCabSafetyBusSerializer().update(instance.btw_cab_safety_bus,
                                                   btw_cab_safety_bus)
            except BTWCabSafetyBus.DoesNotExist:
                BTWCabSafetyBus.objects.create(btw=instance, **btw_cab_safety_bus)

        if 'btw_start_engine_bus' in validated_data:
            btw_start_engine_bus = validated_data.pop('btw_start_engine_bus')
            try:
                BTWStartEngineBusSerializer().update(instance.btw_start_engine_bus, btw_start_engine_bus)
            except BTWStartEngineBus.DoesNotExist:
                BTWStartEngineBus.objects.create(btw=instance, **btw_start_engine_bus)

        if 'btw_engine_operation_bus' in validated_data:
            btw_engine_operation_bus = validated_data.pop('btw_engine_operation_bus')
            try:
                BTWEngineOperationBusSerializer().update(instance.btw_engine_operation_bus,
                                                         btw_engine_operation_bus)
            except BTWEngineOperationBus.DoesNotExist:
                BTWEngineOperationBus.objects.create(btw=instance, **btw_engine_operation_bus)

        if 'btw_passenger_safety_bus' in validated_data:
            btw_passenger_safety_bus = validated_data.pop('btw_passenger_safety_bus')
            try:
                BTWPassengerSafetyBusSerializer().update(instance.btw_passenger_safety_bus,
                                                         btw_passenger_safety_bus)
            except BTWPassengerSafetyBus.DoesNotExist:
                BTWPassengerSafetyBus.objects.create(btw=instance, **btw_passenger_safety_bus)

        if 'btw_brakes_and_stopping_bus' in validated_data:
            btw_brakes_and_stopping_bus = validated_data.pop('btw_brakes_and_stopping_bus')
            try:
                BTWBrakesAndStoppingsBusSerializer().update(instance.btw_brakes_and_stopping_bus,
                                                            btw_brakes_and_stopping_bus)
            except BTWBrakesAndStoppingsBus.DoesNotExist:
                BTWBrakesAndStoppingsBus.objects.create(btw=instance, **btw_brakes_and_stopping_bus)

        if 'btw_eye_movement_and_mirror_bus' in validated_data:
            btw_eye_movement_and_mirror_bus = validated_data.pop('btw_eye_movement_and_mirror_bus')
            try:
                BTWEyeMovementAndMirrorBusSerializer().update(instance.btw_eye_movement_and_mirror_bus,
                                                              btw_eye_movement_and_mirror_bus)
            except BTWEyeMovementAndMirrorBus.DoesNotExist:
                BTWEyeMovementAndMirrorBus.objects.create(btw=instance, **btw_eye_movement_and_mirror_bus)

        if 'btw_recognizes_hazards_bus' in validated_data:
            btw_recognizes_hazards_bus = validated_data.pop('btw_recognizes_hazards_bus')
            try:
                BTWRecognizesHazardsBusSerializer().update(instance.btw_recognizes_hazards_bus,
                                                           btw_recognizes_hazards_bus)
            except BTWRecognizesHazardsBus.DoesNotExist:
                BTWRecognizesHazardsBus.objects.create(btw=instance, **btw_recognizes_hazards_bus)

        if 'btw_lights_and_signals_bus' in validated_data:

            btw_lights_and_signals_bus = validated_data.pop('btw_lights_and_signals_bus')
            try:
                BTWLightsAndSignalsBusSerializer().update(instance.btw_lights_and_signals_bus,
                                                          btw_lights_and_signals_bus)
            except BTWLightsAndSignalsBus.DoesNotExist:
                BTWLightsAndSignalsBus.objects.create(btw=instance, **btw_lights_and_signals_bus)

        if 'btw_steering_bus' in validated_data:
            btw_steering_bus = validated_data.pop('btw_steering_bus')
            try:
                BTWSteeringBusSerializer().update(instance.btw_steering_bus, btw_steering_bus)
            except BTWSteeringBus.DoesNotExist:
                BTWSteeringBus.objects.create(btw=instance, **btw_steering_bus)

        if 'btw_backing_bus' in validated_data:
            btw_backing_bus = validated_data.pop('btw_backing_bus')
            try:
                BTWBackingBusSerializer().update(instance.btw_backing_bus, btw_backing_bus)
            except BTWBackingBus.DoesNotExist:
                BTWBackingBus.objects.create(btw=instance, **btw_backing_bus)

        if 'btw_speed_bus' in validated_data:
            btw_speed_bus = validated_data.pop('btw_speed_bus')
            try:
                BTWSpeedBusSerializer().update(instance.btw_speed_bus, btw_speed_bus)
            except BTWSpeedBus.DoesNotExist:
                BTWSpeedBus.objects.create(btw=instance, **btw_speed_bus)

        if 'btw_intersections_bus' in validated_data:
            btw_intersections_bus = validated_data.pop('btw_intersections_bus')
            try:
                BTWIntersectionsBusSerializer().update(instance.btw_intersections_bus, btw_intersections_bus)
            except BTWIntersectionsBus.DoesNotExist:
                BTWIntersectionsBus.objects.create(btw=instance, **btw_intersections_bus)

        if 'btw_turning_bus' in validated_data:
            btw_turning_bus = validated_data.pop('btw_turning_bus')
            try:
                BTWTurningBusSerializer().update(instance.btw_turning_bus, btw_turning_bus)
            except BTWTurningBus.DoesNotExist:
                BTWTurningBus.objects.create(btw=instance, **btw_turning_bus)

        if 'btw_parking_bus' in validated_data:
            btw_parking_bus = validated_data.pop('btw_parking_bus')
            try:
                BTWParkingBusSerializer().update(instance.btw_parking_bus, btw_parking_bus)
            except BTWIntersectionsBus.DoesNotExist:
                BTWParkingBus.objects.create(btw=instance, **btw_parking_bus)

        if 'btw_hills_bus' in validated_data:
            btw_hills_bus = validated_data.pop('btw_hills_bus')
            try:
                BTWHillsBusSerializer().update(instance.btw_hills_bus, btw_hills_bus)
            except BTWHillsBus.DoesNotExist:
                BTWHillsBus.objects.create(btw=instance, **btw_hills_bus)

        if 'btw_passing_bus' in validated_data:
            btw_passing_bus = validated_data.pop('btw_passing_bus')
            try:
                BTWPassingBusSerializer().update(instance.btw_passing_bus, btw_passing_bus)
            except BTWPassingBus.DoesNotExist:
                BTWPassingBus.objects.create(btw=instance, **btw_passing_bus)

        if 'btw_railroad_crossing_bus' in validated_data:
            btw_railroad_crossing_bus = validated_data.pop('btw_railroad_crossing_bus')
            try:
                BTWRailroadCrossingBusSerializer().update(instance.btw_railroad_crossing_bus, btw_railroad_crossing_bus)
            except BTWRailroadCrossingBus.DoesNotExist:
                BTWRailroadCrossingBus.objects.create(btw=instance, **btw_railroad_crossing_bus)

        if 'btw_general_safety_bus' in validated_data:
            btw_general_safety_bus = validated_data.pop('btw_general_safety_bus')
            try:
                BTWGeneralSafetyAndDOTAdherenceBusSerializer().update(instance.btw_general_safety_bus,
                                                                      btw_general_safety_bus)
            except BTWGeneralSafetyAndDOTAdherenceBus.DoesNotExist:
                BTWGeneralSafetyAndDOTAdherenceBus.objects.create(btw=instance, **btw_general_safety_bus)

        if 'btw_internal_environment_bus' in validated_data:
            btw_internal_environment_bus = validated_data.pop('btw_internal_environment_bus')
            try:
                BTWInternalEnvironmentBusSerializer().update(instance.btw_internal_environment_bus,
                                                             btw_internal_environment_bus)
            except BTWInternalEnvironmentBus.DoesNotExist:
                BTWInternalEnvironmentBus.objects.create(btw=instance, **btw_internal_environment_bus)

        return super(BTWBusSerializer, self).update(instance, validated_data)
