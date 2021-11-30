from rest_framework import serializers
from safe_driver.api.v1.mixins import SerializerFiledAttributesMixin, DBTableNameMixin
from safe_driver.api.v1.serializers import StudentTestSerializer, StudentDetailSerializer
from safe_driver.image_functions import base64_to_image_content
from safe_driver.models.pretrips_class_a import *
from users.api.v1.serializers import UserStudentSerializer


class PreTripInsideCabSerializerClassA(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripInsideCabClassA
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_a': {
                'read_only': True
            }
        }


class PreTripCOALSSerializerClassA(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripCOALSClassA
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_a': {
                'read_only': True
            }
        }


class PreTripEngineCompartmentSerializerClassA(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripEngineCompartmentClassA
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_a': {
                'read_only': True
            }
        }


class PreTripVehicleFrontSerializerClassA(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripVehicleFrontClassA
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_a': {
                'read_only': True
            }
        }


class PreTripBothSidesVehicleSerializerClassA(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripBothSidesVehiclesClassA
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_a': {
                'read_only': True
            }
        }


class PreTripVehicleOrTractorRearSerializerClassA(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripVehicleOrTractorRearClassA
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_a': {
                'read_only': True
            }
        }


class PreTripFrontTrailerBoxSerializerClassA(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripFrontTrailerBoxClassA
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_a': {
                'read_only': True
            }
        }


class PreTripDriverSideTrailerBoxSerializerClassA(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripDriverSideTrailerBoxClassA
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_a': {
                'read_only': True
            }
        }


class PreTripRearTrailerBoxSerializerClassA(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripRearTrailerBoxClassA
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_a': {
                'read_only': True
            }
        }


class PreTripPassengerSideTrailerBoxSerializerClassA(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripPassengerSideTrailerBoxClassA
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_a': {
                'read_only': True
            }
        }


class PreTripDollySerializerClassA(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripDollyClassA
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_a': {
                'read_only': True
            }
        }


class PreTripPostTripSerializerClassA(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripPostTripClassA
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_a': {
                'read_only': True
            }
        }


