from rest_framework import serializers
from safe_driver.api.v1.mixins import SerializerFiledAttributesMixin
from safe_driver.api.v1.serializers import StudentTestSerializer, StudentInfoSerializer, StudentDetailSerializer
from safe_driver.image_functions import base64_to_image_content
from safe_driver.models.pretrips_bus import *
from users.api.v1.serializers import UserStudentSerializer


class PreTripInsideCabSerializerBus(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripInsideCabBus
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_bus': {
                'read_only': True
            }
        }


class PreTripCOALSSerializerBus(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripCOALSBus
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_bus': {
                'read_only': True
            }
        }


class PreTripEngineCompartmentSerializerBus(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripEngineCompartmentBus
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_bus': {
                'read_only': True
            }
        }


class PreTripVehicleFrontSerializerBus(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripVehicleFrontBus
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_bus': {
                'read_only': True
            }
        }


class PreTripBothSidesVehicleSerializerBus(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripBothSidesVehiclesBus
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_bus': {
                'read_only': True
            }
        }


class PreTripHandyCapSerializerBus(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripHandyCapBus
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_bus': {
                'read_only': True
            }
        }


class PreTripRearOfVehicleSerializerBus(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripRearOfVehicleBus
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_bus': {
                'read_only': True
            }
        }


class PreTripPostTripSerializerBus(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripPostTripBus
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_bus': {
                'read_only': True
            }
        }


class PreTripCargoAreaBusSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripCargoAreaBus
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_bus': {
                'read_only': True
            }
        }


class PreTripRampBusSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripRampBus
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_bus': {
                'read_only': True
            }
        }


class PreTripInteriorOperationBusSerializer(serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripInteriorOperationBus
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_bus': {
                'read_only': True
            }
        }


