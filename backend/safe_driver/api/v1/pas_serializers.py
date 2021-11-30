from django.contrib.auth import get_user_model
from rest_framework import serializers

from safe_driver.api.v1.serializers import StudentTestSerializer, StudentInfoSerializer, StudentDetailUpdateSerializer, \
    StudentDetailSerializer

from safe_driver.models import (
    PASBacking, PASBrakesAndStoppings, PASCabSafety, PASEngineOperation, PASEyeMovementAndMirror,
    PASGeneralSafetyAndDOTAdherence, PASHills, PASIntersections, PASLightsAndSignals, PASParking, PASPassengerSafety,
    PASPassing, PASRailroadCrossing, PASRecognizesHazards, PASSpeed, PASStartEngine, PASSteering, PASTurning,
    PassengerVehicles,
)

User = get_user_model()


class PASCabSafetySerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASCabSafety
        fields = '__all__'


class PASStartEngineSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASStartEngine
        fields = '__all__'


class PASEngineOperationSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASEngineOperation
        fields = '__all__'


class PASBrakesAndStoppingsSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASBrakesAndStoppings
        fields = '__all__'


class PASPassengerSafetySerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASPassengerSafety
        fields = '__all__'


class PASEyeMovementAndMirrorSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASEyeMovementAndMirror
        fields = '__all__'


class PASRecognizesHazardsSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASRecognizesHazards
        fields = '__all__'


class PASLightsAndSignalsSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASLightsAndSignals
        fields = '__all__'


class PASSteeringSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASSteering
        fields = '__all__'


class PASBackingSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASBacking
        fields = '__all__'


class PASSpeedSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASSpeed
        fields = '__all__'


class PASIntersectionsSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASIntersections
        fields = '__all__'


class PASTurningSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASTurning
        fields = '__all__'


class PASParkingSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASParking
        fields = '__all__'


class PASHillsSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASHills
        fields = '__all__'


class PASPassingSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASPassing
        fields = '__all__'


class PASRailroadCrossingSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASRailroadCrossing
        fields = '__all__'


class PASGeneralSafetyAndDOTAdherenceSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PASGeneralSafetyAndDOTAdherence
        fields = '__all__'


