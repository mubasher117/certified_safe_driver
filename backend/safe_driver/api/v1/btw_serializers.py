from rest_framework import serializers
from users.api.v1.serializers import UserStudentSerializer
from safe_driver.models import (
    BTWCabSafety, BTWStartEngine, BTWEngineOperation, BTWClutchAndTransmission, BTWCoupling, BTWUncoupling,
    BTWBrakesAndStoppings, BTWEyeMovementAndMirror, BTWRecognizesHazards, BTWLightsAndSignals, BTWSteering, BTWBacking,
    BTWSpeed, BTWIntersections, BTWTurning, BTWParking, BTWMultipleTrailers,
    BTWHills, BTWPassing, BTWGeneralSafetyAndDOTAdherence, SafeDriveBTW
)


class BTWCabSafetySerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWCabSafety
        fields = '__all__'


class BTWStartEngineSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWStartEngine
        fields = '__all__'


class BTWEngineOperationSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWEngineOperation
        fields = '__all__'


class BTWClutchAndTransmissionSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWClutchAndTransmission
        fields = '__all__'


class BTWCouplingSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWCoupling
        fields = '__all__'


class BTWUncouplingSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWUncoupling
        fields = '__all__'


class BTWBrakesAndStoppingsSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWBrakesAndStoppings
        fields = '__all__'


class BTWEyeMovementAndMirrorSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWEyeMovementAndMirror
        fields = '__all__'


class BTWRecognizesHazardsSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWRecognizesHazards
        fields = '__all__'


class BTWLightsAndSignalsSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWLightsAndSignals
        fields = '__all__'


class BTWSteeringSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWSteering
        fields = '__all__'


class BTWBackingSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWBacking
        fields = '__all__'


class BTWSpeedSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWSpeed
        fields = '__all__'


class BTWIntersectionsSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWIntersections
        fields = '__all__'


class BTWTurningSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWTurning
        fields = '__all__'


class BTWParkingSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWParking
        fields = '__all__'


class BTWMultipleTrailersSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWMultipleTrailers
        fields = '__all__'


class BTWHillsSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWHills
        fields = '__all__'


class BTWPassingSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWPassing
        fields = '__all__'


class BTWGeneralSafetyAndDOTAdherenceSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = BTWGeneralSafetyAndDOTAdherence
        fields = '__all__'


