from rest_framework import serializers

from safe_driver.api.v1.mixins import DBTableNameMixin
from safe_driver.api.v1.serializers import StudentTestSerializer, StudentDetailSerializer
from safe_driver.image_functions import base64_to_image_content
from safe_driver.models.pretrips_class_c import *


class PreTripInsideCabSerializerClassC(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripInsideCabClassC
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_c': {
                'read_only': True
            }
        }


class PreTripEngineCompartmentSerializerClassC(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripEngineCompartmentClassC
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_c': {
                'read_only': True
            }
        }


class PreTripVehicleFrontSerializerClassC(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripVehicleFrontClassC
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_c': {
                'read_only': True
            }
        }


class PreTripBothSidesVehicleSerializerClassC(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripBothSidesVehiclesClassC
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_c': {
                'read_only': True
            }
        }


class PreTripVehicleRearSerializerClassC(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripVehicleRearClassC
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_c': {
                'read_only': True
            }
        }


class PreTripCargoAreaSerializerClassC(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripCargoAreaClassC
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_c': {
                'read_only': True
            }
        }


class PreTripPostTripSerializerClassC(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripPostTripClassC
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_c': {
                'read_only': True
            }
        }


class PreTripSerializerClassC(DBTableNameMixin, serializers.ModelSerializer):
    test = StudentTestSerializer(read_only=True)
    inside_cab = PreTripInsideCabSerializerClassC(source='pretrip_insidecab_class_c', required=False)
    engine_compartment = PreTripEngineCompartmentSerializerClassC(source='pretrip_engine_compartment_class_c',
                                                                  required=False)
    vehicle_front = PreTripVehicleFrontSerializerClassC(source='pretrip_vehicle_front_class_c', required=False)
    both_sides_vehicle = PreTripBothSidesVehicleSerializerClassC(source='pretrip_both_sides_vehicle_class_c',
                                                                 required=False)
    vehicle_rear = PreTripVehicleRearSerializerClassC(source='pretrip_vehicle_rear_class_c', required=False)
    cargo_area = PreTripCargoAreaSerializerClassC(source='pretrip_cargo_area_class_c', required=False)
    post_trip = PreTripPostTripSerializerClassC(source='pretrip_posttrip_class_c', required=False)

    # student = UserStudentSerializer(read_only=True)
    driver_signature = serializers.CharField(required=False, write_only=True)
    evaluator_signature = serializers.CharField(required=False, write_only=True)
    company_rep_signature = serializers.CharField(required=False, write_only=True)

    def to_representation(self, instance):
        res = super(PreTripSerializerClassC, self).to_representation(instance)
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
        model = PreTripClassC
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

        if "pretrip_insidecab_class_c" in validated_data:
            inside_cab = validated_data.pop('pretrip_insidecab_class_c')
            inside_cab_serializer = PreTripInsideCabSerializerClassC()
            # inside_cab_serializer.update(instance.pretripinsidecab, inside_cab)
            try:
                inside_cab_serializer.update(instance.pretrip_insidecab_class_c, inside_cab)
            except PreTripInsideCabClassC.DoesNotExist:
                PreTripInsideCabClassC.objects.create(pre_trip_class_c=instance, **inside_cab)

        if "pretrip_engine_compartment_class_c" in validated_data:
            engine_compartment = validated_data.pop('pretrip_engine_compartment_class_c')
            engine_compartment_serializer = PreTripEngineCompartmentSerializerClassC()
            try:
                engine_compartment_serializer.update(instance.pretrip_engine_compartment_class_c, engine_compartment)
            except PreTripEngineCompartmentClassC.DoesNotExist:
                PreTripEngineCompartmentClassC.objects.create(pre_trip_class_c=instance, **engine_compartment)

        if "pretrip_vehicle_front_class_c" in validated_data:
            vehicle_front = validated_data.pop('pretrip_vehicle_front_class_c')
            vehicle_front_serializer = PreTripVehicleFrontSerializerClassC()
            # inside_cab_serializer.update(instance.pretripinsidecab, inside_cab)
            try:
                vehicle_front_serializer.update(instance.pretrip_vehicle_front_class_c, vehicle_front)
            except PreTripVehicleFrontClassC.DoesNotExist:
                PreTripVehicleFrontClassC.objects.create(pre_trip_class_c=instance, **vehicle_front)

        if "pretrip_both_sides_vehicle_class_c" in validated_data:
            both_sides_vehicle = validated_data.pop('pretrip_both_sides_vehicle_class_c')
            both_sides_vehicle_serializer = PreTripBothSidesVehicleSerializerClassC()
            try:
                both_sides_vehicle_serializer.update(instance.pretrip_both_sides_vehicle_class_c, both_sides_vehicle)
            except PreTripBothSidesVehiclesClassC.DoesNotExist:
                PreTripBothSidesVehiclesClassC.objects.create(pre_trip_class_c=instance, **both_sides_vehicle)

        if "pretrip_vehicle_rear_class_c" in validated_data:
            vehicle_rear = validated_data.pop('pretrip_vehicle_rear_class_c')
            vehicle_rear_serializer = PreTripVehicleRearSerializerClassC()
            try:
                vehicle_rear_serializer.update(instance.pretrip_vehicle_rear_class_c, vehicle_rear)
            except PreTripVehicleRearClassC.DoesNotExist:
                PreTripVehicleRearClassC.objects.create(pre_trip_class_c=instance, **vehicle_rear)

        if "pretrip_cargo_area_class_c" in validated_data:
            cargo_area = validated_data.pop('pretrip_cargo_area_class_c')
            cargo_area_serializer = PreTripCargoAreaSerializerClassC()
            try:
                cargo_area_serializer.update(instance.pretrip_cargo_area_class_c, cargo_area)
            except PreTripCargoAreaClassC.DoesNotExist:
                PreTripCargoAreaClassC.objects.create(pre_trip_class_c=instance, **cargo_area)

        if "pretrip_posttrip_class_c" in validated_data:
            post_trip = validated_data.pop('pretrip_posttrip_class_c')
            post_trip_serializer = PreTripPostTripSerializerClassC()
            try:
                post_trip_serializer.update(instance.pretrip_posttrip_class_c, post_trip)
            except PreTripPostTripClassC.DoesNotExist:
                PreTripPostTripClassC.objects.create(pre_trip_class_c=instance, **post_trip)

        return super(PreTripSerializerClassC, self).update(instance, validated_data)
        # return instance