class PassengerVehiclesSerializer(serializers.ModelSerializer):
    # student = UserStudentSerializer(read_only=True)
    test = StudentTestSerializer(read_only=True)
    cab_safety = PASCabSafetySerializer(source='pascabsafety')
    start_engine = PASStartEngineSerializer(source='passtartengine')
    engine_operation = PASEngineOperationSerializer(source='pasengineoperation')
    brakes_and_stopping = PASBrakesAndStoppingsSerializer(source='pasbrakesandstoppings')
    passenger_safety = PASPassengerSafetySerializer(source='paspassengersafety')
    eye_movement_and_mirror = PASEyeMovementAndMirrorSerializer(source='paseyemovementandmirror')
    recognizes_hazards = PASRecognizesHazardsSerializer(source='pasrecognizeshazards')
    lights_and_signals = PASLightsAndSignalsSerializer(source='paslightsandsignals')
    steering = PASSteeringSerializer(source='passteering')
    backing = PASBackingSerializer(source='pasbacking')
    speed = PASSpeedSerializer(source='passpeed')
    intersections = PASIntersectionsSerializer(source='pasintersections')
    turning = PASTurningSerializer(source='pasturning', )
    parking = PASParkingSerializer(source='pasparking', )
    hills = PASHillsSerializer(source='pashills', )
    passing = PASPassingSerializer(source='paspassing', )
    rail_road_crossing = PASRailroadCrossingSerializer(source='pasrailroadcrossing')
    general_safety_and_dot_adherence = PASGeneralSafetyAndDOTAdherenceSerializer(
        source='pasgeneralsafetyanddotadherence')

    driver_signature = serializers.CharField(required=False, write_only=True)
    evaluator_signature = serializers.CharField(required=False, write_only=True)
    company_rep_signature = serializers.CharField(required=False, write_only=True)

    def to_representation(self, instance):
        response = super(PassengerVehiclesSerializer, self).to_representation(instance)
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
        model = PassengerVehicles
        fields = '__all__'
        # depth = 4

    def update(self, instance, validated_data):
        # print(validated_data)
        if 'pascabsafety' in validated_data:
            pascabsafety = validated_data.pop('pascabsafety')
            try:
                PASCabSafetySerializer().update(instance.pascabsafety, pascabsafety)
            except PASCabSafety.DoesNotExist:
                PASCabSafety.objects.create(pas=instance, **pascabsafety)

        if 'passtartengine' in validated_data:
            passtartengine = validated_data.pop('passtartengine')
            try:
                PASStartEngineSerializer().update(instance.passtartengine, passtartengine)
            except PASStartEngine.DoesNotExist:
                PASStartEngine.objects.create(pas=instance, **passtartengine)

        if 'pasengineoperation' in validated_data:
            pasengineoperation = validated_data.pop('pasengineoperation')
            try:
                PASEngineOperationSerializer().update(instance.pasengineoperation, pasengineoperation)
            except PASEngineOperation.DoesNotExist:
                PASEngineOperation.objects.create(pas=instance, **pasengineoperation)

        if 'pasbrakesandstoppings' in validated_data:
            pasbrakesandstoppings = validated_data.pop('pasbrakesandstoppings')
            try:
                PASBrakesAndStoppingsSerializer().update(instance.pasbrakesandstoppings,
                                                         pasbrakesandstoppings)
            except PASBrakesAndStoppings.DoesNotExist:
                PASBrakesAndStoppings.objects.create(pas=instance, **pasbrakesandstoppings)

        if 'paspassengersafety' in validated_data:
            paspassengersafety = validated_data.pop('paspassengersafety')
            try:
                PASPassengerSafetySerializer().update(instance.paspassengersafety,
                                                      paspassengersafety)
            except PASPassengerSafety.DoesNotExist:
                PASPassengerSafety.objects.create(pas=instance, **paspassengersafety)

        if 'paseyemovementandmirror' in validated_data:
            paseyemovementandmirror = validated_data.pop('paseyemovementandmirror')
            try:
                PASEyeMovementAndMirrorSerializer().update(instance.paseyemovementandmirror,
                                                           paseyemovementandmirror)
            except PASEyeMovementAndMirror.DoesNotExist:
                PASEyeMovementAndMirror.objects.create(pas=instance, **paseyemovementandmirror)

        if 'pasrecognizeshazards' in validated_data:
            pasrecognizeshazards = validated_data.pop('pasrecognizeshazards')
            try:
                PASRecognizesHazardsSerializer().update(instance.pasrecognizeshazards,
                                                        pasrecognizeshazards)
            except PASRecognizesHazards.DoesNotExist:
                PASRecognizesHazards.objects.create(pas=instance, **pasrecognizeshazards)

        if 'paslightsandsignals' in validated_data:

            paslightsandsignals = validated_data.pop('paslightsandsignals')
            try:
                PASLightsAndSignalsSerializer().update(instance.paslightsandsignals,
                                                       paslightsandsignals)
            except PASLightsAndSignals.DoesNotExist:
                PASLightsAndSignals.objects.create(pas=instance, **paslightsandsignals)

        if 'passteering' in validated_data:
            passteering = validated_data.pop('passteering')
            try:
                PASSteeringSerializer().update(instance.passteering, passteering)
            except PASSteering.DoesNotExist:
                PASSteering.objects.create(pas=instance, **passteering)

        if 'pasbacking' in validated_data:
            pasbacking = validated_data.pop('pasbacking')
            try:
                PASBackingSerializer().update(instance.pasbacking, pasbacking)
            except PASBacking.DoesNotExist:
                PASBacking.objects.create(pas=instance, **pasbacking)

        if 'passpeed' in validated_data:
            passpeed = validated_data.pop('passpeed')
            try:
                PASSpeedSerializer().update(instance.passpeed, passpeed)
            except PASSpeed.DoesNotExist:
                PASSpeed.objects.create(pas=instance, **passpeed)

        if 'pasintersections' in validated_data:
            pasintersections = validated_data.pop('pasintersections')
            try:
                PASIntersectionsSerializer().update(instance.pasintersections, pasintersections)
            except PASIntersections.DoesNotExist:
                PASIntersections.objects.create(pas=instance, **pasintersections)

        if 'pasturning' in validated_data:
            pasturning = validated_data.pop('pasturning')
            try:
                PASTurningSerializer().update(instance.pasturning, pasturning)
            except PASTurning.DoesNotExist:
                PASTurning.objects.create(pas=instance, **pasturning)

        if 'pasparking' in validated_data:
            pasparking = validated_data.pop('pasparking')
            try:
                PASParkingSerializer().update(instance.pasparking, pasparking)
            except PASParking.DoesNotExist:
                PASParking.objects.create(pas=instance, **pasparking)

        if 'pashills' in validated_data:
            pashills = validated_data.pop('pashills')
            try:
                PASHillsSerializer().update(instance.pashills, pashills)
            except PASHills.DoesNotExist:
                PASHills.objects.create(pas=instance, **pashills)

        if 'paspassing' in validated_data:
            paspassing = validated_data.pop('paspassing')
            try:
                PASPassingSerializer().update(instance.paspassing, paspassing)
            except PASPassing.DoesNotExist:
                PASPassing.objects.create(pas=instance, **paspassing)

        if 'pasrailroadcrossing' in validated_data:
            pasrailroadcrossing = validated_data.pop('pasrailroadcrossing')
            try:
                PASRailroadCrossingSerializer().update(instance.pasrailroadcrossing, pasrailroadcrossing)
            except PASRailroadCrossing.DoesNotExist:
                PASRailroadCrossing.objects.create(pas=instance, **pasrailroadcrossing)

        if 'pasgeneralsafetyanddotadherence' in validated_data:
            pasgeneralsafetyanddotadherence = validated_data.pop('pasgeneralsafetyanddotadherence')
            try:
                PASGeneralSafetyAndDOTAdherenceSerializer().update(
                    instance.pasgeneralsafetyanddotadherence, pasgeneralsafetyanddotadherence)
            except PASGeneralSafetyAndDOTAdherence.DoesNotExist:
                PASGeneralSafetyAndDOTAdherence.objects.create(pas=instance, **pasgeneralsafetyanddotadherence)

        return super(PassengerVehiclesSerializer, self).update(instance, validated_data)
