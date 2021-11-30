from operator import itemgetter
from django.db.models import Sum
# from django.urls import reverse
from rest_framework.reverse import reverse
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from safe_driver.models import BTWBus, BTWClassP
from users.api.v1.permissions import InstructorPermission
from .serializers import *

# Class A Detail
from .serializers.btw_bus_serializers import BTWBusSerializer
from .serializers.btw_class_p_serializers import BTWClassPSerializer
from ..functions import RequestMixinAPIView
from ..mixins import FactorAPIView


class BTWClassList(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    @staticmethod
    def get(request, *args, **kwargs):
        url_kwargs = {'student_id': kwargs.get('student_id'), 'test_id': kwargs.get('test_id')}
        class_a_url = reverse('api_v1:safe_driver:student_btw_class_a_detail', kwargs=url_kwargs, request=request)
        class_b_url = reverse('api_v1:safe_driver:student_btw_class_b_detail', kwargs=url_kwargs, request=request)
        class_c_url = reverse('api_v1:safe_driver:student_btw_class_c_detail', kwargs=url_kwargs, request=request)
        bus_url = reverse('api_v1:safe_driver:student_btw_bus_detail', kwargs=url_kwargs, request=request)
        data = {
            'class_a': class_a_url,
            'class_b': class_b_url,
            'class_c': class_c_url,
            'bus': bus_url,
        }
        return Response(data)


class BTWClassADetailView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = BTWClassASerializer

    queryset = BTWClassA.objects.none()

    def get_object(self):
        test_id = self.kwargs['test_id']
        student_id = self.kwargs['student_id']
        try:
            obj = BTWClassA.objects.select_related(
                'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
                'test__student__student_info__group', 'btw_cab_safety_class_a',
                'btw_start_engine_class_a', 'btw_engine_operation_class_a',
                'btw_clutch_and_transmission_class_a', 'btw_coupling_class_a',
                'btw_uncoupling_class_a', 'btw_brakes_and_stopping_class_a',
                'btw_eye_movement_and_mirror_class_a', 'btw_recognizes_hazards_class_a',
                'btw_lights_and_signals_class_a', 'btw_steering_class_a',
                'btw_backing_class_a', 'btw_speed_class_a',
                'btw_intersections_class_a', 'btw_turning_class_a',
                'btw_parking_class_a', 'btw_multiple_trailers_class_a',
                'btw_hills_class_a', 'btw_passing_class_a',
                'btw_general_safety_and_dot_adherence_class_a',
            ).get(test_id=test_id)
            # obj = BTWClassA.objects.get(test_id=test_id, test__student_id=student_id)
        except BTWClassA.DoesNotExist:
            obj = BTWClassA.objects.create(test_id=test_id)

        # print(obj.btw_cab_safety_class_a.possible_points)
        return obj


# Class B Detail
class BTWClassBDetailView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = BTWClassBSerializer

    queryset = BTWClassB.objects.none()

    def get_object(self):
        test_id = self.kwargs['test_id']
        student_id = self.kwargs['student_id']
        try:
            obj = BTWClassB.objects.select_related(
                'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
                'test__student__student_info__group', 'btw_cab_safety_class_b',
                'btw_start_engine_class_b', 'btw_engine_operation_class_b',
                'btw_clutch_and_transmission_class_b', 'btw_brakes_and_stoppings_class_b',
                'btw_eye_movement_and_mirror_class_b', 'btw_recognizes_hazards_class_b',
                'btw_lights_and_signals_class_b', 'btw_steering_class_b',
                'btw_backing_class_b', 'btw_speed_class_b',
                'btw_intersections_class_b', 'btw_turning_class_b',
                'btw_parking_class_b',
                'btw_hills_class_b', 'btw_passing_class_b',
                'btw_general_safety_and_dot_adherence_class_b',
            ).get(test_id=test_id)
            # obj = BTWClassA.objects.get(test_id=test_id, test__student_id=student_id)
        except BTWClassB.DoesNotExist:
            obj = BTWClassB.objects.create(test_id=test_id)
        return obj


# Class C Detail
class BTWClassCDetailView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = BTWClassCSerializer

    queryset = BTWClassC.objects.none()

    def get_object(self):
        test_id = self.kwargs['test_id']
        student_id = self.kwargs['student_id']
        try:
            obj = BTWClassC.objects.select_related(
                'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
                'test__student__student_info__group', 'btw_cab_safety_class_c',
                'btw_start_engine_class_c', 'btw_engine_operation_class_c',
                'btw_clutch_and_transmission_class_c', 'btw_brakes_and_stoppings_class_c',
                'btw_eye_movement_and_mirror_class_c', 'btw_recognizes_hazards_class_c',
                'btw_lights_and_signals_class_c', 'btw_steering_class_c',
                'btw_backing_class_c', 'btw_speed_class_c',
                'btw_intersections_class_c', 'btw_turning_class_c',
                'btw_parking_class_c',
                'btw_hills_class_c', 'btw_passing_class_c',
                'btw_general_safety_and_dot_adherence_class_c',
            ).get(test_id=test_id)
            # obj = BTWClassA.objects.get(test_id=test_id, test__student_id=student_id)
        except BTWClassC.DoesNotExist:
            obj = BTWClassC.objects.create(test_id=test_id)
        return obj


# BTW Class P Detail UpdateA
class BTWClassPDetailView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = BTWClassPSerializer

    queryset = BTWClassP.objects.none()

    def get_serializer_context(self):
        context = super(self.__class__, self).get_serializer_context()
        context.update({"request": self.request})
        return context

    # def get_serializer(self, *args, **kwargs):
    #     return BTWBusSerializer(context={"request": self.request})

    # def get_serializer_class(self):
    #     return self.serializer_class(context={"request": self.request})

    def get_object(self):
        test_id = self.kwargs['test_id']
        student_id = self.kwargs['student_id']
        try:
            obj = BTWClassP.objects.select_related(
                'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
                'test__student__student_info__group', 'btw_cab_safety_class_p',
                'btw_start_engine_class_p', 'btw_engine_operation_class_p',
                'btw_passenger_safety_class_p', 'btw_brakes_and_stopping_class_p',
                'btw_eye_movement_and_mirror_class_p', 'btw_recognizes_hazards_class_p',
                'btw_lights_and_signals_class_p', 'btw_steering_class_p',
                'btw_backing_class_p', 'btw_speed_class_p', 'btw_intersections_class_p', 'btw_turning_class_p',
                'btw_parking_class_p', 'btw_hills_class_p', 'btw_passing_class_p', 'btw_railroad_crossing_class_p',
                'btw_general_safety_class_p', 'btw_internal_environment_class_p', 'test__student__student_info__company'
            ).get(test_id=test_id)
            # obj = BTWClassA.objects.get(test_id=test_id, test__student_id=student_id)
        except BTWClassP.DoesNotExist:
            obj = BTWClassP.objects.create(test_id=test_id)
        return obj


# BTW Bus Detail UpdateA
class BTWBusDetailView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = BTWBusSerializer

    queryset = BTWBus.objects.none()

    def get_serializer_context(self):
        context = super(BTWBusDetailView, self).get_serializer_context()
        context.update({"request": self.request})
        return context

    # def get_serializer(self, *args, **kwargs):
    #     return BTWBusSerializer(context={"request": self.request})

    # def get_serializer_class(self):
    #     return self.serializer_class(context={"request": self.request})

    def get_object(self):
        test_id = self.kwargs['test_id']
        student_id = self.kwargs['student_id']
        try:
            obj = BTWBus.objects.select_related(
                'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
                'test__student__student_info__group', 'btw_cab_safety_bus',
                'btw_start_engine_bus', 'btw_engine_operation_bus',
                'btw_passenger_safety_bus', 'btw_brakes_and_stopping_bus',
                'btw_eye_movement_and_mirror_bus', 'btw_recognizes_hazards_bus',
                'btw_lights_and_signals_bus', 'btw_steering_bus',
                'btw_backing_bus', 'btw_speed_bus', 'btw_intersections_bus', 'btw_turning_bus', 'btw_parking_bus',
                'btw_hills_bus', 'btw_passing_bus', 'btw_railroad_crossing_bus', 'btw_general_safety_bus',
                'btw_internal_environment_bus',
                'test__student__student_info__company'
            ).get(test_id=test_id)
            # obj = BTWClassA.objects.get(test_id=test_id, test__student_id=student_id)
        except BTWBus.DoesNotExist:
            obj = BTWBus.objects.create(test_id=test_id)
        return obj

    # def retrieve(self, request, *args, **kwargs):
    #     # from django.db import connection, reset_queries
    #     # print(len(connection.queries))
    #     return super(BTWBusDetailView, self).retrieve(request, *args, **kwargs)


class BTWClassAFactors(FactorAPIView):
    def get(self, request, *args, **kwargs):
        student_id = kwargs['student_id']
        test_id = kwargs['test_id']
        from safe_driver.models import FACTOR_CHOICES, AccidentProbabilityValueBTWClassA
        # test_id = request.kwargs['test_id']

        class_factors = AccidentProbabilityValueBTWClassA.objects.values('key', 'field_name', 'value', )
        # base_total = AccidentProbabilityValueBTWClassA.objects.values_list('key').aggregate(sum=Sum('key'))
        # print(base_total)
        class_factors_list = list(class_factors)

        obj = BTWClassA.objects.select_related(
            'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
            'test__student__student_info__group', 'btw_cab_safety_class_a',
            'btw_start_engine_class_a', 'btw_engine_operation_class_a',
            'btw_clutch_and_transmission_class_a', 'btw_coupling_class_a',
            'btw_uncoupling_class_a', 'btw_brakes_and_stopping_class_a',
            'btw_eye_movement_and_mirror_class_a', 'btw_recognizes_hazards_class_a',
            'btw_lights_and_signals_class_a', 'btw_steering_class_a',
            'btw_backing_class_a', 'btw_speed_class_a',
            'btw_intersections_class_a', 'btw_turning_class_a',
            'btw_parking_class_a', 'btw_multiple_trailers_class_a',
            'btw_hills_class_a', 'btw_passing_class_a',
            'btw_general_safety_and_dot_adherence_class_a',
        ).get(test_id=test_id)
        fields_list = []
        factor_data = self.factor_data
        model_fields = obj._meta.get_fields()

        total_possible_points = 0
        total_received_points = 0

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
                            # print(value)
                            factors = []
                            factor_items = [factor for factor in class_factors_list if
                                            factor['field_name'] == rel_field.name]
                            for item in factor_items:
                                # print(item)
                                factor_value = value * item['value']
                                factor_data[item['key']]['received_points'] += factor_value
                                # factor_data[item['key']]['possible_points'] += item['value'] * 5
                                total_received_points += factor_value
                                if value > 0:
                                    factor_data[item['key']]['possible_points'] += item['value'] * 5
                                    total_possible_points += item['value'] * 5
                                else:
                                    factor_data[item['key']]['possible_points'] += 0
                                    total_possible_points += 0
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

        for value, name in FACTOR_CHOICES:
            possible_points = factor_data[value]['possible_points']
            received_points = factor_data[value]['received_points']
            factor_data[value]['title'] = name
            if possible_points > 0 and received_points > 0:
                percentage = '{:.2f}'.format((100 / possible_points) * received_points)
                # percentage = round((100 / possible_points) * received_points, 2)
                factor_data[value]['percentage'] = percentage

            if total_received_points > 0 and received_points > 0:
                new_value = total_received_points / received_points
                new_percentage = (new_value / total_received_points) * 100
                factor_data[value]['new_value'] = '{:.2f}'.format(new_value)
                factor_data[value]['new_percentage'] = '{:.2f}'.format(new_percentage)
            else:
                factor_data[value]['new_value'] = 0
                factor_data[value]['new_percentage'] = 0

        results = {
            'total_possible_points': total_possible_points,
            'total_received_points': total_received_points,
            'chart_data': factor_data,
            'fields': fields_list
        }
        return Response(results)


class BTWClassBFactors(FactorAPIView):
    def get(self, request, *args, **kwargs):
        student_id = kwargs['student_id']
        test_id = kwargs['test_id']
        from safe_driver.models import FACTOR_CHOICES, AccidentProbabilityValueBTWClassB
        # test_id = request.kwargs['test_id']
        class_factors = AccidentProbabilityValueBTWClassB.objects.values('key', 'field_name', 'value', )

        # print(list(class_factors))
        class_factors_list = list(class_factors)

        obj = BTWClassB.objects.select_related(
            'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
            'test__student__student_info__group', 'btw_cab_safety_class_b',
            'btw_start_engine_class_b', 'btw_engine_operation_class_b',
            'btw_clutch_and_transmission_class_b', 'btw_brakes_and_stoppings_class_b',
            'btw_eye_movement_and_mirror_class_b', 'btw_recognizes_hazards_class_b',
            'btw_lights_and_signals_class_b', 'btw_steering_class_b',
            'btw_backing_class_b', 'btw_speed_class_b',
            'btw_intersections_class_b', 'btw_turning_class_b',
            'btw_parking_class_b',
            'btw_hills_class_b', 'btw_passing_class_b',
            'btw_general_safety_and_dot_adherence_class_b',
        ).get(test_id=test_id)
        fields_list = []
        factor_data = self.factor_data
        model_fields = obj._meta.get_fields()
        total_possible_points = 0
        total_received_points = 0

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
                            # print(value)
                            factors = []
                            factor_items = [factor for factor in class_factors_list if
                                            factor['field_name'] == rel_field.name]
                            for item in factor_items:
                                # print(item)
                                factor_value = value * item['value']
                                factor_data[item['key']]['received_points'] += factor_value
                                # factor_data[item['key']]['possible_points'] += item['value'] * 5
                                total_received_points += factor_value
                                if value > 0:
                                    factor_data[item['key']]['possible_points'] += item['value'] * 5
                                    total_possible_points += item['value'] * 5
                                else:
                                    factor_data[item['key']]['possible_points'] += 0
                                    total_possible_points += 0
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

        for value, name in FACTOR_CHOICES:
            possible_points = factor_data[value]['possible_points']
            received_points = factor_data[value]['received_points']
            factor_data[value]['title'] = name
            if possible_points > 0 and received_points > 0:
                percentage = '{:.2f}'.format((100 / possible_points) * received_points)
                # percentage = round((100 / possible_points) * received_points, 2)
                factor_data[value]['percentage'] = percentage

            if total_received_points > 0 and received_points > 0:
                new_value = total_received_points / received_points
                new_percentage = (new_value / total_received_points) * 100
                factor_data[value]['new_value'] = '{:.2f}'.format(new_value)
                factor_data[value]['new_percentage'] = '{:.2f}'.format(new_percentage)
            else:
                factor_data[value]['new_value'] = 0
                factor_data[value]['new_percentage'] = 0

        results = {
            'total_possible_points': total_possible_points,
            'total_received_points': total_received_points,
            'chart_data': factor_data,
            'fields': fields_list
        }
        return Response(results)


class BTWClassCFactors(FactorAPIView):
    def get(self, request, *args, **kwargs):
        student_id = kwargs['student_id']
        test_id = kwargs['test_id']
        from safe_driver.models import FACTOR_CHOICES, AccidentProbabilityValueBTWClassC
        # test_id = request.kwargs['test_id']
        class_factors = AccidentProbabilityValueBTWClassC.objects.values('key', 'field_name', 'value', )
        # print(list(class_factors))
        class_factors_list = list(class_factors)

        obj = BTWClassC.objects.select_related(
            'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
            'test__student__student_info__group', 'btw_cab_safety_class_c',
            'btw_start_engine_class_c', 'btw_engine_operation_class_c',
            'btw_clutch_and_transmission_class_c', 'btw_brakes_and_stoppings_class_c',
            'btw_eye_movement_and_mirror_class_c', 'btw_recognizes_hazards_class_c',
            'btw_lights_and_signals_class_c', 'btw_steering_class_c',
            'btw_backing_class_c', 'btw_speed_class_c',
            'btw_intersections_class_c', 'btw_turning_class_c',
            'btw_parking_class_c',
            'btw_hills_class_c', 'btw_passing_class_c',
            'btw_general_safety_and_dot_adherence_class_c',
        ).get(test_id=test_id)
        fields_list = []
        factor_data = self.factor_data

        model_fields = obj._meta.get_fields()
        total_possible_points = 0
        total_received_points = 0

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
                            # print(value)
                            factors = []
                            factor_items = [factor for factor in class_factors_list if
                                            factor['field_name'] == rel_field.name]
                            for item in factor_items:
                                # print(item)
                                factor_value = value * item['value']
                                factor_data[item['key']]['received_points'] += factor_value
                                # factor_data[item['key']]['possible_points'] += item['value'] * 5
                                total_received_points += factor_value
                                if value > 0:
                                    factor_data[item['key']]['possible_points'] += item['value'] * 5
                                    total_possible_points += item['value'] * 5
                                else:
                                    factor_data[item['key']]['possible_points'] += 0
                                    total_possible_points += 0
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

        for value, name in FACTOR_CHOICES:
            possible_points = factor_data[value]['possible_points']
            received_points = factor_data[value]['received_points']
            factor_data[value]['title'] = name
            if possible_points > 0 and received_points > 0:
                percentage = '{:.2f}'.format((100 / possible_points) * received_points)
                # percentage = round((100 / possible_points) * received_points, 2)
                factor_data[value]['percentage'] = percentage

            if total_received_points > 0 and received_points > 0:
                new_value = total_received_points / received_points
                new_percentage = (new_value / total_received_points) * 100
                factor_data[value]['new_value'] = '{:.2f}'.format(new_value)
                factor_data[value]['new_percentage'] = '{:.2f}'.format(new_percentage)
            else:
                factor_data[value]['new_value'] = 0
                factor_data[value]['new_percentage'] = 0

        results = {
            'total_possible_points': total_possible_points,
            'total_received_points': total_received_points,
            'chart_data': factor_data,
            'fields': fields_list
        }
        return Response(results)


# btw class c factors with calculations
# @api_view(['GET'])
class BTWClassPFactors(FactorAPIView):
    def get(self, request, *args, **kwargs):
        student_id = kwargs['student_id']
        test_id = kwargs['test_id']
        from safe_driver.models import FACTOR_CHOICES, AccidentProbabilityValueBTWClassP
        # test_id = request.kwargs['test_id']
        class_factors = AccidentProbabilityValueBTWClassP.objects.values('key', 'field_name', 'value', )
        # print(list(class_factors))
        class_factors_list = list(class_factors)

        obj = BTWClassP.objects.select_related(
            'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
            'test__student__student_info__group', 'btw_cab_safety_class_p',
            'btw_start_engine_class_p', 'btw_engine_operation_class_p',
            'btw_passenger_safety_class_p', 'btw_brakes_and_stopping_class_p',
            'btw_eye_movement_and_mirror_class_p', 'btw_recognizes_hazards_class_p',
            'btw_lights_and_signals_class_p', 'btw_steering_class_p',
            'btw_backing_class_p', 'btw_speed_class_p', 'btw_intersections_class_p', 'btw_turning_class_p',
            'btw_parking_class_p', 'btw_hills_class_p', 'btw_passing_class_p', 'btw_railroad_crossing_class_p',
            'btw_general_safety_class_p', 'btw_internal_environment_class_p', 'test__student__student_info__company'
        ).get(test_id=test_id)
        fields_list = []

        factor_data = self.factor_data
        model_fields = obj._meta.get_fields()
        total_possible_points = 0
        total_received_points = 0

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
                            # print(value)
                            factors = []
                            factor_items = [factor for factor in class_factors_list if
                                            factor['field_name'] == rel_field.name]
                            for item in factor_items:
                                # print(item)
                                factor_value = value * item['value']
                                factor_data[item['key']]['received_points'] += factor_value
                                # factor_data[item['key']]['possible_points'] += item['value'] * 5
                                total_received_points += factor_value
                                if value > 0:
                                    factor_data[item['key']]['possible_points'] += item['value'] * 5
                                    total_possible_points += item['value'] * 5
                                else:
                                    factor_data[item['key']]['possible_points'] += 0
                                    total_possible_points += 0
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

        for value, name in FACTOR_CHOICES:
            possible_points = factor_data[value]['possible_points']
            received_points = factor_data[value]['received_points']
            factor_data[value]['title'] = name
            if possible_points > 0 and received_points > 0:
                percentage = '{:.2f}'.format((100 / possible_points) * received_points)
                # percentage = round((100 / possible_points) * received_points, 2)
                factor_data[value]['percentage'] = percentage

            if total_received_points > 0 and received_points > 0:
                new_value = total_received_points / received_points
                new_percentage = (new_value / total_received_points) * 100
                factor_data[value]['new_value'] = '{:.2f}'.format(new_value)
                factor_data[value]['new_percentage'] = '{:.2f}'.format(new_percentage)
            else:
                factor_data[value]['new_value'] = 0
                factor_data[value]['new_percentage'] = 0

        results = {
            'total_possible_points': total_possible_points,
            'total_received_points': total_received_points,
            'chart_data': factor_data,
            'fields': fields_list
        }
        return Response(results)


class BTWBusFactors(FactorAPIView):
    def get(self, request, *args, **kwargs):
        student_id = kwargs['student_id']
        test_id = kwargs['test_id']
        from safe_driver.models import FACTOR_CHOICES, AccidentProbabilityValueBTWBus
        # test_id = request.kwargs['test_id']
        class_factors = AccidentProbabilityValueBTWBus.objects.values('key', 'field_name', 'value', )
        # print(list(class_factors))
        class_factors_list = list(class_factors)

        obj = BTWBus.objects.select_related(
            'test', 'test__student', 'test__student__student_info', 'test__student__student_info__company',
            'test__student__student_info__group', 'btw_cab_safety_bus',
            'btw_start_engine_bus', 'btw_engine_operation_bus',
            'btw_passenger_safety_bus', 'btw_brakes_and_stopping_bus',
            'btw_eye_movement_and_mirror_bus', 'btw_recognizes_hazards_bus',
            'btw_lights_and_signals_bus', 'btw_steering_bus',
            'btw_backing_bus', 'btw_speed_bus',
            'test__student__student_info__company'
        ).get(test_id=test_id)
        fields_list = []
        factor_data = self.factor_data

        model_fields = obj._meta.get_fields()
        total_possible_points = 0
        total_received_points = 0

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
                            # print(value)
                            factors = []
                            factor_items = [factor for factor in class_factors_list if
                                            factor['field_name'] == rel_field.name]
                            for item in factor_items:
                                # print(item)
                                factor_value = value * item['value']
                                factor_data[item['key']]['received_points'] += factor_value
                                # factor_data[item['key']]['possible_points'] += item['value'] * 5
                                total_received_points += factor_value
                                if value > 0:
                                    factor_data[item['key']]['possible_points'] += item['value'] * 5
                                    total_possible_points += item['value'] * 5
                                else:
                                    factor_data[item['key']]['possible_points'] += 0
                                    total_possible_points += 0
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

        for value, name in FACTOR_CHOICES:
            possible_points = factor_data[value]['possible_points']
            received_points = factor_data[value]['received_points']
            factor_data[value]['title'] = name
            if possible_points > 0 and received_points > 0:
                percentage = '{:.2f}'.format((100 / possible_points) * received_points)
                # percentage = round((100 / possible_points) * received_points, 2)
                factor_data[value]['percentage'] = percentage

            if total_received_points > 0 and received_points > 0:
                new_value = total_received_points / received_points
                new_percentage = (new_value / total_received_points) * 100
                factor_data[value]['new_value'] = '{:.2f}'.format(new_value)
                factor_data[value]['new_percentage'] = '{:.2f}'.format(new_percentage)
            else:
                factor_data[value]['new_value'] = 0
                factor_data[value]['new_percentage'] = 0

        results = {
            'total_possible_points': total_possible_points,
            'total_received_points': total_received_points,
            'chart_data': factor_data,
            'fields': fields_list
        }
        return Response(results)


def btw_class_a_instructions(request, student_id, test_id):
    return Response()
