from rest_framework import serializers

from safe_driver.api.v1.mixins import DBTableNameMixin
from safe_driver.image_functions import base64_to_image_content
from safe_driver.models import (
    SWPEmployeesInterview,
    SWPPowerEquipment,
    SWPJobSetup,
    SWPExpectTheUnexpected,
    SWPPushingAndPulling,
    SWPEndRangeMotion,
    SWPKeysLiftingAndLowering,
    SWPCuttingHazardsAndSharpObjects,
    SWPKeysToAvoidingSlipsAndFalls,
    SafeDriveSWP
)

from safe_driver.api.v1.serializers import (StudentTestSerializer, StudentDetailSerializer)


# from users.api.v1.serializers import UserStudentSerializer
class SWPEmployeesInterviewSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = SWPEmployeesInterview
        fields = '__all__'


class SWPPowerEquipmentSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = SWPPowerEquipment
        fields = '__all__'


class SWPJobSetupSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = SWPJobSetup
        fields = '__all__'


class SWPExpectTheUnexpectedSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = SWPExpectTheUnexpected
        fields = '__all__'


class SWPPushingAndPullingSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = SWPPushingAndPulling
        fields = '__all__'


class SWPEndRangeMotionSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = SWPEndRangeMotion
        fields = '__all__'


class SWPKeysLiftingAndLoweringSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = SWPKeysLiftingAndLowering
        fields = '__all__'


class SWPCuttingHazardsAndSharpObjectsSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = SWPCuttingHazardsAndSharpObjects
        fields = '__all__'


class SWPKeysToAvoidingSlipsAndFallsSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = SWPKeysToAvoidingSlipsAndFalls
        fields = '__all__'


class SafeDriveSWPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    test = StudentTestSerializer(read_only=True)
    employees_interview = SWPEmployeesInterviewSerializer(source='swpemployeesinterview')
    power_equipment = SWPPowerEquipmentSerializer(source='swppowerequipment')
    job_setup = SWPJobSetupSerializer(source='swpjobsetup')
    expect_the_unexpected = SWPExpectTheUnexpectedSerializer(source='swpexpecttheunexpected')
    pushing_and_pulling = SWPPushingAndPullingSerializer(source='swppushingandpulling')
    end_range_motion = SWPEndRangeMotionSerializer(source='swpendrangemotion')
    keys_lifting_and_lowering = SWPKeysLiftingAndLoweringSerializer(source='swpkeysliftingandlowering')
    cutting_hazards_and_sharp_objects = SWPCuttingHazardsAndSharpObjectsSerializer(
        source='swpcuttinghazardsandsharpobjects')
    eys_to_avoidings_lips_and_falls = SWPKeysToAvoidingSlipsAndFallsSerializer(
        source='swpkeystoavoidingslipsandfalls')

    driver_signature = serializers.CharField(required=False, write_only=True)
    evaluator_signature = serializers.CharField(required=False, write_only=True)
    company_rep_signature = serializers.CharField(required=False, write_only=True)

    def to_representation(self, instance):
        response = super(SafeDriveSWPSerializer, self).to_representation(instance)
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
        model = SafeDriveSWP
        fields = '__all__'

    def update(self, instance, validated_data):
        # print(validated_data)

        if 'driver_signature' in validated_data:
            driver_signature = validated_data.pop('driver_signature')
            try:
                image_content_file = base64_to_image_content(driver_signature)
                validated_data['driver_signature'] = image_content_file
            except Exception as e:
                print(e)

        if 'evaluator_signature' in validated_data:
            driver_signature = validated_data.pop('evaluator_signature')
            try:
                image_content_file = base64_to_image_content(driver_signature)
                validated_data['evaluator_signature'] = image_content_file
            except Exception as e:
                print(e)

        if 'company_rep_signature' in validated_data:
            driver_signature = validated_data.pop('company_rep_signature')
            try:
                image_content_file = base64_to_image_content(driver_signature)
                validated_data['company_rep_signature'] = image_content_file
            except Exception as e:
                print(e)

        if 'swpemployeesinterview' in validated_data:
            swpemployeesinterview = validated_data.pop('swpemployeesinterview')
            try:
                SWPEmployeesInterviewSerializer().update(instance.swpemployeesinterview, swpemployeesinterview)
            except SWPEmployeesInterview.DoesNotExist:
                SWPEmployeesInterview.objects.create(pas=instance, **swpemployeesinterview)

        if 'swppowerequipment' in validated_data:
            swppowerequipment = validated_data.pop('swppowerequipment')
            try:
                SWPEmployeesInterviewSerializer().update(instance.swppowerequipment, swppowerequipment)
            except SWPPowerEquipment.DoesNotExist:
                SWPPowerEquipment.objects.create(pas=instance, **swppowerequipment)

        if 'swpjobsetup' in validated_data:
            swpjobsetup = validated_data.pop('swpjobsetup')
            try:
                SWPEmployeesInterviewSerializer().update(instance.swpjobsetup, swpjobsetup)
            except SWPJobSetup.DoesNotExist:
                SWPJobSetup.objects.create(pas=instance, **swpjobsetup)

        if 'swpexpecttheunexpected' in validated_data:
            swpexpecttheunexpected = validated_data.pop('swpexpecttheunexpected')
            try:
                SWPEmployeesInterviewSerializer().update(instance.swpexpecttheunexpected, swpexpecttheunexpected)
            except SWPExpectTheUnexpected.DoesNotExist:
                SWPExpectTheUnexpected.objects.create(pas=instance, **swpexpecttheunexpected)

        if 'swppushingandpulling' in validated_data:
            swppushingandpulling = validated_data.pop('swppushingandpulling')
            try:
                SWPEmployeesInterviewSerializer().update(instance.swppushingandpulling, swppushingandpulling)
            except SWPPushingAndPulling.DoesNotExist:
                SWPPushingAndPulling.objects.create(pas=instance, **swppushingandpulling)

        if 'swpendrangemotion' in validated_data:
            swpendrangemotion = validated_data.pop('swpendrangemotion')
            try:
                SWPEmployeesInterviewSerializer().update(instance.swpendrangemotion, swpendrangemotion)
            except SWPEndRangeMotion.DoesNotExist:
                SWPEndRangeMotion.objects.create(pas=instance, **swpendrangemotion)

        if 'swpkeysliftingandlowering' in validated_data:
            swpkeysliftingandlowering = validated_data.pop('swpkeysliftingandlowering')
            try:
                SWPEmployeesInterviewSerializer().update(instance.swpkeysliftingandlowering, swpkeysliftingandlowering)
            except SWPKeysLiftingAndLowering.DoesNotExist:
                SWPKeysLiftingAndLowering.objects.create(pas=instance, **swpkeysliftingandlowering)

        if 'swpcuttinghazardsandsharpobjects' in validated_data:
            swpcuttinghazardsandsharpobjects = validated_data.pop('swpcuttinghazardsandsharpobjects')
            try:
                SWPCuttingHazardsAndSharpObjectsSerializer().update(instance.swpcuttinghazardsandsharpobjects,
                                                                    swpcuttinghazardsandsharpobjects)
            except SWPCuttingHazardsAndSharpObjects.DoesNotExist:
                SWPCuttingHazardsAndSharpObjects.objects.create(pas=instance, **swpcuttinghazardsandsharpobjects)

        if 'swpkeystoavoidingslipsandfalls' in validated_data:
            swpkeystoavoidingslipsandfalls = validated_data.pop('swpkeystoavoidingslipsandfalls')
            try:
                SWPKeysToAvoidingSlipsAndFallsSerializer().update(instance.swpkeystoavoidingslipsandfalls,
                                                                  swpkeystoavoidingslipsandfalls)
            except SWPKeysToAvoidingSlipsAndFalls.DoesNotExist:
                SWPKeysToAvoidingSlipsAndFalls.objects.create(pas=instance, **swpkeystoavoidingslipsandfalls)

        return super(SafeDriveSWPSerializer, self).update(instance, validated_data)
