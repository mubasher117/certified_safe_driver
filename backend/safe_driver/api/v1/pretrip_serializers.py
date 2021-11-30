from collections import OrderedDict

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, SkipField
from rest_framework.relations import PKOnlyObject

from safe_driver.api.v1.mixins import SerializerFiledAttributesMixin
from safe_driver.models import (
    PreTripInsideCab, PreTripCOALS, PreTripEngineCompartment, PreTripVehicleFront, PreTripBothSidesVehicle,
    PreTripVehicleOrTractorRear, PreTripFrontTrailerBox, PreTripDriverSideTrailerBox, PreTripRearTrailerBox,
    PreTripPassengerSideTrailerBox, PreTripDolly, PreTripCombinationVehicles, PreTripPostTrip, SafeDrivePreTrip
)
from users.api.v1.serializers import UserStudentSerializer


class PreTripInsideCabSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreTripInsideCab
        fields = '__all__'


class PreTripCOALSSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreTripCOALS
        fields = '__all__'


class PreTripEngineCompartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreTripEngineCompartment
        fields = '__all__'


class PreTripVehicleFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreTripVehicleFront
        fields = '__all__'


class PreTripBothSidesVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreTripBothSidesVehicle
        fields = '__all__'


class PreTripVehicleOrTractorRearSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreTripVehicleOrTractorRear
        fields = '__all__'


class PreTripFrontTrailerBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreTripFrontTrailerBox
        fields = '__all__'


class PreTripDriverSideTrailerBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreTripDriverSideTrailerBox
        fields = '__all__'


class PreTripRearTrailerBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreTripRearTrailerBox
        fields = '__all__'


class PreTripPassengerSideTrailerBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreTripPassengerSideTrailerBox
        fields = '__all__'


class PreTripDollySerializer(serializers.ModelSerializer):
    class Meta:
        model = PreTripDolly
        fields = '__all__'


class PreTripCombinationVehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreTripCombinationVehicles
        fields = '__all__'


class PreTripPostTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreTripPostTrip
        fields = '__all__'


