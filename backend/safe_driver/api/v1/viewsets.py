from django.db import connection, reset_queries
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.api.v1.permissions import InstructorPermission, IsSuperUser
from .btw_serializers import SafeDriveBTWSerializer
from .pretrip_serializers import SafeDrivePreTripSerializer
from .serializers import *
from .pas_serializers import (PassengerVehiclesSerializer)
from .swp_serializers import (SafeDriveSWPSerializer)
from .vrt_serializers import SafeDriveVRTSerializer


class StudentGroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = StudentGroupSerializer
    queryset = StudentGroup.objects.all().order_by('name')
    filter_backends = [DjangoFilterBackend, SearchFilter]

    search_fields = ['name']


class CompaniesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = CompanySerializer
    queryset = Company.objects.none()

    filter_backends = [DjangoFilterBackend, SearchFilter]

    search_fields = ['name', 'company_id', 'city', 'country', 'zip_code']

    # def perform_create(self, serializer):
    #     instructor = self.request.user
    #     if 'instructor' in self.request.data:
    #         instructor = self.request.data.get('instructor')
    #     serializer.save(instructor=instructor)

    def get_queryset(self):
        if self.request.user.is_instructor:
            return Company.objects.filter(instructors__in=[self.request.user]).order_by('name')
        return Company.objects.none()

        # return Company.objects.all().order_by('name')


class InstructorProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = InstructorProfileSerializer
    queryset = InstructorProfile.objects.all().order_by('user__username')

    filter_backends = [DjangoFilterBackend, SearchFilter]

    search_fields = ['user__username']


class StudentTestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = StudentTestSerializer
    queryset = StudentTest.objects.all().order_by('-created')
    filter_backends = [DjangoFilterBackend, SearchFilter]

    search_fields = ['student__username', 'student__first_name', 'student__last_name', 'student__email']


class SafeDriveEquipmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = EquipmentSerializer

    queryset = Equipment.objects.all()

    def get_queryset(self):
        # queryset = SafeDriveEquipment.objects.select_related('test', 'test__student'
        #                                                      'test__student__student_info__company',
        #                                                      'test__student__student_info__instructor',
        #                                                      'test__student__student_info').all().order_by('-created')
        queryset = Equipment.objects.select_related('test', 'test__student',
                                                    'test__student__student_info',
                                                    'test__student__student_info__company',
                                                    'test__student__student_info__instructor',
                                                    ).all().order_by('-created')
        return queryset

    def partial_update(self, request, *args, **kwargs):
        return super(SafeDriveEquipmentViewSet, self).partial_update(request, *args, **kwargs)


class SafeDriveEyeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SafeDriveEyeSerializer
    queryset = SafeDriveEye.objects.all().order_by('-created')

    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['test__student__date_joined', 'test__student__date_of_birth', 'test__student__email',
                     'test__student__first_name',
                     'home_phone_number', 'test__student__is_active', 'test__student__is_instructor',
                     'test__student__is_staff',
                     'test__student__is_student', 'test__student__is_superuser',
                     'test__student__last_login', 'test__student__last_name', 'test__student__middle_name',
                     'test__student__mobile_number',
                     'test__student__phone', 'test__student__send_gps_location', 'test__student__sex',
                     'test__student__surname', 'test__student__username', 'work_phone_number',
                     'test__student__student_info__city',
                     'test__student__student_info__state',
                     'test__student__student_info__country',
                     'test__student__student_info__territory',
                     'test__test__student__student_info__zip_code',
                     'test__student__student_info__customer_number',
                     'test__student__student_info__date_of_hire',
                     'test__student__student_info__driver_license_number',
                     'test__student__student_info__dot_expiration_date',
                     'test__student__student_info__manager_name',
                     'test__student__student_info__manager_employee_id',
                     'test__student__student_info__manager_record_id',
                     ]

    def get_queryset(self):
        return SafeDriveEye.objects.select_related(
            'test',
            'test__student',
            'test__student__student_info__company', 'test__student__student_info__instructor',
            'test__student__student_info'
        ).all().order_by('-created')


class SafeDriveNoteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SafeDriveNoteSerializer
    http_method_names = ['get', ]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['test__student__username', 'test__student__email']

    # queryset = SafeDriveNote.objects.all().order_by('-created')

    def get_queryset(self):
        queryset = SafeDriveNote.objects.select_related(
            'test__student__student_info__company', 'test__student__student_info__instructor',
            'test__student__student_info').all().order_by(
            '-created')
        return queryset

    # @action(detail=True, methods=['get', 'patch', 'delete', 'update', 'put'])
    # def get_student(self, request,):
    #     student = request.GET.get('student')
    #     obj = get_object_or_404(self.get_queryset(), student_id=student)
    #     serializer = self.get_serializer(obj)
    #     return Response(serializer.data)


class SafeDriveProdViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SafeDriveProdSerializer

    def get_queryset(self):
        queryset = SafeDriveProd.objects.select_related('test', 'test__student').all().order_by('-created')
        return queryset

    def list(self, request, *args, **kwargs):
        # print('count', len(connection.queries))
        return super(SafeDriveProdViewSet, self).list(request, *args, **kwargs)


class SafeDrivePreTripViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SafeDrivePreTripSerializer

    def get_queryset(self):
        queryset = SafeDrivePreTrip.objects.select_related(
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
        ).prefetch_related(
            'student',
        ).all().order_by('-created')
        return queryset

    def list(self, request, *args, **kwargs):
        # print('count', len(connection.queries))
        # reset_queries()
        serializer = self.get_serializer()
        # print(serializer.get_labels())
        print('ok')
        return super(SafeDrivePreTripViewSet, self).list(request, *args, **kwargs)


# BTW ViewSet
class SafeDriveBTWViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SafeDriveBTWSerializer

    def get_queryset(self):
        queryset = SafeDriveBTW.objects.select_related(
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
        ).prefetch_related('student', ).all().order_by('-created')
        return queryset


# VRT ViewSet
class SafeDriveVRTViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SafeDriveVRTSerializer

    def get_queryset(self):
        queryset = VehicleRoadTest.objects.select_related(
            'test',
            'test__student',
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
        ).prefetch_related('test__student', ).all().order_by('-created')
        return queryset


# PAS ViewSet
class SafeDrivePASViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = PassengerVehiclesSerializer

    def get_queryset(self):
        queryset = PassengerVehicles.objects.select_related(
            'test',
            'test__student',
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
        ).prefetch_related('student', ).all().order_by('-created')
        return queryset


# SWP ViewSet
class SafeDriveSWPViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = SafeDriveSWPSerializer

    def get_queryset(self):
        queryset = SafeDriveSWP.objects.select_related(
            'test', ).prefetch_related('test', ).all().order_by('-created')
        return queryset
