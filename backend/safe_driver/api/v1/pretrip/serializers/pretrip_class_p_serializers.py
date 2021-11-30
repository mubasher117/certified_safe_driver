from rest_framework import serializers
from safe_driver.api.v1.mixins import SerializerFiledAttributesMixin, DBTableNameMixin
from safe_driver.api.v1.serializers import StudentTestSerializer, StudentInfoSerializer, StudentDetailSerializer
from safe_driver.image_functions import base64_to_image_content
from safe_driver.models.pretrips_class_p import *
from users.api.v1.serializers import UserStudentSerializer


class PreTripInsideCabSerializerClassP(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripInsideCabClassP
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_p': {
                'read_only': True
            }
        }


class PreTripCOALSSerializerClassP(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripCOALSClassP
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_p': {
                'read_only': True
            }
        }


class PreTripEngineCompartmentSerializerClassP(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripEngineCompartmentClassP
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_p': {
                'read_only': True
            }
        }


class PreTripVehicleFrontSerializerClassP(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripVehicleFrontClassP
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_p': {
                'read_only': True
            }
        }


class PreTripBothSidesVehicleSerializerClassP(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripBothSidesVehiclesClassP
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_p': {
                'read_only': True
            }
        }


class PreTripHandyCapSerializerClassP(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripHandyCapClassP
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_p': {
                'read_only': True
            }
        }


class PreTripRearOfVehicleSerializerClassP(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripRearOfVehicleClassP
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_p': {
                'read_only': True
            }
        }


class PreTripPostTripSerializerClassP(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripPostTripClassP
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_p': {
                'read_only': True
            }
        }


class PreTripCargoAreaClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripCargoAreaClassP
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_p': {
                'read_only': True
            }
        }


class PreTripRampClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripRampClassP
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_p': {
                'read_only': True
            }
        }


class PreTripInteriorOperationClassPSerializer(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripInteriorOperationClassP
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_p': {
                'read_only': True
            }
        }