class SafeDrivePreTripSerializer(serializers.ModelSerializer):
    inside_cab = PreTripInsideCabSerializer(source='pretripinsidecab', read_only=True)
    coals = PreTripCOALSSerializer(source='pretripcoals', read_only=True)
    engine_compartment = PreTripEngineCompartmentSerializer(source='pretripenginecompartment', read_only=True)
    vehicle_front = PreTripVehicleFrontSerializer(source='pretripvehiclefront', read_only=True)
    both_sides_vehicle = PreTripBothSidesVehicleSerializer(source='pretripbothsidesvehicle', read_only=True)
    vehicle_or_tractor_rear = PreTripVehicleOrTractorRearSerializer(source='pretripvehicleortractorrear',
                                                                    read_only=True)
    front_trailer_box = PreTripFrontTrailerBoxSerializer(source='pretripfronttrailerbox', read_only=True)
    driver_side_trailer_box = PreTripDriverSideTrailerBoxSerializer(source='pretripdriversidetrailerbox',
                                                                    read_only=True)
    rear_trailer_box = PreTripRearTrailerBoxSerializer(source='pretripreartrailerbox', read_only=True)
    passenger_side_trailer_box = PreTripPassengerSideTrailerBoxSerializer(source='pretrippassengersidetrailerbox',
                                                                          read_only=True)
    dolly = PreTripDollySerializer(source='pretripdolly', read_only=True)
    combination_vehicles = PreTripCombinationVehiclesSerializer(source='pretripcombinationvehicles', read_only=True)
    post_trip = PreTripPostTripSerializer(source='pretripposttrip', read_only=True)
    student = UserStudentSerializer(read_only=True)

    # def __init__(self, *args, **kwargs):
    #     super(SafeDrivePreTripSerializer, self).__init__(*args, **kwargs)
    #
    #     if 'labels' in self.fields:
    #         raise RuntimeError(
    #             'You cant have labels field defined '
    #             'while using MyModelSerializer'
    #         )
    #
    #     self.fields['labels'] = SerializerMethodField()
    #
    # def get_labels(self, *args):
    #     labels = {}
    #
    #     for field in self.Meta.model._meta.get_fields():
    #         if field.name in self.fields:
    #             labels[field.name] = field.verbose_name
    #
    #     return labels

    class Meta:
        model = SafeDrivePreTrip
        fields = '__all__'
        # exclude = ('student', )

    def update(self, instance, validated_data):
        request = self.context.get("request")

        if "inside_cab" in request.data:
            inside_cab = request.data.get('inside_cab')
            inside_cab_serializer = PreTripInsideCabSerializer()
            # inside_cab_serializer.update(instance.pretripinsidecab, inside_cab)
            try:
                inside_cab_serializer.update(instance.pretripinsidecab, inside_cab)
            except:
                PreTripInsideCab.objects.create(pre_trip=instance, **inside_cab)

        if "coals" in request.data:
            coals = request.data.get('coals')
            coals_serializer = PreTripCOALSSerializer()
            # inside_cab_serializer.update(instance.pretripinsidecab, inside_cab)
            try:
                coals_serializer.update(instance.pretripcoals, coals)
            except:
                PreTripCOALS.objects.create(pre_trip=instance, **coals)

        if "engine_compartment" in request.data:
            engine_compartment = request.data.get('engine_compartment')
            engine_compartment_serializer = PreTripEngineCompartmentSerializer()
            try:
                engine_compartment_serializer.update(instance.pretripenginecompartment, engine_compartment)
            except:
                PreTripEngineCompartment.objects.create(pre_trip=instance, **engine_compartment)

        if "vehicle_front" in request.data:
            vehicle_front = request.data.get('vehicle_front')
            vehicle_front_serializer = PreTripVehicleFrontSerializer()
            # inside_cab_serializer.update(instance.pretripinsidecab, inside_cab)
            try:
                vehicle_front_serializer.update(instance.pretripvehiclefront, vehicle_front)
            except:
                PreTripVehicleFront.objects.create(pre_trip=instance, **vehicle_front)

        if "both_sides_vehicle" in request.data:
            both_sides_vehicle = request.data.get('both_sides_vehicle')
            both_sides_vehicle_serializer = PreTripBothSidesVehicleSerializer()
            try:
                both_sides_vehicle_serializer.update(instance.pretripbothsidesvehicle, both_sides_vehicle)
            except:
                PreTripBothSidesVehicle.objects.create(pre_trip=instance, **both_sides_vehicle)

        if "vehicle_or_tractor_rear" in request.data:
            vehicle_or_tractor_rear = request.data.get('vehicle_or_tractor_rear')
            vehicle_or_tractor_rear_serializer = PreTripVehicleOrTractorRearSerializer()
            try:
                vehicle_or_tractor_rear_serializer.update(instance.pretripvehicleortractorrear, vehicle_or_tractor_rear)
            except:
                PreTripVehicleOrTractorRear.objects.create(pre_trip=instance, **vehicle_or_tractor_rear)

        if "front_trailer_box" in request.data:
            front_trailer_box = request.data.get('front_trailer_box')
            front_trailer_box_serializer = PreTripFrontTrailerBoxSerializer()
            try:
                front_trailer_box_serializer.update(instance.pretripfronttrailerbox, front_trailer_box)
            except:
                PreTripFrontTrailerBox.objects.create(pre_trip=instance, **front_trailer_box)

        if "driver_side_trailer_box" in request.data:
            driver_side_trailer_box = request.data.get('driver_side_trailer_box')
            driver_side_trailer_box_serializer = PreTripDriverSideTrailerBoxSerializer()
            try:
                driver_side_trailer_box_serializer.update(instance.pretripdriversidetrailerbox, driver_side_trailer_box)
            except:
                PreTripDriverSideTrailerBox.objects.create(pre_trip=instance, **driver_side_trailer_box)

        if "rear_trailer_box" in request.data:
            rear_trailer_box = request.data.get('rear_trailer_box')
            rear_trailer_box_serializer = PreTripRearTrailerBoxSerializer()
            try:
                rear_trailer_box_serializer.update(instance.pretripreartrailerbox, rear_trailer_box)
            except:
                PreTripRearTrailerBox.objects.create(pre_trip=instance, **rear_trailer_box)

        if "passenger_side_trailer_box" in request.data:
            passenger_side_trailer_box = request.data.get('passenger_side_trailer_box')
            passenger_side_trailer_box_serializer = PreTripPassengerSideTrailerBoxSerializer()
            try:
                passenger_side_trailer_box_serializer.update(instance.pretrippassengersidetrailerbox,
                                                             passenger_side_trailer_box)
            except:
                PreTripPassengerSideTrailerBox.objects.create(pre_trip=instance, **passenger_side_trailer_box)

        if "dolly" in request.data:
            dolly = request.data.get('dolly')
            dolly_serializer = PreTripDollySerializer()
            try:
                dolly_serializer.update(instance.pretripdolly, dolly)
            except:
                PreTripDolly.objects.create(pre_trip=instance, **dolly)

        if "combination_vehicles" in request.data:
            combination_vehicles = request.data.get('combination_vehicles')
            combination_vehicles_serializer = PreTripCombinationVehiclesSerializer()
            try:
                combination_vehicles_serializer.update(instance.pretripcombinationvehicles, combination_vehicles)
            except:
                PreTripCombinationVehicles.objects.create(pre_trip=instance, **combination_vehicles)

        if "post_trip" in request.data:
            post_trip = request.data.get('post_trip')
            post_trip_serializer = PreTripPostTripSerializer()
            try:
                post_trip_serializer.update(instance.pretripposttrip, post_trip)
            except:
                PreTripPostTrip.objects.create(pre_trip=instance, **post_trip)

        return super(SafeDrivePreTripSerializer, self).update(instance, validated_data)