class PreTripSerializerClassA(DBTableNameMixin, serializers.ModelSerializer):
    test = StudentTestSerializer(read_only=True)
    inside_cab = PreTripInsideCabSerializerClassA(source='pretrip_insidecab_class_a', required=False)

    coals = PreTripCOALSSerializerClassA(source='pretrip_coals_class_a', required=False)
    engine_compartment = PreTripEngineCompartmentSerializerClassA(source='pretrip_engine_compartment_class_a',
                                                                  required=False)
    vehicle_front = PreTripVehicleFrontSerializerClassA(source='pretrip_vehicle_front_class_a', required=False)
    both_sides_vehicle = PreTripBothSidesVehicleSerializerClassA(source='pretrip_both_sides_vehicle_class_a',
                                                                 required=False)
    vehicle_or_tractor_rear = PreTripVehicleOrTractorRearSerializerClassA(
        source='pretrip_vehicle_or_tractor_rear_class_a', required=False)
    front_trailer_box = PreTripFrontTrailerBoxSerializerClassA(source='pretrip_front_trailer_box_class_a',
                                                               required=False)
    driver_side_trailer_box = PreTripDriverSideTrailerBoxSerializerClassA(
        source='pretrip_driver_side_trailer_box_class_a', required=False)
    rear_trailer_box = PreTripRearTrailerBoxSerializerClassA(source='pretrip_rear_trailer_box_class_a', required=False)
    passenger_side_trailer_box = PreTripPassengerSideTrailerBoxSerializerClassA(
        source='pretrip_passenger_side_trailer_box_class_a', required=False)
    dolly = PreTripDollySerializerClassA(source='pretrip_dolly_class_a', required=False)
    post_trip = PreTripPostTripSerializerClassA(source='pretrip_posttrip_class_a', required=False)

    # student = UserStudentSerializer(read_only=True)
    driver_signature = serializers.CharField(required=False)
    evaluator_signature = serializers.CharField(required=False)
    company_rep_signature = serializers.CharField(required=False)

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
        model = PreTripClassA
        fields = '__all__'
        # exclude = ('student', )

    def update(self, instance, validated_data):
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

        if "pretrip_insidecab_class_a" in validated_data:
            inside_cab = validated_data.pop('pretrip_insidecab_class_a')
            # inside_cab_serializer = PreTripInsideCabSerializerClassA()
            # inside_cab_serializer.update(instance.pretripinsidecab, inside_cab)
            try:
                PreTripInsideCabSerializerClassA().update(instance.pretrip_insidecab_class_a, inside_cab)
            except PreTripInsideCabClassA.DoesNotExist:
                PreTripInsideCabClassA.objects.create(pre_trip_class_a=instance, **inside_cab)

        if "pretrip_coals_class_a" in validated_data:
            coals = validated_data.pop('pretrip_coals_class_a')
            coals_serializer = PreTripCOALSSerializerClassA()
            try:
                coals_serializer.update(instance.pretrip_coals_class_a, coals)
            except PreTripCOALSClassA.DoesNotExist:
                PreTripCOALSClassA.objects.create(pre_trip_class_a=instance, **coals)
        #
        if "pretrip_engine_compartment_class_a" in validated_data:
            engine_compartment = validated_data.pop('pretrip_engine_compartment_class_a')
            engine_compartment_serializer = PreTripEngineCompartmentSerializerClassA()
            try:
                engine_compartment_serializer.update(instance.pretrip_engine_compartment_class_a, engine_compartment)
            except PreTripEngineCompartmentClassA.DoesNotExist:
                PreTripEngineCompartmentClassA.objects.create(pre_trip_class_a=instance, **engine_compartment)
        #
        if "pretrip_vehicle_front_class_a" in validated_data:
            vehicle_front = validated_data.pop('pretrip_vehicle_front_class_a')
            vehicle_front_serializer = PreTripVehicleFrontSerializerClassA()
            try:
                vehicle_front_serializer.update(instance.pretrip_vehicle_front_class_a, vehicle_front)
            except PreTripVehicleFrontClassA.DoesNotExist:
                PreTripVehicleFrontClassA.objects.create(pre_trip_class_a=instance, **vehicle_front)

        if "pretrip_both_sides_vehicle_class_a" in validated_data:
            both_sides_vehicle = validated_data.pop('pretrip_both_sides_vehicle_class_a')
            both_sides_vehicle_serializer = PreTripBothSidesVehicleSerializerClassA()
            try:
                both_sides_vehicle_serializer.update(instance.pretrip_both_sides_vehicle_class_a, both_sides_vehicle)
            except PreTripBothSidesVehiclesClassA.DoesNotExist:
                PreTripBothSidesVehiclesClassA.objects.create(pre_trip_class_a=instance, **both_sides_vehicle)

        if "pretrip_vehicle_or_tractor_rear_class_a" in validated_data:
            vehicle_or_tractor_rear = validated_data.pop('pretrip_vehicle_or_tractor_rear_class_a')
            vehicle_or_tractor_rear_serializer = PreTripVehicleOrTractorRearSerializerClassA()
            try:
                vehicle_or_tractor_rear_serializer.update(instance.pretrip_vehicle_or_tractor_rear_class_a,
                                                          vehicle_or_tractor_rear)
            except PreTripVehicleOrTractorRearClassA.DoesNotExist:
                PreTripVehicleOrTractorRearClassA.objects.create(pre_trip_class_a=instance, **vehicle_or_tractor_rear)

        if "pretrip_front_trailer_box_class_a" in validated_data:
            front_trailer_box = validated_data.pop('pretrip_front_trailer_box_class_a')
            front_trailer_box_serializer = PreTripFrontTrailerBoxSerializerClassA()
            try:
                front_trailer_box_serializer.update(instance.pretrip_front_trailer_box_class_a, front_trailer_box)
            except PreTripFrontTrailerBoxClassA.DoesNotExist:
                PreTripFrontTrailerBoxClassA.objects.create(pre_trip_class_a=instance, **front_trailer_box)

        if "pretrip_driver_side_trailer_box_class_a" in validated_data:
            driver_side_trailer_box = validated_data.pop('pretrip_driver_side_trailer_box_class_a')
            driver_side_trailer_box_serializer = PreTripDriverSideTrailerBoxSerializerClassA()
            try:
                driver_side_trailer_box_serializer.update(instance.pretrip_driver_side_trailer_box_class_a,
                                                          driver_side_trailer_box)
            except PreTripDriverSideTrailerBoxClassA.DoesNotExist:
                PreTripDriverSideTrailerBoxClassA.objects.create(pre_trip_class_a=instance, **driver_side_trailer_box)

        if "pretrip_rear_trailer_box_class_a" in validated_data:
            rear_trailer_box = validated_data.pop('pretrip_rear_trailer_box_class_a')
            rear_trailer_box_serializer = PreTripRearTrailerBoxSerializerClassA()
            try:
                rear_trailer_box_serializer.update(instance.pretrip_rear_trailer_box_class_a, rear_trailer_box)
            except PreTripRearTrailerBoxClassA.DoesNotExist:
                PreTripRearTrailerBoxClassA.objects.create(pretrip_rear_trailer_box_class_a=instance,
                                                           **rear_trailer_box)

        if "pretrip_passenger_side_trailer_box_class_a" in validated_data:
            passenger_side_trailer_box = validated_data.pop('pretrip_passenger_side_trailer_box_class_a')
            passenger_side_trailer_box_serializer = PreTripPassengerSideTrailerBoxSerializerClassA()
            try:
                passenger_side_trailer_box_serializer.update(instance.pretrip_passenger_side_trailer_box_class_a,
                                                             passenger_side_trailer_box)
            except PreTripPassengerSideTrailerBoxClassA.DoesNotExist:
                PreTripPassengerSideTrailerBoxClassA.objects.create(pre_trip_class_a=instance,
                                                                    **passenger_side_trailer_box)

        if "pretrip_dolly_class_a" in validated_data:
            dolly = validated_data.pop('pretrip_dolly_class_a')
            dolly_serializer = PreTripDollySerializerClassA()
            try:
                dolly_serializer.update(instance.pretrip_dolly_class_a, dolly)
            except PreTripDollyClassA.DoesNotExist:
                PreTripDollyClassA.objects.create(pre_trip_class_a=instance, **dolly)

        if "pretrip_posttrip_class_a" in validated_data:
            post_trip = validated_data.pop('pretrip_posttrip_class_a')
            post_trip_serializer = PreTripPostTripSerializerClassA()
            try:
                post_trip_serializer.update(instance.pretrip_posttrip_class_a, post_trip)
            except PreTripPostTripClassA.DoesNotExist:
                PreTripPostTripClassA.objects.create(pre_trip_class_a=instance, **post_trip)

        return super(PreTripSerializerClassA, self).update(instance, validated_data)


class TestPretripClassASerializer(serializers.ModelSerializer):
    inside_cab = PreTripInsideCabSerializerClassA(source='pretrip_insidecab_class_a', )

    class Meta:
        model = PreTripClassA
        fields = '__all__'
        extra_kwargs = {
            'test': {
                'read_only': True
            },
        }

    def update(self, instance, validated_data):
        if "pretrip_insidecab_class_a" in validated_data:
            inside_cab = validated_data.pop('pretrip_insidecab_class_a')
            try:
                inside_cab_obj = PreTripInsideCabSerializerClassA().update(instance.pretrip_insidecab_class_a,
                                                                           inside_cab)
                print(instance.pretrip_insidecab_class_a)
            except PreTripInsideCabClassA.DoesNotExist:
                inside_cab_obj = PreTripInsideCabClassA.objects.create(pre_trip_class_a=instance, **inside_cab)
                print(inside_cab_obj)
        print(instance.pretrip_insidecab_class_a)
        return super(TestPretripClassASerializer, self).update(instance, validated_data)
