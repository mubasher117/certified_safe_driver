from rest_framework import serializers
from safe_driver.api.v1.mixins import SerializerFiledAttributesMixin, DBTableNameMixin
from safe_driver.api.v1.serializers import StudentTestSerializer, StudentDetailSerializer
from safe_driver.image_functions import base64_to_image_content
from safe_driver.models.pretrips_class_b import *
from users.api.v1.serializers import UserStudentSerializer


class PreTripInsideCabSerializerClassB(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripInsideCabClassB
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_b': {
                'read_only': True
            }
        }


class PreTripCOALSSerializerClassB(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripCOALSClassB
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_b': {
                'read_only': True
            }
        }


class PreTripEngineCompartmentSerializerClassB(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripEngineCompartmentClassB
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_b': {
                'read_only': True
            }
        }


class PreTripVehicleFrontSerializerClassB(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripVehicleFrontClassB
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_b': {
                'read_only': True
            }
        }


class PreTripBothSidesVehicleSerializerClassB(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripBothSidesVehiclesClassB
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_b': {
                'read_only': True
            }
        }


class PreTripVehicleOrTractorRearSerializerClassB(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripVehicleOrTractorRearClassB
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_b': {
                'read_only': True
            }
        }


class PreTripBoxHeaderBoardSerializerClassB(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripBoxHeaderBoardClassB
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_b': {
                'read_only': True
            }
        }


class PreTripDriverSideBoxSerializerClassB(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripDriverSideBoxClassB
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_b': {
                'read_only': True
            }
        }


class PreTripCargoAreaSerializerClassB(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripCargoAreaClassB
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_b': {
                'read_only': True
            }
        }


class PreTripPassengerSideBoxSerializerClassB(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripPassengerSideBoxClassB
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_b': {
                'read_only': True
            }
        }


class PreTripPostTripSerializerClassB(DBTableNameMixin, serializers.ModelSerializer):
    possible_points = serializers.IntegerField(read_only=True)
    points_received = serializers.IntegerField(read_only=True)
    percent_effective = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = PreTripPostTripClassB
        fields = '__all__'
        extra_kwargs = {
            'pre_trip_class_b': {
                'read_only': True
            }
        }