class SafeDriveBTWSerializer(serializers.ModelSerializer):
    student = UserStudentSerializer(read_only=True)
    cab_safety = BTWCabSafetySerializer(source='btwcabsafety')
    start_engine = BTWStartEngineSerializer(source='btwstartengine')
    engine_operation = BTWEngineOperationSerializer(source='btwengineoperation')
    clutch_and_transmission = BTWClutchAndTransmissionSerializer(source='btwclutchandtransmission')
    coupling = BTWCouplingSerializer(source='btwcoupling', )
    uncoupling = BTWUncouplingSerializer(source='btwuncoupling')
    brakes_and_stopping = BTWBrakesAndStoppingsSerializer(source='btwbrakesandstoppings')
    eye_movement_and_mirror = BTWEyeMovementAndMirrorSerializer(source='btweyemovementandmirror')
    recognizes_hazards = BTWRecognizesHazardsSerializer(source='btwrecognizeshazards')
    lights_and_signals = BTWLightsAndSignalsSerializer(source='btwlightsandsignals')
    steering = BTWSteeringSerializer(source='btwsteering')
    backing = BTWBackingSerializer(source='btwbacking')
    speed = BTWSpeedSerializer(source='btwspeed')
    intersections = BTWIntersectionsSerializer(source='btwintersections')
    turning = BTWTurningSerializer(source='btwturning', )
    parking = BTWParkingSerializer(source='btwparking', )
    multiple_trailers = BTWMultipleTrailersSerializer(source='btwmultipletrailers', )
    hills = BTWHillsSerializer(source='btwhills', )
    passing = BTWPassingSerializer(source='btwpassing', )
    general_safety_and_dot_adherence = BTWGeneralSafetyAndDOTAdherenceSerializer(
        source='btwgeneralsafetyanddotadherence')

    class Meta:
        model = SafeDriveBTW
        fields = '__all__'

    def update(self, instance, validated_data):
        # print(validated_data)
        if 'btwcabsafety' in validated_data:
            btwcabsafety = validated_data.pop('btwcabsafety')
            try:
                BTWCabSafetySerializer().update(instance.btwcabsafety,
                                                btwcabsafety)
            except BTWCabSafety.DoesNotExist:
                BTWCabSafety.objects.create(btw=instance, **btwcabsafety)

        if 'btwstartengine' in validated_data:
            btwstartengine = validated_data.pop('btwstartengine')
            try:
                BTWStartEngineSerializer().update(instance.btwstartengine, btwstartengine)
            except BTWStartEngine.DoesNotExist:
                BTWStartEngine.objects.create(btw=instance, **btwstartengine)

        if 'btwengineoperation' in validated_data:
            btwengineoperation = validated_data.pop('btwengineoperation')
            try:
                BTWEngineOperationSerializer().update(instance.btwengineoperation, btwengineoperation)
            except BTWEngineOperation.DoesNotExist:
                BTWEngineOperation.objects.create(btw=instance, **btwengineoperation)

        if 'btwclutchandtransmission' in validated_data:
            btwclutchandtransmission = validated_data.pop('btwclutchandtransmission')
            try:
                BTWClutchAndTransmissionSerializer().update(instance.btwclutchandtransmission,
                                                            btwclutchandtransmission)
            except BTWClutchAndTransmission.DoesNotExist:
                BTWClutchAndTransmission.objects.create(btw=instance, **btwclutchandtransmission)

        if 'btwcoupling' in validated_data:
            btwcoupling = validated_data.pop('btwcoupling')
            print(btwcoupling)
            try:
                BTWCouplingSerializer().update(instance.btwcoupling, btwcoupling)
            except BTWCoupling.DoesNotExist:
                BTWCoupling.objects.create(btw=instance, **btwcoupling)

        if 'btwuncoupling' in validated_data:
            btwuncoupling = validated_data.pop('btwuncoupling')
            try:
                BTWUncouplingSerializer().update(instance.btwuncoupling, btwuncoupling)
            except BTWUncoupling.DoesNotExist:
                BTWUncoupling.objects.create(btw=instance, **btwuncoupling)

        if 'btwbrakesandstoppings' in validated_data:
            btwbrakesandstoppings = validated_data.pop('btwbrakesandstoppings')
            try:
                BTWBrakesAndStoppingsSerializer().update(instance.btwbrakesandstoppings,
                                                         btwbrakesandstoppings)
            except BTWBrakesAndStoppings.DoesNotExist:
                BTWBrakesAndStoppings.objects.create(btw=instance, **btwbrakesandstoppings)

        if 'btweyemovementandmirror' in validated_data:
            btweyemovementandmirror = validated_data.pop('btweyemovementandmirror')
            try:
                BTWEyeMovementAndMirrorSerializer().update(instance.btweyemovementandmirror,
                                                           btweyemovementandmirror)
            except BTWEyeMovementAndMirror.DoesNotExist:
                BTWEyeMovementAndMirror.objects.create(btw=instance, **btweyemovementandmirror)

        if 'btwrecognizeshazards' in validated_data:
            btwrecognizeshazards = validated_data.pop('btwrecognizeshazards')
            try:
                BTWRecognizesHazardsSerializer().update(instance.btwrecognizeshazards,
                                                        btwrecognizeshazards)
            except BTWRecognizesHazards.DoesNotExist:
                BTWRecognizesHazards.objects.create(btw=instance, **btwrecognizeshazards)

        if 'btwlightsandsignals' in validated_data:

            btwlightsandsignals = validated_data.pop('btwlightsandsignals')
            try:
                BTWLightsAndSignalsSerializer().update(instance.btwlightsandsignals,
                                                       btwlightsandsignals)
            except BTWLightsAndSignals.DoesNotExist:
                BTWLightsAndSignals.objects.create(btw=instance, **btwlightsandsignals)

        if 'btwsteering' in validated_data:
            btwsteering = validated_data.pop('btwsteering')
            try:
                BTWSteeringSerializer().update(instance.btwsteering, btwsteering)
            except BTWSteering.DoesNotExist:
                BTWSteering.objects.create(btw=instance, **btwsteering)

        if 'btwbacking' in validated_data:
            btwbacking = validated_data.pop('btwbacking')
            try:
                BTWBackingSerializer().update(instance.btwbacking, btwbacking)
            except BTWBacking.DoesNotExist:
                BTWBacking.objects.create(btw=instance, **btwbacking)

        if 'btwspeed' in validated_data:
            btwspeed = validated_data.pop('btwspeed')
            try:
                BTWSpeedSerializer().update(instance.btwspeed, btwspeed)
            except BTWSpeed.DoesNotExist:
                BTWSpeed.objects.create(btw=instance, **btwspeed)

        if 'btwintersections' in validated_data:
            btwintersections = validated_data.pop('btwintersections')
            try:
                BTWIntersectionsSerializer().update(instance.btwintersections, btwintersections)
            except BTWIntersections.DoesNotExist:
                BTWIntersections.objects.create(btw=instance, **btwintersections)

        if 'btwturning' in validated_data:
            btwturning = validated_data.pop('btwturning')
            try:
                BTWTurningSerializer().update(instance.btwturning, btwturning)
            except BTWTurning.DoesNotExist:
                BTWTurning.objects.create(btw=instance, **btwturning)

        if 'btwparking' in validated_data:
            btwparking = validated_data.pop('btwparking')
            try:
                BTWParkingSerializer().update(instance.btwparking, btwparking)
            except BTWParking.DoesNotExist:
                BTWParking.objects.create(btw=instance, **btwparking)

        if 'btwmultipletrailers' in validated_data:
            btwmultipletrailers = validated_data.pop('btwmultipletrailers')
            try:
                BTWMultipleTrailersSerializer().update(instance.btwmultipletrailers,
                                                       btwmultipletrailers)
            except BTWMultipleTrailers.DoesNotExist:
                BTWMultipleTrailers.objects.create(btw=instance, **btwmultipletrailers)

        if 'btwhills' in validated_data:
            btwhills = validated_data.pop('btwhills')
            try:
                BTWHillsSerializer().update(instance.btwhills, btwhills)
            except BTWHills.DoesNotExist:
                BTWHills.objects.create(btw=instance, **btwhills)

        if 'btwpassing' in validated_data:
            btwpassing = validated_data.pop('btwpassing')
            try:
                BTWPassingSerializer().update(instance.btwpassing, btwpassing)
            except BTWPassing.DoesNotExist:
                BTWPassing.objects.create(btw=instance, **btwpassing)

        if 'btwgeneralsafetyanddotadherence' in validated_data:
            btwgeneralsafetyanddotadherence = validated_data.pop('btwgeneralsafetyanddotadherence')
            try:
                BTWGeneralSafetyAndDOTAdherenceSerializer().update(
                    instance.btwgeneralsafetyanddotadherence, btwgeneralsafetyanddotadherence)
            except BTWGeneralSafetyAndDOTAdherence.DoesNotExist:
                BTWGeneralSafetyAndDOTAdherence.objects.create(btw=instance, **btwgeneralsafetyanddotadherence)

        return super(SafeDriveBTWSerializer, self).update(instance, validated_data)
