from rest_framework import serializers

from safe_driver.api.v1.mixins import DBTableNameMixin
from safe_driver.api.v1.serializers import StudentTestSerializer, StudentDetailSerializer
from safe_driver.image_functions import base64_to_image_content
from safe_driver.models import (
    VehicleRoadTest,
    VRTPreTrip, VRTCoupling, VRTUncoupling, VRTEngineOperations, VRTStartEngine, VRTUseClutch,
    VRTUseOfTransmission, VRTUseOfBrakes, VRTBacking, VRTParking, VRTDrivingHabits, VRTPostTrip
)
from users.api.v1.serializers import UserStudentSerializer


class VRTPreTripSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)

    class Meta:
        model = VRTPreTrip
        fields = '__all__'


class VRTCouplingSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)

    class Meta:
        model = VRTCoupling
        fields = '__all__'


class VRTUncouplingSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)

    class Meta:
        model = VRTUncoupling
        fields = '__all__'


class VRTEngineOperationsSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)

    class Meta:
        model = VRTEngineOperations
        fields = '__all__'


class VRTStartEngineSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)

    class Meta:
        model = VRTStartEngine
        fields = '__all__'


class VRTUseClutchSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)

    class Meta:
        model = VRTUseClutch
        fields = '__all__'


class VRTUseOfTransmissionSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)

    class Meta:
        model = VRTUseOfTransmission
        fields = '__all__'


class VRTUseOfBrakesSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)

    class Meta:
        model = VRTUseOfBrakes
        fields = '__all__'


class VRTBackingSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)

    class Meta:
        model = VRTBacking
        fields = '__all__'


class VRTParkingSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)

    class Meta:
        model = VRTParking
        fields = '__all__'


class VRTDrivingHabitsSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)

    class Meta:
        model = VRTDrivingHabits
        fields = '__all__'


class VRTPostTripSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)

    class Meta:
        model = VRTPostTrip
        fields = '__all__'