class PreTripSerializerClassB(DBTableNameMixin, serializers.ModelSerializer):
    test = StudentTestSerializer(read_only=True)
    inside_cab = PreTripInsideCabSerializerClassB(source='pretrip_insidecab_class_b', required=False)
    coals = PreTripCOALSSerializerClassB(source='pretrip_coals_class_b', required=False)
    engine_compartment = PreTripEngineCompartmentSerializerClassB(source='pretrip_engine_compartment_class_b',
                                                                  required=False)
    vehicle_front = PreTripVehicleFrontSerializerClassB(source='pretrip_vehicle_front_class_b', required=False)
    both_sides_vehicle = PreTripBothSidesVehicleSerializerClassB(source='pretrip_both_sides_vehicle_class_b',
                                                                 required=False)
    vehicle_or_tractor_rear = PreTripVehicleOrTractorRearSerializerClassB(
        source='pretrip_vehicle_or_tractor_rear_class_b', required=False)
    box_header_board = PreTripBoxHeaderBoardSerializerClassB(source='pretrip_box_header_board_class_b',
                                                             required=False)
    driver_side_box = PreTripDriverSideBoxSerializerClassB(
        source='pretrip_driver_side_box_class_b', required=False)
    cargo_area = PreTripCargoAreaSerializerClassB(source='pretrip_cargo_area_class_b', required=False)
    passenger_side_box = PreTripPassengerSideBoxSerializerClassB(
        source='pretrip_passenger_side_box_class_b', required=False)
    post_trip = PreTripPostTripSerializerClassB(source='pretrip_posttrip_class_b', required=False)
    # student = UserStudentSerializer(read_only=True)

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
        model = PreTripClassB
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

        if "pretrip_insidecab_class_b" in validated_data:
            inside_cab = validated_data.pop('pretrip_insidecab_class_b')
            inside_cab_serializer = PreTripInsideCabSerializerClassB()
            # inside_cab_serializer.update(instance.pretripinsidecab, inside_cab)
            try:
                inside_cab_serializer.update(instance.pretrip_insidecab_class_b, inside_cab)
            except PreTripInsideCabClassB.DoesNotExist:
                PreTripInsideCabClassB.objects.create(pre_trip_class_b=instance, **inside_cab)

        if "pretrip_coals_class_b" in validated_data:
            coals = validated_data.pop('pretrip_coals_class_b')
            coals_serializer = PreTripCOALSSerializerClassB()
            # inside_cab_serializer.update(instance.pretripinsidecab, inside_cab)
            try:
                coals_serializer.update(instance.pretrip_coals_class_b, coals)
            except PreTripCOALSClassB.DoesNotExist:
                PreTripCOALSClassB.objects.create(pre_trip_class_b=instance, **coals)

        if "pretrip_engine_compartment_class_b" in validated_data:
            engine_compartment = validated_data.pop('pretrip_engine_compartment_class_b')
            engine_compartment_serializer = PreTripEngineCompartmentSerializerClassB()
            try:
                engine_compartment_serializer.update(instance.pretrip_engine_compartment_class_b, engine_compartment)
            except PreTripEngineCompartmentClassB.DoesNotExist:
                PreTripEngineCompartmentClassB.objects.create(pre_trip_class_b=instance, **engine_compartment)

        if "pretrip_vehicle_front_class_b" in validated_data:
            vehicle_front = validated_data.pop('pretrip_vehicle_front_class_b')
            vehicle_front_serializer = PreTripVehicleFrontSerializerClassB()
            # inside_cab_serializer.update(instance.pretripinsidecab, inside_cab)
            try:
                vehicle_front_serializer.update(instance.pretrip_vehicle_front_class_b, vehicle_front)
            except PreTripVehicleFrontClassB.DoesNotExist:
                PreTripVehicleFrontClassB.objects.create(pre_trip_class_b=instance, **vehicle_front)

        if "pretrip_both_sides_vehicle_class_b" in validated_data:
            both_sides_vehicle = validated_data.pop('pretrip_both_sides_vehicle_class_b')
            both_sides_vehicle_serializer = PreTripBothSidesVehicleSerializerClassB()
            try:
                both_sides_vehicle_serializer.update(instance.pretrip_both_sides_vehicle_class_b, both_sides_vehicle)
            except PreTripBothSidesVehiclesClassB.DoesNotExist:
                PreTripBothSidesVehiclesClassB.objects.create(pre_trip_class_b=instance, **both_sides_vehicle)

        if "pretrip_vehicle_or_tractor_rear_class_b" in validated_data:
            vehicle_or_tractor_rear = validated_data.pop('pretrip_vehicle_or_tractor_rear_class_b')
            vehicle_or_tractor_rear_serializer = PreTripVehicleOrTractorRearSerializerClassB()
            try:
                vehicle_or_tractor_rear_serializer.update(instance.pretrip_vehicle_or_tractor_rear_class_b,
                                                          vehicle_or_tractor_rear)
            except PreTripVehicleOrTractorRearClassB.DoesNotExist:
                PreTripVehicleOrTractorRearClassB.objects.create(pre_trip_class_b=instance, **vehicle_or_tractor_rear)

        if "pretrip_box_header_board_class_b" in validated_data:
            box_header_board = validated_data.pop('pretrip_box_header_board_class_b')
            box_header_board_serializer = PreTripBoxHeaderBoardSerializerClassB()
            try:
                box_header_board_serializer.update(instance.pretrip_box_header_board_class_b, box_header_board)
            except PreTripBoxHeaderBoardClassB.DoesNotExist:
                PreTripBoxHeaderBoardClassB.objects.create(pre_trip_class_b=instance, **box_header_board)

        if "pretrip_driver_side_box_class_b" in validated_data:
            driver_side_box = validated_data.pop('pretrip_driver_side_box_class_b')
            driver_side_box_serializer = PreTripDriverSideBoxSerializerClassB()
            try:
                driver_side_box_serializer.update(instance.pretrip_driver_side_box_class_b, driver_side_box)
            except PreTripDriverSideBoxClassB.DoesNotExist:
                PreTripDriverSideBoxClassB.objects.create(pre_trip_class_b=instance, **driver_side_box)

        if "pretrip_cargo_area_class_b" in validated_data:
            cargo_area = validated_data.pop('pretrip_cargo_area_class_b')
            cargo_area_serializer = PreTripCargoAreaSerializerClassB()
            try:
                cargo_area_serializer.update(instance.pretrip_cargo_area_class_b, cargo_area)
            except PreTripCargoAreaClassB.DoesNotExist:
                PreTripCargoAreaClassB.objects.create(pre_trip_class_b=instance, **cargo_area)

        if "pretrip_passenger_side_trailer_box_class_b" in validated_data:
            passenger_side_box = validated_data.pop('pretrip_passenger_side_trailer_box_class_b')
            passenger_side_box_serializer = PreTripPassengerSideBoxSerializerClassB()
            try:
                passenger_side_box_serializer.update(instance.pretrip_passenger_side_trailer_box_class_b,
                                                     passenger_side_box)
            except PreTripPassengerSideBoxClassB.DoesNotExist:
                PreTripPassengerSideBoxClassB.objects.create(pre_trip_class_b=instance, **passenger_side_box)

        if "pretrip_posttrip_class_b" in validated_data:
            post_trip = validated_data.pop('pretrip_posttrip_class_b')
            post_trip_serializer = PreTripPostTripSerializerClassB()
            try:
                post_trip_serializer.update(instance.pretrip_posttrip_class_b, post_trip)
            except PreTripPostTripClassB.DoesNotExist:
                PreTripPostTripClassB.objects.create(pre_trip_class_b=instance, **post_trip)

        return super(self.__class__, self).update(instance, validated_data)
        # return instance
