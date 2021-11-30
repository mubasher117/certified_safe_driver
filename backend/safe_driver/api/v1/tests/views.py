from django.http import Http404
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404, \
    RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from safe_driver.api.v1.swp_serializers import SafeDriveSWPSerializer
from users.api.v1.permissions import InstructorPermission
from safe_driver.api.v1.serializers import StudentTestDetailSerializer, StudentTestListSerializer
from safe_driver.models import StudentTest, SafeDriveSWP
from .serializers import *


class StudentTestListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = StudentTestListSerializer

    queryset = StudentTest.objects.all()

    def get_queryset(self):
        return StudentTest.objects.filter(student_id=self.kwargs.get('student_id')) \
            .select_related('student', 'student_test_info', 'student__student_info', 'instructor',
                            'student__student_info__company', 'student__student_info__group',
                            'student_test_info__instructor').prefetch_related(
            'student__student_info__company__instructors', ).order_by('-created')

    def perform_create(self, serializer):
        serializer.save(student_id=self.kwargs.get('student_id'), instructor=self.request.user)


class StudentTestDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = StudentTestDetailSerializer

    queryset = StudentTest.objects.all().order_by('-created')

    # def get_queryset(self):
    #     return StudentTest.objects.get(student_id=self.kwargs.get('student_id'), id=self.kwargs.get('test_id'))

    def get_object(self):
        return StudentTest.objects.select_related(
            'student', 'student_test_info', 'student__student_info', 'instructor',
            'student__student_info__company', 'student__student_info__group',
            'student_test_info__instructor').prefetch_related('student__student_info__company__instructors', ).get(
            student_id=self.kwargs.get('student_id'), id=self.kwargs.get('test_id'))


# student test info detail
class StudentTestInfoDetailAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = StudentTestInfoSerializer
    queryset = StudentTestInfo.objects.all().order_by('-created')

    def get_queryset(self):
        return StudentTestInfo.objects.filter(test__student_id=self.kwargs.get('student_id')).order_by('-created')

    def get_object(self):
        try:
            obj = StudentTestInfo.objects.select_related('test').get(test_id=self.kwargs.get('test_id'))
        except StudentTestInfo.DoesNotExist:
            obj = StudentTestInfo.objects.create(test_id=self.kwargs.get('test_id'), instructor=self.request.user)
        return obj