class PreTripSerializerBus(serializers.ModelSerializer):
    test = StudentTestSerializer(read_only=True)
    inside_cab = PreTripInsideCabSerializerBus(source='pretrip_insidecab_bus', read_only=True)
    coals = PreTripCOALSSerializerBus(source='pretrip_coals_bus', read_only=True)
    engine_compartment = PreTripEngineCompartmentSerializerBus(source='pretrip_engine_compartment_bus',
                                                               read_only=True)
    vehicle_front = PreTripVehicleFrontSerializerBus(source='pretrip_vehicle_front_bus', read_only=True)
    both_sides_vehicle = PreTripBothSidesVehicleSerializerBus(source='pretrip_both_sides_vehicle_bus',
                                                              read_only=True)
    handy_cap = PreTripHandyCapSerializerBus(
        source='pretrip_handycap_bus', read_only=True)
    rear_of_vehicle = PreTripRearOfVehicleSerializerBus(source='pretrip_rear_of_vehicle_bus',
                                                        read_only=True)

    cargo_area = PreTripCargoAreaBusSerializer(source='pretrip_cargo_area_bus', read_only=True)
    ramp = PreTripRampBusSerializer(source='pretrip_ramp_bus', read_only=True)
    interior_operations = PreTripInteriorOperationBusSerializer(source='pretrip_interior_operation_bus', read_only=True)

    post_trip = PreTripPostTripSerializerBus(source='pretrip_posttrip_bus', read_only=True)
    # student = StudentDetailSerializer(source='test__student_tests')
    driver_signature = serializers.CharField(required=False, write_only=True)
    evaluator_signature = serializers.CharField(required=False, write_only=True)
    company_rep_signature = serializers.CharField(required=False, write_only=True)

    def to_representation(self, instance):
        res = super(PreTripSerializerBus, self).to_representation(instance)
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
        model = PreTripBus
        fields = '__all__'
        # exclude = ('student', )

    def update(self, instance, validated_data):
        request = self.context.get("request")

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

        if "inside_cab" in request.data:
            inside_cab = request.data.get('inside_cab')
            inside_cab_serializer = PreTripInsideCabSerializerBus()
            # inside_cab_serializer.update(instance.pretripinsidecab, inside_cab)
            try:
                inside_cab_serializer.update(instance.pretrip_insidecab_bus, inside_cab)
            except PreTripInsideCabBus.DoesNotExist:
                PreTripInsideCabBus.objects.create(pre_trip_bus=instance, **inside_cab)

        if "coals" in request.data:
            coals = request.data.get('coals')
            coals_serializer = PreTripCOALSSerializerBus()
            # inside_cab_serializer.update(instance.pretripinsidecab, inside_cab)
            try:
                coals_serializer.update(instance.pretrip_coals_bus, coals)
            except PreTripCOALSBus.DoesNotExist:
                PreTripCOALSBus.objects.create(pre_trip_bus=instance, **coals)

        if "engine_compartment" in request.data:
            engine_compartment = request.data.get('engine_compartment')
            engine_compartment_serializer = PreTripEngineCompartmentSerializerBus()
            try:
                engine_compartment_serializer.update(instance.pretrip_engine_compartment_bus, engine_compartment)
            except PreTripEngineCompartmentBus.DoesNotExist:
                PreTripEngineCompartmentBus.objects.create(pre_trip_bus=instance, **engine_compartment)

        if "vehicle_front" in request.data:
            vehicle_front = request.data.get('vehicle_front')
            vehicle_front_serializer = PreTripVehicleFrontSerializerBus()
            # inside_cab_serializer.update(instance.pretripinsidecab, inside_cab)
            try:
                vehicle_front_serializer.update(instance.pretrip_vehicle_front_bus, vehicle_front)
            except PreTripVehicleFrontBus.DoesNotExist:
                PreTripVehicleFrontBus.objects.create(pre_trip_bus=instance, **vehicle_front)

        if "both_sides_vehicle" in request.data:
            both_sides_vehicle = request.data.get('both_sides_vehicle')
            both_sides_vehicle_serializer = PreTripBothSidesVehicleSerializerBus()
            try:
                both_sides_vehicle_serializer.update(instance.pretrip_both_sides_vehicle_bus, both_sides_vehicle)
            except PreTripBothSidesVehiclesBus.DoesNotExist:
                PreTripBothSidesVehiclesBus.objects.create(pre_trip_bus=instance, **both_sides_vehicle)

        if "handy_cap" in request.data:
            handy_cap = request.data.get('handy_cap')
            handy_cap_serializer = PreTripHandyCapSerializerBus()
            try:
                handy_cap_serializer.update(instance.pretrip_handycap_bus, handy_cap)
            except PreTripHandyCapBus.DoesNotExist:
                PreTripHandyCapBus.objects.create(pre_trip_bus=instance, **handy_cap)

        if "rear_of_vehicle" in request.data:
            rear_of_vehicle = request.data.get('rear_of_vehicle')
            rear_of_vehicle_serializer = PreTripRearOfVehicleSerializerBus()
            try:
                rear_of_vehicle_serializer.update(instance.pretrip_rear_of_vehicle_bus, rear_of_vehicle)
            except PreTripRearOfVehicleBus.DoesNotExist:
                PreTripRearOfVehicleBus.objects.create(pre_trip_bus=instance, **rear_of_vehicle)

        if "post_trip" in request.data:
            post_trip = request.data.get('post_trip')
            post_trip_serializer = PreTripPostTripSerializerBus()
            try:
                post_trip_serializer.update(instance.pretrip_posttrip_bus, post_trip)
            except PreTripPostTripBus.DoesNotExist:
                PreTripPostTripBus.objects.create(pre_trip_bus=instance, **post_trip)

        if "cargo_area" in request.data:
            cargo_area = request.data.get('cargo_area')
            cargo_area_serializer = PreTripCargoAreaBusSerializer()
            try:
                cargo_area_serializer.update(instance.pretrip_cargo_area_bus, cargo_area)
            except PreTripCargoAreaBus.DoesNotExist:
                PreTripCargoAreaBus.objects.create(pre_trip_bus=instance, **cargo_area)

        if "ramp" in request.data:
            ramp = request.data.get('ramp')
            ramp_serializer = PreTripRampBusSerializer()
            try:
                ramp_serializer.update(instance.pretrip_ramp_bus, ramp)
            except PreTripRampBus.DoesNotExist:
                PreTripRampBus.objects.create(pre_trip_bus=instance, **ramp)

        if "interiior_operations" in request.data:
            interiior_operations = request.data.get('interiior_operations')
            interiior_operations_serializer = PreTripInteriorOperationBusSerializer()
            try:
                interiior_operations_serializer.update(instance.pretrip_cargo_area_bus, interiior_operations)
            except PreTripInteriorOperationBus.DoesNotExist:
                PreTripInteriorOperationBus.objects.create(pre_trip_bus=instance, **interiior_operations)

        return super(PreTripSerializerBus, self).update(instance, validated_data)
        # return instance
