from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_auth.views import PasswordChangeView
from .permissions import InstructorPermission, IsSuperUser
from .serializers import *


class AdminTokenObtainPairView(TokenObtainPairView):
    serializer_class = AdminTokenObtainPairSerializer


class StudentTokenObtainPairView(TokenObtainPairView):
    serializer_class = StudentTokenObtainPairSerializer


class LoggdeUserDetail(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    @staticmethod
    def get(request, *args, **kwargs):
        serializer = LoggedUserStudentProfileSerializer(request.user)
        if request.user.is_superuser or request.user.is_staff or request.user.is_instructor:
            serializer = LoggedUserAdminProfileSerializer(request.user)
        return Response(serializer.data)


class UserGroupList(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = UserGroupSerializer
    queryset = UserGroup.objects.all()


class PermissionList(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = UserPermissionSerializer
    queryset = Permission.objects.all()


# class ChangeUserPassword(UpdateAPIView):
class ChangeUserPassword(PasswordChangeView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    # serializer_class = CustomPasswordChangeSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    # def update(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     serializer = self.get_serializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         old_password = serializer.data.get('old_password')
    #         old_password = serializer.data.get('old_password')
    #         old_password = serializer.data.get('old_password')


class AddNewAdminUser(CreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = AdminUserCreateSerializer


class AdminUserList(ListAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = AdminUserListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['is_instructor', 'is_superuser', 'is_staff', 'is_active', 'is_student', 'sex', ]
    ordering_fields = '__all__'
    search_fields = ['date_joined', 'date_of_birth', 'email', 'first_name',
                     'home_phone_number', 'is_active', 'is_instructor', 'is_staff', 'is_student', 'is_superuser',
                     'last_login', 'last_name', 'middle_name', 'mobile_number', 'phone', 'send_gps_location', 'sex',
                     'surname', 'username', 'work_phone_number',
                     'student_info__city',
                     'student_info__state',
                     'student_info__country',
                     'student_info__territory',
                     'student_info__zip_code',
                     'student_info__customer_number',
                     'student_info__date_of_hire',
                     'student_info__driver_license_number',
                     'student_info__dot_expiration_date',
                     'student_info__manager_name',
                     'student_info__manager_employee_id',
                     'student_info__manager_record_id',
                     ]

    # search_fields = '__all_-'

    def get_queryset(self):
        queryset = User.objects.filter(~Q(id=self.request.user.id),
                                       ~Q(username='AnonymousUser')
                                       ).select_related(
            'student_info',
            'student_info__company',
            'student_info__instructor'
        ).order_by('first_name')
        return queryset


class AdminUserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = AdminUserDetailSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset


# instructor API
class InstructorRegister(CreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = RegisterInstructorSerializer