class SafeDriveVRTSerializer(DBTableNameMixin, serializers.ModelSerializer):
    # student = UserStudentSerializer(read_only=True)
    points = serializers.SerializerMethodField(read_only=True, method_name='get_points')
    test = StudentTestSerializer(read_only=True)
    pre_trip = VRTPreTripSerializer(source='vrtpretrip')
    coupling = VRTCouplingSerializer(source='vrtcoupling')
    uncoupling = VRTUncouplingSerializer(source='vrtuncoupling')
    engine_operations = VRTEngineOperationsSerializer(source='vrtengineoperations')
    start_engine = VRTStartEngineSerializer(source='vrtstartengine')
    use_of_clutch = VRTUseClutchSerializer(source='vrtuseclutch')
    use_of_transmission = VRTUseOfTransmissionSerializer(source='vrtuseoftransmission')
    use_of_brakes = VRTUseOfBrakesSerializer(source='vrtuseofbrakes')
    backing = VRTBackingSerializer(source='vrtbacking')
    parking = VRTParkingSerializer(source='vrtparking')
    driving_habits = VRTDrivingHabitsSerializer(source='vrtdrivinghabits')
    post_trip = VRTPostTripSerializer(source='vrtposttrip')

    driver_signature = serializers.CharField(required=False, write_only=True)
    evaluator_signature = serializers.CharField(required=False, write_only=True)
    company_rep_signature = serializers.CharField(required=False, write_only=True)

    def get_points(self, instance):
        model_fields = instance._meta.get_fields()
        total_possible_points = 0
        total_received_points = 0
        count = 0
        for field in model_fields:
            related_model = instance._meta.get_field(field.name).related_model
            if related_model:
                try:
                    ppoints = getattr(instance, field.name, 'possible_points')
                    total_possible_points += ppoints.possible_points
                    count += 1
                except Exception as e:
                    pass

                try:
                    rcpoints = getattr(instance, field.name, 'points_received')
                    total_received_points += rcpoints.points_received
                except Exception as e:
                    pass

        # print(count)
        percentage = 0
        if total_possible_points > total_received_points:
            percentage = '{:.2f}'.format((100 / total_possible_points) * total_received_points)

        data = {
            'total_possible_points': total_possible_points,
            'total_received_points': total_received_points,
            'percentage': percentage
        }
        return data

    def to_representation(self, instance):
        response = super(self.__class__, self).to_representation(instance)
        response['student'] = StudentDetailSerializer(instance.test.student).data
        if instance.driver_signature:
            response['driver_signature'] = instance.driver_signature.url
        else:
            response['driver_signature'] = None
        if instance.evaluator_signature:
            response['evaluator_signature'] = instance.evaluator_signature.url
        else:
            response['evaluator_signature'] = None

        if instance.company_rep_signature:
            response['company_rep_signature'] = instance.company_rep_signature.url
        else:
            response['company_rep_signature'] = None

        return response

    class Meta:
        model = VehicleRoadTest
        fields = '__all__'

    def update(self, instance, validated_data):
        # print(validated_data)

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

        if 'vrtpretrip' in validated_data:
            vrtpretrip = validated_data.pop('vrtpretrip')
            try:
                instance.vrtpretrip
                VRTPreTripSerializer().update(instance.vrtpretrip, vrtpretrip)
            except VRTPreTrip.DoesNotExist:
                VRTPreTrip.objects.create(vrt=instance, **vrtpretrip)

        if 'vrtcoupling' in validated_data:
            vrtcoupling = validated_data.pop('vrtcoupling')
            try:
                instance.vrtcoupling
                VRTPreTripSerializer().update(instance.vrtcoupling, vrtcoupling)
            except VRTCoupling.DoesNotExist:
                VRTCoupling.objects.create(vrt=instance, **vrtcoupling)

        if 'vrtuncoupling' in validated_data:
            vrtuncoupling = validated_data.pop('vrtuncoupling')
            try:
                instance.vrtuncoupling
                VRTUncouplingSerializer().update(instance.vrtuncoupling, vrtuncoupling)
            except VRTUncoupling.DoesNotExist:
                VRTUncoupling.objects.create(vrt=instance, **vrtuncoupling)

        if 'vrtengineoperations' in validated_data:
            vrtengineoperations = validated_data.pop('vrtengineoperations')
            try:
                VRTEngineOperationsSerializer().update(instance.vrtengineoperations,
                                                       vrtengineoperations)
            except VRTEngineOperations.DoesNotExist:
                VRTEngineOperations.objects.create(vrt=instance, **vrtengineoperations)

        if 'vrtstartengine' in validated_data:
            vrtstartengine = validated_data.pop('vrtstartengine')
            try:
                instance.vrtstartengine
                VRTStartEngineSerializer().update(instance.vrtstartengine, vrtstartengine)
            except VRTStartEngine.DoesNotExist:
                VRTStartEngine.objects.create(vrt=instance, **vrtstartengine)

        if 'vrtuseclutch' in validated_data:
            vrtuseclutch = validated_data.pop('vrtuseclutch')
            try:
                VRTUseClutchSerializer().update(instance.vrtuseclutch, vrtuseclutch)
            except VRTUseClutch.DoesNotExist:
                VRTUseClutch.objects.create(vrt=instance, **vrtuseclutch)

        if 'vrtuseoftransmission' in validated_data:
            vrtuseoftransmission = validated_data.pop('vrtuseoftransmission')
            try:
                VRTUseOfTransmissionSerializer().update(instance.vrtuseoftransmission, vrtuseoftransmission)
            except VRTUseOfTransmission.DoesNotExist:
                VRTUseOfTransmission.objects.create(vrt=instance, **vrtuseoftransmission)

        if 'vrtuseofbrakes' in validated_data:
            vrtuseofbrakes = validated_data.pop('vrtuseofbrakes')
            try:
                VRTUseOfBrakesSerializer().update(instance.vrtuseofbrakes, vrtuseofbrakes)
            except VRTUseOfBrakes.DoesNotExist:
                VRTUseOfBrakes.objects.create(vrt=instance, **vrtuseofbrakes)

        if 'vrtbacking' in validated_data:
            vrtbacking = validated_data.pop('vrtbacking')
            try:
                VRTBackingSerializer().update(instance.vrtbacking, vrtbacking)
            except VRTBacking.DoesNotExist:
                VRTBacking.objects.create(vrt=instance, **vrtbacking)

        if 'vrtparking' in validated_data:

            vrtparking = validated_data.pop('vrtparking')
            try:
                VRTParkingSerializer().update(instance.vrtparking, vrtparking)
            except VRTParking.DoesNotExist:
                VRTParking.objects.create(vrt=instance, **vrtparking)

        if 'vrtdrivinghabits' in validated_data:
            vrtdrivinghabits = validated_data.pop('vrtdrivinghabits')
            try:
                VRTDrivingHabitsSerializer().update(instance.vrtdrivinghabits, vrtdrivinghabits)
            except VRTDrivingHabits.DoesNotExist:
                VRTDrivingHabits.objects.create(vrt=instance, **vrtdrivinghabits)

        if 'vrtposttrip' in validated_data:
            vrtposttrip = validated_data.pop('vrtposttrip')
            try:
                VRTPostTripSerializer().update(instance.vrtposttrip, vrtposttrip)
            except VRTPostTrip.DoesNotExist:
                VRTPostTrip.objects.create(vrt=instance, **vrtposttrip)

        return super(SafeDriveVRTSerializer, self).update(instance, validated_data)