# test notes
class TestNotes(ListCreateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = StudentTestNoteSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentTestNoteSerializer

        return StudentTestNoteCreateSerializer

    def get_serializer_context(self):
        context = super(TestNotes, self).get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        return StudentTestNote.objects.filter(test_id=self.kwargs.get('test_id')) \
            .select_related('test', 'test__student', 'test__student').order_by('-created')

    def perform_create(self, serializer):
        serializer.save(test_id=self.kwargs.get('test_id'))


# test not detail
class TestNoteDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = StudentTestNoteSerializer
    queryset = StudentTestNote.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentTestNoteSerializer

        return StudentTestNoteCreateSerializer

    def get_serializer_context(self):
        context = super(TestNoteDetail, self).get_serializer_context()
        context['request'] = self.request
        return context

    def get_object(self):
        note = get_object_or_404(StudentTestNote.objects.all(), test_id=self.kwargs.get('test_id'),
                                 id=self.kwargs.get('note_id'))
        # note = StudentTestNote.objects.select_related('test', 'test__student').get(
        #     test_id=self.kwargs.get('test_id'),
        #     id=self.kwargs.get('note_id')
        # )
        return note


class StudentTestSWPDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SafeDriveSWPSerializer
    queryset = SafeDriveSWP.objects.all()

    # def get_serializer_context(self):
    #     ctx = super(StudentTestSWPDetail, self).get_serializer_context()
    #     ctx.update({'request': self.request})
    #     return ctx

    def get_object(self):
        try:
            obj = SafeDriveSWP.objects.select_related(
                'test',
                'test__student',
                'test__student__student_info',
                'test__student__student_info__company',
                'test__student__student_info__group',
                'swpemployeesinterview',
                'swppowerequipment',
                'swpjobsetup',
                'swpexpecttheunexpected',
                'swppushingandpulling',
                'swpendrangemotion',
                'swpkeysliftingandlowering',
                'swpcuttinghazardsandsharpobjects',
                'swpkeystoavoidingslipsandfalls',
            ).get(test_id=self.kwargs['test_id'])
        except SafeDriveSWP.DoesNotExist:
            obj = SafeDriveSWP.objects.create(test_id=self.kwargs['test_id'])
        return obj


# SWP Injury probability graph views


@api_view(['GET'])
def swp_injury_probability_graph(request, student_id, test_id):
    SWP_INJURY_DATA = {
        'animal_bite': {
            'title': '',
            'possible_points': 0,
            'received_points': 0,
            'percentage': 0
        },
        'amputation': {
            'title': '',
            'possible_points': 0,
            'received_points': 0,
            'percentage': 0
        },
        'blunt_force_trauma': {
            'title': '',
            'possible_points': 0,
            'received_points': 0,
            'percentage': 0
        },
        'burn': {
            'title': '',
            'possible_points': 0,
            'received_points': 0,
            'percentage': 0
        },
        'cut': {
            'title': '',
            'possible_points': 0,
            'received_points': 0,
            'percentage': 0
        },
        'dehydration': {
            'title': '',
            'possible_points': 0,
            'received_points': 0,
            'percentage': 0
        },
        'fracture': {
            'title': '',
            'possible_points': 0,
            'received_points': 0,
            'percentage': 0
        },
        'frost_bite': {
            'title': '',
            'possible_points': 0,
            'received_points': 0,
            'percentage': 0
        },
        'heat_stress': {
            'title': '',
            'possible_points': 0,
            'received_points': 0,
            'percentage': 0
        },
        'sprain': {
            'title': '',
            'possible_points': 0,
            'received_points': 0,
            'percentage': 0
        },
        'spider_bite_sting': {
            'title': '',
            'possible_points': 0,
            'received_points': 0,
            'percentage': 0
        },
        'strain': {
            'title': '',
            'possible_points': 0,
            'received_points': 0,
            'percentage': 0
        },
        'stress': {
            'title': '',
            'possible_points': 0,
            'received_points': 0,
            'percentage': 0
        },
        'toxic_exposure': {
            'title': '',
            'possible_points': 0,
            'received_points': 0,
            'percentage': 0
        }
    }
    from safe_driver.models import SWP_FACTOR_CHOICES, InjuryProbabilityValueSWP
    # test_id = request.kwargs['test_id']

    class_factors = InjuryProbabilityValueSWP.objects.values('db_table', 'key', 'field_name', 'value', )
    # base_total = AccidentProbabilityValueBTWClassA.objects.values_list('key').aggregate(sum=Sum('key'))
    # print(base_total)
    class_factors_list = list(class_factors)

    obj = SafeDriveSWP.objects.select_related(
        'test',
        'test__student',
        'test__student__student_info',
        'test__student__student_info__company',
        'test__student__student_info__group',
        'swpemployeesinterview',
        'swppowerequipment',
        'swpjobsetup',
        'swpexpecttheunexpected',
        'swppushingandpulling',
        'swpendrangemotion',
        'swpkeysliftingandlowering',
        'swpcuttinghazardsandsharpobjects',
        'swpkeystoavoidingslipsandfalls',
    ).get(test_id=test_id)
    fields_list = []
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
                        factors = []
                        factor_items = [factor for factor in class_factors_list if
                                        factor['field_name'] == rel_field.name]
                        for item in factor_items:
                            # print(item)
                            factor_value = value * item['value']
                            total_received_points += factor_value
                            if value > 0:
                                SWP_INJURY_DATA[item['key']]['received_points'] += factor_value
                                SWP_INJURY_DATA[item['key']]['possible_points'] += item['value'] * 5
                                total_possible_points += item['value'] * 5
                            factors.append({
                                # 'name': item['name'],
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

    for value, name in SWP_FACTOR_CHOICES:
        # print(value)
        possible_points = SWP_INJURY_DATA[value]['possible_points']
        received_points = SWP_INJURY_DATA[value]['received_points']
        SWP_INJURY_DATA[value]['title'] = name
        if possible_points > 0 and received_points > 0:
            percentage = '{:.2f}'.format((100 / possible_points) * received_points)
            # percentage = round((100 / possible_points) * received_points, 2)
            SWP_INJURY_DATA[value]['percentage'] = percentage

        if total_received_points > 0 and received_points > 0:
            new_value = total_received_points / received_points
            new_percentage = (new_value / total_received_points) * 100
            SWP_INJURY_DATA[value]['new_value'] = '{:.2f}'.format(new_value)
            SWP_INJURY_DATA[value]['new_percentage'] = '{:.2f}'.format(new_percentage)
        else:
            SWP_INJURY_DATA[value]['new_value'] = 0
            SWP_INJURY_DATA[value]['new_percentage'] = 0

    results = {
        'total_possible_points': total_possible_points,
        'total_received_points': total_received_points,
        'chart_data': SWP_INJURY_DATA,
        'fields': fields_list
    }
    return Response(results)
