from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from safe_driver.models import PreTripBus, PreTripClassP
from users.api.v1.permissions import InstructorPermission
from .serializers import *

from .serializers.pretrips_bus_serializers import PreTripSerializerBus
from .serializers.pretrip_class_p_serializers import PreTripSerializerClassP


class PreTripClassADetailView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = PreTripSerializerClassA

    queryset = PreTripClassA.objects.none()

    def get_object(self):
        test_id = self.kwargs['test_id']
        student_id = self.kwargs['student_id']
        try:
            obj = PreTripClassA.objects.select_related(
                'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
                'test__student__student_info__group', 'pretrip_insidecab_class_a',
                'pretrip_coals_class_a', 'pretrip_dolly_class_a',
                'pretrip_posttrip_class_a', 'pretrip_vehicle_front_class_a',
                'pretrip_both_sides_vehicle_class_a', 'pretrip_driver_side_trailer_box_class_a',
                'pretrip_engine_compartment_class_a', 'pretrip_front_trailer_box_class_a',
                'pretrip_passenger_side_trailer_box_class_a', 'pretrip_vehicle_or_tractor_rear_class_a'
            ).get(test_id=test_id)
        except PreTripClassA.DoesNotExist:
            obj = PreTripClassA.objects.create(test_id=test_id)
        return obj

    def update(self, request, *args, **kwargs):
        serializer = PreTripSerializerClassA(self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            # serializer_data = PreTripSerializerClassA(self.get_object()).data
            return Response(serializer.data)
        return Response(serializer.errors)


class TestPretripClassView(RetrieveUpdateAPIView):
    ermission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = TestPretripClassASerializer
    queryset = PreTripClassA.objects.none()

    def get_object(self):
        obj = PreTripClassA.objects.select_related(
            'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
            'test__student__student_info__group', 'pretrip_insidecab_class_a',
            'pretrip_coals_class_a', 'pretrip_dolly_class_a',
            'pretrip_posttrip_class_a', 'pretrip_vehicle_front_class_a',
            'pretrip_both_sides_vehicle_class_a', 'pretrip_driver_side_trailer_box_class_a',
            'pretrip_engine_compartment_class_a', 'pretrip_front_trailer_box_class_a',
            'pretrip_passenger_side_trailer_box_class_a', 'pretrip_vehicle_or_tractor_rear_class_a'
        ).get(test_id=1)

        return obj


# class B Detail
class PreTripClassBDetailView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = PreTripSerializerClassB

    queryset = PreTripClassB.objects.none()

    def get_object(self):
        test_id = self.kwargs['test_id']
        student_id = self.kwargs['student_id']
        try:
            obj = PreTripClassB.objects.select_related(
                'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
                'test__student__student_info__group', 'pretrip_insidecab_class_b',
                'pretrip_coals_class_b', 'pretrip_cargo_area_class_b',
                'pretrip_posttrip_class_b', 'pretrip_vehicle_front_class_b',
                'pretrip_both_sides_vehicle_class_b', 'pretrip_driver_side_box_class_b',
                'pretrip_engine_compartment_class_b', 'pretrip_box_header_board_class_b',
                'pretrip_passenger_side_box_class_b', 'pretrip_vehicle_or_tractor_rear_class_b'
            ).get(test_id=test_id)
        except PreTripClassB.DoesNotExist:
            obj = PreTripClassB.objects.create(test_id=test_id)
        return obj


# class C Detail
class PreTripClassCDetailView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = PreTripSerializerClassC

    queryset = PreTripClassC.objects.none()

    def get_object(self):
        test_id = self.kwargs['test_id']
        student_id = self.kwargs['student_id']
        try:
            obj = PreTripClassC.objects.select_related(
                'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
                'test__student__student_info__group', 'pretrip_insidecab_class_c',
                'pretrip_cargo_area_class_c', 'pretrip_posttrip_class_c',
                'pretrip_vehicle_front_class_c', 'pretrip_both_sides_vehicle_class_c',
                'pretrip_engine_compartment_class_c', 'pretrip_vehicle_rear_class_c'
            ).get(test_id=test_id)
        except PreTripClassC.DoesNotExist:
            obj = PreTripClassC.objects.create(test_id=test_id)
        return obj


# class P Detail
class PreTripClassPDetailView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = PreTripSerializerClassP

    queryset = PreTripClassP.objects.none()

    def get_object(self):
        test_id = self.kwargs['test_id']
        student_id = self.kwargs['student_id']
        try:
            obj = PreTripClassP.objects.select_related(
                'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
                'test__student__student_info__group', 'pretrip_insidecab_class_p',
                'pretrip_coals_class_p', 'pretrip_engine_compartment_class_p',
                'pretrip_vehicle_front_class_p', 'pretrip_both_sides_vehicle_class_p',
                'pretrip_handycap_class_p', 'pretrip_rear_of_vehicle_class_p', 'pretrip_posttrip_class_p'
            ).get(test_id=test_id)
        except PreTripClassP.DoesNotExist:
            obj = PreTripClassP.objects.create(test_id=test_id)
        return obj


class PreTripClassPDetailViewWithInsructions(RetrieveAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = PreTripSerializerClassP

    queryset = PreTripClassP.objects.none()

    def get_object(self):
        test_id = self.kwargs['test_id']
        student_id = self.kwargs['student_id']
        try:
            obj = PreTripClassP.objects.select_related(
                'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
                'test__student__student_info__group', 'pretrip_insidecab_class_p',
                'pretrip_coals_class_p', 'pretrip_engine_compartment_class_p',
                'pretrip_vehicle_front_class_p', 'pretrip_both_sides_vehicle_class_p',
                'pretrip_handycap_class_p', 'pretrip_rear_of_vehicle_class_p', 'pretrip_posttrip_class_p'
            ).get(test_id=test_id)
        except PreTripClassP.DoesNotExist:
            obj = PreTripClassP.objects.create(test_id=test_id)
        return obj


# BUS Detail
class PreTripBusDetailView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = PreTripSerializerBus

    queryset = PreTripBus.objects.none()

    def get_object(self):
        test_id = self.kwargs['test_id']
        student_id = self.kwargs['student_id']
        try:
            obj = PreTripBus.objects.select_related(
                'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
                'test__student__student_info__group', 'pretrip_insidecab_bus',
                'pretrip_coals_bus', 'pretrip_engine_compartment_bus',
                'pretrip_vehicle_front_bus', 'pretrip_both_sides_vehicle_bus',
                'pretrip_handycap_bus', 'pretrip_rear_of_vehicle_bus', 'pretrip_posttrip_bus'
            ).get(test_id=test_id)
        except PreTripBus.DoesNotExist:
            obj = PreTripBus.objects.create(test_id=test_id)
        return obj


# probability graph views
FACTOR_DATA_PRETRIPS = {
    'inside_cab': {
        'title': '',
        'possible_points': 0,
        'received_points': 0,
        'percentage': 0
    },
    'coals': {
        'title': '',
        'possible_points': 0,
        'received_points': 0,
        'percentage': 0
    },
    'engine_compartment': {
        'title': '',
        'possible_points': 0,
        'received_points': 0,
        'percentage': 0
    },
    'vehicle_front': {
        'title': '',
        'possible_points': 0,
        'received_points': 0,
        'percentage': 0
    },
    'both_sides_vehicle': {
        'title': '',
        'possible_points': 0,
        'received_points': 0,
        'percentage': 0
    },
    'vehicle_or_tractor_rear': {
        'title': '',
        'possible_points': 0,
        'received_points': 0,
        'percentage': 0
    },
    'front_of_trailer_box': {
        'title': '',
        'possible_points': 0,
        'received_points': 0,
        'percentage': 0
    },
    'driver_side_trailer_or_box': {
        'title': '',
        'possible_points': 0,
        'received_points': 0,
        'percentage': 0
    },
    'rear_trailer_and_box': {
        'title': '',
        'possible_points': 0,
        'received_points': 0,
        'percentage': 0
    },
    'passenger_side_trailer_or_box': {
        'title': '',
        'possible_points': 0,
        'received_points': 0,
        'percentage': 0
    },
    'dolly': {
        'title': '',
        'possible_points': 0,
        'received_points': 0,
        'percentage': 0
    },
    'post_trip': {
        'title': '',
        'possible_points': 0,
        'received_points': 0,
        'percentage': 0
    },
}


class FactorDataPreTripsAPiView(APIView):
    @property
    def factor_data_pretrips(self):
        return {
            'inside_cab': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'coals': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'engine_compartment': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'vehicle_front': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'both_sides_vehicle': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'vehicle_or_tractor_rear': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'front_of_trailer_box': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'driver_side_trailer_or_box': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'rear_trailer_and_box': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'passenger_side_trailer_or_box': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'dolly': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
            'post_trip': {
                'title': '',
                'possible_points': 0,
                'received_points': 0,
                'percentage': 0
            },
        }


class PreTripClassAProbabilityGraph(FactorDataPreTripsAPiView):
    def get(self, request, *args, **kwargs):
        student_id = kwargs['student_id']
        test_id = kwargs['test_id']
        from safe_driver.models import FACTOR_CHOICES_PRETRIPS, AccidentProbabilityValuePreTripClassA
        # test_id = request.kwargs['test_id']

        class_factors = AccidentProbabilityValuePreTripClassA.objects.values('key', 'field_name', 'value', )
        # base_total = AccidentProbabilityValueBTWClassA.objects.values_list('key').aggregate(sum=Sum('key'))
        # print(base_total)
        class_factors_list = list(class_factors)

        obj = PreTripClassA.objects.select_related(
            'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
            'test__student__student_info__group', 'pretrip_insidecab_class_a',
            'pretrip_coals_class_a', 'pretrip_dolly_class_a',
            'pretrip_posttrip_class_a', 'pretrip_vehicle_front_class_a',
            'pretrip_both_sides_vehicle_class_a', 'pretrip_driver_side_trailer_box_class_a',
            'pretrip_engine_compartment_class_a', 'pretrip_front_trailer_box_class_a',
            'pretrip_passenger_side_trailer_box_class_a', 'pretrip_vehicle_or_tractor_rear_class_a'
        ).get(test_id=test_id)
        fields_list = []
        factor_data_pretrips = self.factor_data_pretrips
        model_fields = obj._meta.get_fields()
        for field in model_fields:
            related_model = obj._meta.get_field(field.name).related_model

            if related_model:
                model_name = related_model._meta.verbose_name.title()

                related_fields = related_model._meta.get_fields()

                if related_fields:
                    model_data = {
                        'title': model_name,
                        'data': []
                    }
                    for rel_field in related_fields:
                        if rel_field.get_internal_type() == 'IntegerField':
                            # print(rel_field.__dict__)
                            value = getattr(obj, field.name, rel_field.name).__dict__[rel_field.name]
                            factors = []
                            factor_items = [factor for factor in class_factors_list if
                                            factor['field_name'] == rel_field.name]
                            for item in factor_items:
                                # print(item)
                                factor_value = value * item['value']
                                factor_data_pretrips[item['key']]['received_points'] += factor_value
                                factor_data_pretrips[item['key']]['possible_points'] += item['value'] * 5
                                factors.append({
                                    'value': item['value'],
                                    item['key']: factor_value
                                })

                            model_data['data'].append({
                                'name': rel_field.verbose_name.title(),
                                'field': rel_field.name,
                                'value': value,
                                'factors': factors
                            })
                    if len(model_data['data']) > 0:
                        fields_list.append(model_data)

        for value, name in FACTOR_CHOICES_PRETRIPS:
            # print(value)
            possible_points = factor_data_pretrips[value]['possible_points']
            received_points = factor_data_pretrips[value]['received_points']
            factor_data_pretrips[value]['title'] = name
            if possible_points > 0 and received_points > 0:
                percentage = '{:.2f}'.format((100 / possible_points) * received_points)
                # percentage = round((100 / possible_points) * received_points, 2)
                factor_data_pretrips[value]['percentage'] = percentage
        results = {
            'chart_data': factor_data_pretrips,
            'fields': fields_list
        }
        return Response(results)


class PreTripClassBProbabilityGraph(FactorDataPreTripsAPiView):
    def get(self, request, *args, **kwargs):
        student_id = kwargs['student_id']
        test_id = kwargs['test_id']
        from safe_driver.models import FACTOR_CHOICES_PRETRIPS, AccidentProbabilityValuePreTripClassB
        # test_id = request.kwargs['test_id']
        class_factors = AccidentProbabilityValuePreTripClassB.objects.values('key', 'field_name', 'value', )

        # print(list(class_factors))
        class_factors_list = list(class_factors)

        obj = PreTripClassB.objects.select_related(
            'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
            'test__student__student_info__group', 'pretrip_insidecab_class_b',
            'pretrip_coals_class_b', 'pretrip_cargo_area_class_b',
            'pretrip_posttrip_class_b', 'pretrip_vehicle_front_class_b',
            'pretrip_both_sides_vehicle_class_b', 'pretrip_driver_side_box_class_b',
            'pretrip_engine_compartment_class_b', 'pretrip_box_header_board_class_b',
            'pretrip_passenger_side_box_class_b', 'pretrip_vehicle_or_tractor_rear_class_b'
        ).get(test_id=test_id)
        fields_list = []
        factor_data_pretrips = self.factor_data_pretrips

        model_fields = obj._meta.get_fields()
        for field in model_fields:
            related_model = obj._meta.get_field(field.name).related_model

            if related_model:
                model_name = related_model._meta.verbose_name.title()

                related_fields = related_model._meta.get_fields()

                if related_fields:
                    model_data = {
                        'title': model_name,
                        'data': []
                    }
                    for rel_field in related_fields:
                        if rel_field.get_internal_type() == 'IntegerField':
                            # print(rel_field.__dict__)
                            value = getattr(obj, field.name, rel_field.name).__dict__[rel_field.name]
                            factors = []
                            factor_items = [factor for factor in class_factors_list if
                                            factor['field_name'] == rel_field.name]
                            for item in factor_items:
                                factor_value = value * item['value']
                                factor_data_pretrips[item['key']]['received_points'] += factor_value
                                factor_data_pretrips[item['key']]['possible_points'] += item['value'] * 5
                                factors.append({
                                    'value': item['value'],
                                    item['key']: factor_value
                                })

                            model_data['data'].append({
                                'name': rel_field.verbose_name.title(),
                                'field': rel_field.name,
                                'value': value,
                                'factors': factors
                            })
                    if len(model_data['data']) > 0:
                        fields_list.append(model_data)

        for value, name in FACTOR_CHOICES_PRETRIPS:
            possible_points = factor_data_pretrips[value]['possible_points']
            received_points = factor_data_pretrips[value]['received_points']
            factor_data_pretrips[value]['title'] = name
            if possible_points > 0 and received_points > 0:
                percentage = '{:.2f}'.format((100 / possible_points) * received_points)
                # percentage = round((100 / possible_points) * received_points, 2)
                factor_data_pretrips[value]['percentage'] = percentage
        results = {
            'chart_data': factor_data_pretrips,
            'fields': fields_list
        }
        return Response(results)


class PreTripClassCProbabilityGraph(FactorDataPreTripsAPiView):

    def get(self, request, *args, **kwargs):
        student_id = kwargs['student_id']
        test_id = kwargs['test_id']
        from safe_driver.models import FACTOR_CHOICES_PRETRIPS, AccidentProbabilityValuePreTripClassC
        # test_id = request.kwargs['test_id']
        class_factors = AccidentProbabilityValuePreTripClassC.objects.values('key', 'field_name', 'value', )
        # print(list(class_factors))
        class_factors_list = list(class_factors)

        obj = PreTripClassC.objects.select_related(
            'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
            'test__student__student_info__group', 'pretrip_insidecab_class_c',
            'pretrip_cargo_area_class_c', 'pretrip_posttrip_class_c',
            'pretrip_vehicle_front_class_c', 'pretrip_both_sides_vehicle_class_c',
            'pretrip_engine_compartment_class_c', 'pretrip_vehicle_rear_class_c'
        ).get(test_id=test_id)
        fields_list = []
        factor_data_pretrips = self.factor_data_pretrips

        model_fields = obj._meta.get_fields()
        for field in model_fields:
            related_model = obj._meta.get_field(field.name).related_model

            if related_model:
                model_name = related_model._meta.verbose_name.title()

                related_fields = related_model._meta.get_fields()

                if related_fields:
                    model_data = {
                        'title': model_name,
                        'data': []
                    }
                    for rel_field in related_fields:
                        if rel_field.get_internal_type() == 'IntegerField':
                            # print(rel_field.__dict__)
                            value = getattr(obj, field.name, rel_field.name).__dict__[rel_field.name]
                            factors = []
                            factor_items = [factor for factor in class_factors_list if
                                            factor['field_name'] == rel_field.name]
                            for item in factor_items:
                                factor_value = value * item['value']
                                factor_data_pretrips[item['key']]['received_points'] += factor_value
                                factor_data_pretrips[item['key']]['possible_points'] += item['value'] * 5
                                factors.append({
                                    'value': item['value'],
                                    item['key']: factor_value
                                })
                            model_data['data'].append({
                                'name': rel_field.verbose_name.title(),
                                'field': rel_field.name,
                                'value': value,
                                'factors': factors
                            })
                    if len(model_data['data']) > 0:
                        fields_list.append(model_data)

        for value, name in FACTOR_CHOICES_PRETRIPS:
            possible_points = factor_data_pretrips[value]['possible_points']
            received_points = factor_data_pretrips[value]['received_points']
            factor_data_pretrips[value]['title'] = name
            if possible_points > 0 and received_points > 0:
                percentage = '{:.2f}'.format((100 / possible_points) * received_points)
                # percentage = round((100 / possible_points) * received_points, 2)
                factor_data_pretrips[value]['percentage'] = percentage
        results = {
            'chart_data': factor_data_pretrips,
            'fields': fields_list
        }
        return Response(results)


class PreTripBusProbabilityGraph(FactorDataPreTripsAPiView):
    def get(self, request, *args, **kwargs):
        student_id = kwargs['student_id']
        test_id = kwargs['test_id']
        from safe_driver.models import FACTOR_CHOICES_PRETRIPS, AccidentProbabilityValuePreTripBus
        # test_id = request.kwargs['test_id']
        class_factors = AccidentProbabilityValuePreTripBus.objects.values('key', 'field_name', 'value', )
        # print(list(class_factors))
        class_factors_list = list(class_factors)

        obj = PreTripBus.objects.select_related(
            'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
            'test__student__student_info__group', 'pretrip_insidecab_bus',
            'pretrip_coals_bus', 'pretrip_engine_compartment_bus',
            'pretrip_vehicle_front_bus', 'pretrip_both_sides_vehicle_bus',
            'pretrip_handycap_bus', 'pretrip_rear_of_vehicle_bus', 'pretrip_posttrip_bus'
        ).get(test_id=test_id)
        fields_list = []
        factor_data_pretrips = self.factor_data_pretrips

        model_fields = obj._meta.get_fields()
        for field in model_fields:
            related_model = obj._meta.get_field(field.name).related_model

            if related_model:
                model_name = related_model._meta.verbose_name.title()

                related_fields = related_model._meta.get_fields()

                if related_fields:
                    model_data = {
                        'title': model_name,
                        'data': []
                    }
                    for rel_field in related_fields:
                        if rel_field.get_internal_type() == 'IntegerField':
                            # print(rel_field.__dict__)
                            value = getattr(obj, field.name, rel_field.name).__dict__[rel_field.name]
                            factors = []
                            factor_items = [factor for factor in class_factors_list if
                                            factor['field_name'] == rel_field.name]
                            for item in factor_items:
                                factor_value = value * item['value']
                                factor_data_pretrips[item['key']]['received_points'] += factor_value
                                factor_data_pretrips[item['key']]['possible_points'] += item['value'] * 5
                                factors.append({
                                    'value': item['value'],
                                    item['key']: factor_value
                                })

                            model_data['data'].append({
                                'name': rel_field.verbose_name.title(),
                                'field': rel_field.name,
                                'value': value,
                                'factors': factors
                            })
                    if len(model_data['data']) > 0:
                        fields_list.append(model_data)

        for value, name in FACTOR_CHOICES_PRETRIPS:
            possible_points = factor_data_pretrips[value]['possible_points']
            received_points = factor_data_pretrips[value]['received_points']
            factor_data_pretrips[value]['title'] = name
            if possible_points > 0 and received_points > 0:
                percentage = '{:.2f}'.format((100 / possible_points) * received_points)
                # percentage = round((100 / possible_points) * received_points, 2)
                factor_data_pretrips[value]['percentage'] = percentage
        results = {
            'chart_data': factor_data_pretrips,
            'fields': fields_list
        }
        return Response(results)


class PreTripClassPProbabilityGraph(FactorDataPreTripsAPiView):

    def get(self, request, *args, **kwargs):
        student_id = kwargs['student_id']
        test_id = kwargs['test_id']
        from safe_driver.models import FACTOR_CHOICES_PRETRIPS, AccidentProbabilityValuePreTripClassP
        # test_id = request.kwargs['test_id']
        class_factors = AccidentProbabilityValuePreTripClassP.objects.values('key', 'field_name', 'value', )
        # print(list(class_factors))
        class_factors_list = list(class_factors)

        obj = PreTripClassP.objects.select_related(
            'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
            'test__student__student_info__group', 'pretrip_insidecab_class_p',
            'pretrip_coals_class_p', 'pretrip_engine_compartment_class_p',
            'pretrip_vehicle_front_class_p', 'pretrip_both_sides_vehicle_class_p',
            'pretrip_handycap_class_p', 'pretrip_rear_of_vehicle_class_p', 'pretrip_posttrip_class_p'
        ).get(test_id=test_id)
        fields_list = []
        factor_data_pretrips = self.factor_data_pretrips

        model_fields = obj._meta.get_fields()
        for field in model_fields:
            related_model = obj._meta.get_field(field.name).related_model

            if related_model:
                model_name = related_model._meta.verbose_name.title()

                related_fields = related_model._meta.get_fields()

                if related_fields:
                    model_data = {
                        'title': model_name,
                        'data': []
                    }
                    for rel_field in related_fields:
                        if rel_field.get_internal_type() == 'IntegerField':
                            # print(rel_field.__dict__)
                            value = getattr(obj, field.name, rel_field.name).__dict__[rel_field.name]
                            factors = []
                            factor_items = [factor for factor in class_factors_list if
                                            factor['field_name'] == rel_field.name]
                            for item in factor_items:
                                factor_value = value * item['value']
                                factor_data_pretrips[item['key']]['received_points'] += factor_value
                                factor_data_pretrips[item['key']]['possible_points'] += item['value'] * 5
                                factors.append({
                                    'value': item['value'],
                                    item['key']: factor_value
                                })

                            model_data['data'].append({
                                'name': rel_field.verbose_name.title(),
                                'field': rel_field.name,
                                'value': value,
                                'factors': factors
                            })
                    if len(model_data['data']) > 0:
                        fields_list.append(model_data)
        for value, name in FACTOR_CHOICES_PRETRIPS:
            possible_points = factor_data_pretrips[value]['possible_points']
            received_points = factor_data_pretrips[value]['received_points']
            factor_data_pretrips[value]['title'] = name
            if possible_points > 0 and received_points > 0:
                percentage = '{:.2f}'.format((100 / possible_points) * received_points)
                # percentage = round((100 / possible_points) * received_points, 2)
                factor_data_pretrips[value]['percentage'] = percentage
        results = {
            'chart_data': factor_data_pretrips,
            'fields': fields_list
        }
        return Response(results)