class PreTripSerializerClassP(DBTableNameMixin, serializers.ModelSerializer):
    test = StudentTestSerializer(read_only=True)
    inside_cab = PreTripInsideCabSerializerClassP(source='pretrip_insidecab_class_p', required=False)
    coals = PreTripCOALSSerializerClassP(source='pretrip_coals_class_p', required=False)
    engine_compartment = PreTripEngineCompartmentSerializerClassP(source='pretrip_engine_compartment_class_p',
                                                                  required=False)
    vehicle_front = PreTripVehicleFrontSerializerClassP(source='pretrip_vehicle_front_class_p', required=False)
    both_sides_vehicle = PreTripBothSidesVehicleSerializerClassP(source='pretrip_both_sides_vehicle_class_p',
                                                                 required=False)
    handy_cap = PreTripHandyCapSerializerClassP(
        source='pretrip_handycap_class_p', required=False)
    rear_of_vehicle = PreTripRearOfVehicleSerializerClassP(source='pretrip_rear_of_vehicle_class_p',
                                                           required=False)

    cargo_area = PreTripCargoAreaClassPSerializer(source='pretrip_cargo_area_class_p', required=False)
    ramp = PreTripRampClassPSerializer(source='pretrip_ramp_class_p', required=False)
    interior_operations = PreTripInteriorOperationClassPSerializer(source='pretrip_interior_operation_class_p',
                                                                   required=False)

    post_trip = PreTripPostTripSerializerClassP(source='pretrip_posttrip_class_p', required=False)
    # student = StudentDetailSerializer(source='test__student_tests')
    driver_signature = serializers.CharField(required=False, write_only=True)
    evaluator_signature = serializers.CharField(required=False, write_only=True)
    company_rep_signature = serializers.CharField(required=False, write_only=True)

    def to_representation(self, instance):
        res = super(self.__class__, self).to_representation(instance)
        res['student'] = StudentDetailSerializer(instance.test.student).data
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
        return res

    class Meta:
        model = PreTripClassP
        fields = '__all__'
        # exclude = ('student', )

    def update(self, instance, validated_data):
        # request = self.context.get("request")

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

        if "pretrip_insidecab_class_p" in validated_data:
            inside_cab = validated_data.pop('pretrip_insidecab_class_p')
            inside_cab_serializer = PreTripInsideCabSerializerClassP()
            # inside_cab_serializer.update(instance.pretripinsidecab, inside_cab)
            try:
                inside_cab_serializer.update(instance.pretrip_insidecab_class_p, inside_cab)
            except PreTripInsideCabClassP.DoesNotExist:
                PreTripInsideCabClassP.objects.create(pre_trip_class_p=instance, **inside_cab)

        if "pretrip_coals_class_p" in validated_data:
            coals = validated_data.pop('pretrip_coals_class_p')
            coals_serializer = PreTripCOALSSerializerClassP()
            # inside_cab_serializer.update(instance.pretripinsidecab, inside_cab)
            try:
                coals_serializer.update(instance.pretrip_coals_class_p, coals)
            except PreTripCOALSClassP.DoesNotExist:
                PreTripCOALSClassP.objects.create(pre_trip_class_p=instance, **coals)

        if "pretrip_engine_compartment_class_p" in validated_data:
            engine_compartment = validated_data.pop('pretrip_engine_compartment_class_p')
            engine_compartment_serializer = PreTripEngineCompartmentSerializerClassP()
            try:
                engine_compartment_serializer.update(instance.pretrip_engine_compartment_class_p, engine_compartment)
            except PreTripEngineCompartmentClassP.DoesNotExist:
                PreTripEngineCompartmentClassP.objects.create(pre_trip_class_p=instance, **engine_compartment)

        if "pretrip_vehicle_front_class_p" in validated_data:
            vehicle_front = validated_data.pop('pretrip_vehicle_front_class_p')
            vehicle_front_serializer = PreTripVehicleFrontSerializerClassP()
            # inside_cab_serializer.update(instance.pretripinsidecab, inside_cab)
            try:
                vehicle_front_serializer.update(instance.pretrip_vehicle_front_class_p, vehicle_front)
            except PreTripVehicleFrontClassP.DoesNotExist:
                PreTripVehicleFrontClassP.objects.create(pre_trip_class_p=instance, **vehicle_front)

        if "pretrip_both_sides_vehicle_class_p" in validated_data:
            both_sides_vehicle = validated_data.pop('pretrip_both_sides_vehicle_class_p')
            both_sides_vehicle_serializer = PreTripBothSidesVehicleSerializerClassP()
            try:
                both_sides_vehicle_serializer.update(instance.pretrip_both_sides_vehicle_class_p, both_sides_vehicle)
            except PreTripBothSidesVehiclesClassP.DoesNotExist:
                PreTripBothSidesVehiclesClassP.objects.create(pre_trip_class_p=instance, **both_sides_vehicle)

        if "pretrip_handycap_class_p" in validated_data:
            handy_cap = validated_data.pop('pretrip_handycap_class_p')
            handy_cap_serializer = PreTripHandyCapSerializerClassP()
            try:
                handy_cap_serializer.update(instance.pretrip_handycap_class_p, handy_cap)
            except PreTripHandyCapClassP.DoesNotExist:
                PreTripHandyCapClassP.objects.create(pre_trip_class_p=instance, **handy_cap)

        if "pretrip_rear_of_vehicle_class_p" in validated_data:
            rear_of_vehicle = validated_data.pop('pretrip_rear_of_vehicle_class_p')
            rear_of_vehicle_serializer = PreTripRearOfVehicleSerializerClassP()
            try:
                rear_of_vehicle_serializer.update(instance.pretrip_rear_of_vehicle_class_p, rear_of_vehicle)
            except PreTripRearOfVehicleClassP.DoesNotExist:
                PreTripRearOfVehicleClassP.objects.create(pre_trip_class_p=instance, **rear_of_vehicle)

        if "pretrip_posttrip_class_p" in validated_data:
            post_trip = validated_data.pop('pretrip_posttrip_class_p')
            post_trip_serializer = PreTripPostTripSerializerClassP()
            try:
                post_trip_serializer.update(instance.pretrip_posttrip_class_p, post_trip)
            except PreTripPostTripClassP.DoesNotExist:
                PreTripPostTripClassP.objects.create(pre_trip_class_p=instance, **post_trip)

        if "pretrip_cargo_area_class_p" in validated_data:
            cargo_area = validated_data.pop('pretrip_cargo_area_class_p')
            cargo_area_serializer = PreTripCargoAreaClassPSerializer()
            try:
                cargo_area_serializer.update(instance.pretrip_cargo_area_class_p, cargo_area)
            except PreTripCargoAreaClassP.DoesNotExist:
                PreTripCargoAreaClassP.objects.create(pre_trip_class_p=instance, **cargo_area)

        if "pretrip_ramp_class_p" in validated_data:
            ramp = validated_data.pop('pretrip_ramp_class_p')
            ramp_serializer = PreTripRampClassPSerializer()
            try:
                ramp_serializer.update(instance.pretrip_ramp_class_p, ramp)
            except PreTripRampClassP.DoesNotExist:
                PreTripRampClassP.objects.create(pre_trip_class_p=instance, **ramp)

        if "pretrip_interior_operation_class_p" in validated_data:
            interior_operations = validated_data.pop('pretrip_interior_operation_class_p')
            interior_operations_serializer = PreTripInteriorOperationClassPSerializer()
            try:
                interior_operations_serializer.update(instance.pretrip_interior_operation_class_p,
                                                      interior_operations)
            except PreTripInteriorOperationClassP.DoesNotExist:
                PreTripInteriorOperationClassP.objects.create(pre_trip_class_p=instance, **interior_operations)

        return super(self.__class__, self).update(instance, validated_data)
        # return instance
