from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, GenericAPIView, \
    get_object_or_404, RetrieveUpdateDestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions, \
    DjangoObjectPermissions, \
    DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.api.v1.permissions import InstructorPermission, HasGroupPermission
from users.api.v1.serializers import StudentListSerializer
from .btw_serializers import SafeDriveBTWSerializer
from .filtersets import SudentListInfoFilterSet, InstructorListFilterSet
import json
# from safe_driver.models import *

from ...models import *
from .serializers import CompanySerializer, InstructorListSerializer, InstructorProfileSerializer, \
    NewStudentRegisterSerializer, StudentDetailSerializer, EquipmentSerializer, \
    SafeDriveEyeSerializer, SafeDriveNoteSerializer, SafeDriveProdSerializer, ProdItemSerializer, \
    StudentDetailUpdateSerializer
from .swp_serializers import SafeDriveSWPSerializer
from .vrt_serializers import SafeDriveVRTSerializer
from .pas_serializers import (PassengerVehiclesSerializer)
from .pretrip_serializers import (SafeDrivePreTripSerializer)

User = get_user_model()


class CompaniesListView(GenericAPIView):
    # authentication_classes = [IsAuthenticated, ]
    permission_classes = [IsAuthenticated, InstructorPermission, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = CompanySerializer
    queryset = Company.objects.none()

    required_groups = {
        'GET': ['Instructors Group', ],
    }

    def get_queryset(self):
        queryset = Company.objects.all().order_by('name')
        return queryset

    # def list(self, request, *args, **kwargs):
    #     print(request.user.groups.all())
    #     return super(CompaniesListView, self).list(request, *args, **kwargs)


class InstructorList(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser | InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = InstructorListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = InstructorListFilterSet
    queryset = User.objects.filter(is_instructor=True).order_by('first_name')

    search_fields = ['date_joined', 'date_of_birth', 'email', 'first_name',
                     'home_phone_number', 'is_active', 'is_instructor', 'is_staff', 'is_student', 'is_superuser',
                     'last_login', 'last_name', 'middle_name', 'mobile_number', 'phone', 'send_gps_location', 'sex',
                     'surname', 'username', 'work_phone_number',
                     'instructor_profile__company__name',
                     'instructor_profile__company__compan_id',
                     ]

    def get_queryset(self):
        return User.objects.filter(
            is_instructor=True).filter(~Q(username='AnonymousUser')).select_related(
            'instructor_profile',
            'instructor_profile__company',
        ).prefetch_related('groups', ).order_by('-date_joined')


class InstructorProfileDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser | InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = InstructorProfileSerializer

    def get_object(self):
        try:
            obj = InstructorProfile.objects.get(user_id=self.kwargs['user_id'])
        except InstructorProfile.DoesNotExist:
            obj = InstructorProfile.objects.create(user_id=self.kwargs['user_id'])
        return obj


class NewStudentRegister(CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser | InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = NewStudentRegisterSerializer

    # def create(self, request, *args, **kwargs):
    #     write_serializer = self.get_serializer(data=request.data)
    #     if write_serializer.is_valid(raise_exception=True):
    #         instance = write_serializer.save()
    #         read_serializer = StudentDetailSerializer(instance, many=False)
    #         return Response(read_serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(write_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class StudentInfoCreate(CreateAPIView):
#     serializer_class = StudentInfoSerializer


# class StudentInfoDetail(RetrieveAPIView, UpdateAPIView):
#     permission_classes = [IsAuthenticated, IsAdminUser | InstructorPermission]
#     authentication_classes = [JWTAuthentication, SessionAuthentication, ]
#     serializer_class = StudentInfoReadSerializer
#     queryset = StudentInfo.objects.all()
#
#     # def get_serializer_class(self):
#     #     print(self.request.method)
#     #     if self.request.method in ["POST", "UPDATE", "PATCH"]:
#     #         return StudentInfoWriteSerializer
#     #     else:
#     #         return StudentInfoReadSerializer
#
#     # def get_serializer(self, *args, **kwargs):
#     #     if self.request.method in ["POST", "UPDATE", "PATCH"]:
#     #         return StudentInfoWriteSerializer
#     #     else:
#     #         return StudentInfoWriteSerializer
#
#     def get_object(self):
#         try:
#             obj = StudentInfo.objects.select_related(
#                 'user',
#                 'company',
#                 'instructor'
#             ).get(user_id=self.kwargs['student_id'])
#         except StudentInfo.DoesNotExist:
#             obj = StudentInfo.objects.create(user_id=self.kwargs['student_id'])
#         return obj
#
#     # def partial_update(self, request, *args, **kwargs):
#     #     serializer = self.get_serializer_class()
#     #     if serializer.is_valid(raise_exception=True):
#     #         instance = serializer.save()
#
#     # def partial_update(self, request, *args, **kwargs):


class StudentListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser | InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = StudentListSerializer
    # serializer_class = StudentListInfoSerializer
    queryset = None
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = SudentListInfoFilterSet
    search_fields = ['date_joined', 'date_of_birth', 'email', 'first_name',
                     'home_phone_number', 'is_active', 'is_instructor', 'is_staff', 'is_student', 'is_superuser',
                     'last_login', 'last_name', 'middle_name', 'mobile_number', 'phone', 'send_gps_location', 'sex',
                     'surname', 'username', 'work_phone_number', 'student_info__group__name',
                     'student_info__company__name', 'student_info__company_city', 'student_info__company__state',
                     'student_info__company__zip_code', 'student_info__company__phone',
                     ]

    def get_queryset(self):
        return User.objects.select_related(
            'student_info', 'student_info__company', 'student_info__group'
        ).filter(is_student=True, student_info__company__instructors__in=[self.request.user]).filter(~Q(
            username='AnonymousUser')).prefetch_related('groups', ).order_by('-date_joined')

        # return User.objects.select_related(
        #     'student_info', 'student_info__company', 'student_info__group'
        # ).filter(is_student=True,).filter(~Q(
        #     username='AnonymousUser')).prefetch_related('groups', ).order_by('-date_joined')


class StudentDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = StudentDetailUpdateSerializer

    def get_queryset(self):
        return User.objects.filter(
            is_student=True).select_related().prefetch_related(
            'groups',
        ).order_by('-date_joined')

    def get_object(self):
        obj = User.objects.select_related('student_info', 'student_info__company', 'student_info__group'
                                          ).prefetch_related('groups', ).get(pk=self.kwargs['student_id'])
        try:
            obj.student_info
        except StudentInfo.DoesNotExist:
            StudentInfo.objects.create(student=obj)
        return obj

    def retrieve(self, request, *args, **kwargs):
        # print(len(connection.queries))
        return super(StudentDetailAPIView, self).retrieve(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     print(len(connection.queries))
    #     return super(StudentDetailAPIView, self).update(request, *args, **kwargs)
    #
    # def partial_update(self, request, *args, **kwargs):
    #     print(len(connection.queries))
    #     return super(StudentDetailAPIView, self).partial_update(request, *args, **kwargs)


# student equip list by test
class StudentEquipList(ListCreateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = EquipmentSerializer

    pagination_class = None

    def get_queryset(self):
        queryset = Equipment.objects.select_related('test', 'test__student',
                                                    'test__student__student_info',
                                                    'test__student__student_info__company',
                                                    'test__student__student_info__group',
                                                    ).filter(test_id=self.kwargs['test_id']).order_by('-created')
        return queryset

    def perform_create(self, serializer):
        serializer.save(test_id=self.kwargs['test_id'])


class StudentEquipDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = EquipmentSerializer

    def get_queryset(self):
        queryset = Equipment.objects.select_related('test', 'test__student',
                                                    'test__student__student_info__company',
                                                    'test__student__student_info').all().order_by('-created')
        return queryset

    def get_object(self):
        try:
            obj = Equipment.objects.select_related('test', 'test__student',
                                                   'test__student__student_info__company',
                                                   'test__student__student_info'
                                                   ).get(test_id=self.kwargs['test_id'],
                                                         id=self.kwargs['equip_id'])
        except Equipment.DoesNotExist:
            obj = Equipment.objects.create(test_id=self.kwargs['test_id'])
        return obj


class StudentEyeDetailByStudentID(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SafeDriveEyeSerializer
    queryset = SafeDriveEye.objects.all().order_by('-created')

    def get_object(self):
        try:
            obj = SafeDriveEye.objects.select_related(
                'test', 'test__student', 'test__student__student_info',
                'test__student__student_info__company',
                'test__student__student_info__group',
            ).get(test_id=self.kwargs['test_id'])
        except SafeDriveEye.DoesNotExist:
            obj = SafeDriveEye.objects.create(test_id=self.kwargs['test_id'])
        return obj


class StudentNoteListByStudentID(ListCreateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SafeDriveNoteSerializer
    queryset = SafeDriveNote.objects.all().order_by('-created')

    def get_queryset(self):
        queryset = SafeDriveNote.objects.select_related(
            'student__student_info__company', 'student__student_info__instructor',
            'student__student_info').filter(student_id=self.kwargs['student_id']).order_by('-created')
        return queryset

    def perform_create(self, serializer):
        serializer.save(student_id=self.kwargs['student_id'])


class StudentNoteDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SafeDriveNoteSerializer
    queryset = SafeDriveNote.objects.all()

    def get_object(self):
        obj = get_object_or_404(SafeDriveNote, pk=self.kwargs['pk'], student_id=self.kwargs['student_id'])
        return obj


class StudentProdDetail(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SafeDriveProdSerializer
    queryset = SafeDriveProd.objects.all()

    def get_object(self):
        try:
            obj = SafeDriveProd.objects.select_related(
                'test', 'test__student',

                'test__student__student_info',
                # 'test__student__student_info__instructor',
                'test__student__student_info__company',
                'test__student__student_info__group',
            ).prefetch_related('prod_item', ).get(test_id=self.kwargs['test_id'])
            # obj = get_object_or_404(self.get_queryset().select_related(
            #     'student__student_info__company', 'student__student_info__instructor',
            #     'student__student_info'), student_id=self.kwargs['student_id'])
        except SafeDriveProd.DoesNotExist:
            obj = SafeDriveProd.objects.create(test_id=self.kwargs['test_id'])
        return obj


# prod items by prod id
class ProdItemListCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = ProdItemSerializer
    pagination_class = None

    # queryset = ProdItem.objects.a
    def get_queryset(self):
        prod = SafeDriveProd.objects.get(test_id=self.kwargs['test_id'])
        # print(prod)
        return ProdItem.objects.filter(prod=prod).order_by('created')

    def perform_create(self, serializer):
        prod = SafeDriveProd.objects.get(test_id=self.kwargs['test_id'])
        print(prod)
        obj = serializer.save(prod_id=prod.id)
        # obj.save()
        return obj


class StudentPreTripDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SafeDrivePreTripSerializer
    queryset = SafeDrivePreTrip.objects.all()

    def get_object(self):
        try:
            obj = SafeDrivePreTrip.objects.select_related(
                'student',
                'pretripinsidecab',
                'pretripcoals',
                'pretripenginecompartment',
                'pretripvehiclefront',
                'pretripbothsidesvehicle',
                'pretripvehicleortractorrear',
                'pretripfronttrailerbox',
                'pretripdriversidetrailerbox',
                'pretripreartrailerbox',
                'pretrippassengersidetrailerbox',
                'pretripdolly',
                'pretripcombinationvehicles',
                'pretripcombinationvehicles__pre_trip',
                'pretripposttrip',
            ).get(student_id=self.kwargs['student_id'])
        except SafeDrivePreTrip.DoesNotExist:
            obj = SafeDrivePreTrip.objects.create(student_id=self.kwargs['student_id'])

        # obj = get_object_or_404(SafeDrivePreTrip, student_id=self.kwargs['pk'])
        # test_obj = SafeDrivePreTrip.objects.get(id=1)
        # test_obj.pretripinsidecab
        return obj


# student BTW Details
class StudentBTWDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SafeDriveBTWSerializer
    queryset = SafeDriveBTW.objects.all()

    def get_object(self):
        try:
            obj = SafeDriveBTW.objects.select_related(
                'student',
                'btwcabsafety',
                'btwstartengine',
                'btwengineoperation',
                'btwclutchandtransmission',
                'btwcoupling',
                'btwuncoupling',
                'btwbrakesandstoppings',
                'btweyemovementandmirror',
                'btwrecognizeshazards',
                'btwlightsandsignals',
                'btwsteering',
                'btwbacking',
                'btwspeed',
                'btwintersections',
                'btwturning',
                'btwparking',
                'btwmultipletrailers',
                'btwhills',
                'btwpassing',
                'btwgeneralsafetyanddotadherence',
            ).get(student_id=self.kwargs['student_id'])
        except SafeDriveBTW.DoesNotExist:
            obj = SafeDriveBTW.objects.create(student_id=self.kwargs['student_id'])
        return obj


# student VRT Details
class StudentVRTDetail(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SafeDriveVRTSerializer
    queryset = VehicleRoadTest.objects.all()

    def get_object(self):
        try:
            obj = VehicleRoadTest.objects.select_related(
                'test',
                'test__student',
                'test__student__student_info',
                'test__student__student_info__company',
                'test__student__student_info__group',
                'vrtpretrip',
                'vrtcoupling',
                'vrtuncoupling',
                'vrtengineoperations',
                'vrtstartengine',
                'vrtuseclutch',
                'vrtuseofbrakes',
                'vrtuseoftransmission',
                'vrtbacking',
                'vrtparking',
                'vrtdrivinghabits',
                'vrtposttrip',
            ).get(test_id=self.kwargs['test_id'])
        except VehicleRoadTest.DoesNotExist:
            obj = VehicleRoadTest.objects.create(test_id=self.kwargs['test_id'])
        return obj


# student PAS Details
class StudentPASDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = PassengerVehiclesSerializer
    queryset = PassengerVehicles.objects.all()

    def get_object(self):
        try:
            obj = PassengerVehicles.objects.select_related(
                'student',
                'pascabsafety',
                'passtartengine',
                'pasengineoperation',
                'pasbrakesandstoppings',
                'paspassengersafety',
                'paseyemovementandmirror',
                'pasrecognizeshazards',
                'paslightsandsignals',
                'passteering',
                'pasbacking',
                'passpeed',
                'pasintersections',
                'pasturning',
                'pasparking',
                'pashills',
                'paspassing',
                'pasrailroadcrossing',
                'pasgeneralsafetyanddotadherence',
            ).get(student_id=self.kwargs['student_id'])
        except PassengerVehicles.DoesNotExist:
            obj = PassengerVehicles.objects.create(student_id=self.kwargs['student_id'])
        return obj


class StudentTestPASDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = PassengerVehiclesSerializer
    queryset = PassengerVehicles.objects.all()

    def get_object(self):
        try:
            obj = PassengerVehicles.objects.select_related(
                'test',
                'test__student',
                'test__student__student_info',
                'test__student__student_info__company',
                'test__student__student_info__group',
                'pascabsafety',
                'passtartengine',
                'pasengineoperation',
                'pasbrakesandstoppings',
                'paspassengersafety',
                'paseyemovementandmirror',
                'pasrecognizeshazards',
                'paslightsandsignals',
                'passteering',
                'pasbacking',
                'passpeed',
                'pasintersections',
                'pasturning',
                'pasparking',
                'pashills',
                'paspassing',
                'pasrailroadcrossing',
                'pasgeneralsafetyanddotadherence',
            ).get(test_id=self.kwargs['test_id'])
        except PassengerVehicles.DoesNotExist:
            obj = PassengerVehicles.objects.create(test_id=self.kwargs['test_id'])
        return obj


# student SWP Details
class StudentSWPDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SafeDriveSWPSerializer
    queryset = SafeDriveSWP.objects.all()

    def get_object(self):
        try:
            obj = SafeDriveSWP.objects.select_related(
                'student',
                'swpemployeesinterview',
                'swppowerequipment',
                'swpjobsetup',
                'swpexpecttheunexpected',
                'swppushingandpulling',
                'swpendrangemotion',
                'swpkeysliftingandlowering',
                'swpcuttinghazardsandsharpobjects',
                'swpkeystoavoidingslipsandfalls',
            ).get(student_id=self.kwargs['student_id'])
        except SafeDriveSWP.DoesNotExist:
            obj = SafeDriveSWP.objects.create(student_id=self.kwargs['student_id'])
        return obj


class SampleFactorCSVDownload(APIView):
    authentication_classes = []

    @staticmethod
    @csrf_exempt
    def post(request, *args, **kwargs):
        import csv
        # print(request.data)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="sample.csv"'
        #
        writer = csv.writer(response)
        writer.writerow(['db_table', 'model_name', 'key', 'field_name', 'value', ])

        choice_data = request.data.get('choice_data')
        field_list = request.data.get('field_list')
        for choice in choice_data:
            # print(choice[0])
            for field in field_list:
                for data in field['data']:
                    # print(choice[0], data['field'])
                    writer.writerow([field['db_table'], field['title'], choice[0], data['field'], 0.00, ])
        # return response
        return response


class InstructionSampleCSVDownload(APIView):
    authentication_classes = []

    @staticmethod
    @csrf_exempt
    def post(request, *args, **kwargs):
        import csv
        print(request.data)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="sample.csv"'
        #
        writer = csv.writer(response)
        writer.writerow(['db_table', 'model_name', 'field_name', 'instruction', ])

        field_list = request.data.get('field_list')
        for field in field_list:
            for data in field['data']:
                # print(choice[0], data['field'])
                writer.writerow([field['db_table'], field['title'], data['field'], 'Sample Instruction Text', ])

        # return response
        return response
