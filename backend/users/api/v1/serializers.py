from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.http import HttpRequest
from django.utils.translation import ugettext_lazy as _
from allauth.account import app_settings as allauth_settings
from allauth.account.forms import ResetPasswordForm
from allauth.utils import email_address_exists, generate_unique_username
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import exceptions, serializers
from rest_auth.serializers import PasswordResetSerializer, PasswordChangeSerializer
from django.contrib.auth.models import Group as UserGroup, Permission
from rest_framework.exceptions import NotFound
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone

from safe_driver.models import (Company, InstructorProfile)

User = get_user_model()


class UserCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class UserInstructorProfileSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        try:
            if instance.company:
                ret['company'] = UserCompanySerializer(instance.company).data
            else:
                ret['company'] = None
        except:
            ret['company'] = None
        return ret

    class Meta:
        model = InstructorProfile
        fields = '__all__'


class UserALLFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AdminTokenObtainPairSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)
        # serializer = UserALLFieldSerializer(self.user)
        if self.user.is_instructor or self.user.is_staff or self.user.is_superuser:

            refresh = self.get_token(self.user)
            self.user.last_login = timezone.now()
            self.user.save()
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)

        else:
            raise NotFound('User is not an Instructor/Staff/Admin.')
            # raise serializers.ValidationError({
            #     'detail': 'User is not an Instructor/Staff/Admin.',
            # })

        return data


class StudentTokenObtainPairSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        if not self.user.is_student:
            raise serializers.ValidationError({
                'errors': [
                    _('You do not have permission to perform this action.')
                ],
            })

        refresh = self.get_token(self.user)
        self.user.last_login = timezone.now()
        self.user.save()
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data


class AdminUserCreateSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=False, read_only=True)
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('groups', 'user_permissions')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
        }

    def _get_request(self):
        request = self.context.get('request')
        if request and not isinstance(request, HttpRequest) and hasattr(request, '_request'):
            request = request._request
        return request

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def create(self, validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        username = validated_data.get('username')
        if username is None or username == "":
            username = generate_unique_username([
                first_name,
                last_name,
                'user'
            ])

        validated_data['username'] = username

        user = User(**validated_data)

        user.set_password(validated_data.get('password'))
        user.save()
        # print(validated_data)
        request = self._get_request()
        setup_user_email(request, user, [])
        return user

    def save(self, request=None):
        """rest_auth passes request so we must override to accept it"""
        return super().save()


class SignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'middle_name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
            'username': {
                'required': False,
                'allow_blank': False,
            },
            'email': {
                'required': True,
                'allow_blank': False,
            },
            'first_name': {
                'required': True,
                'allow_blank': False,
            },
            'last_name': {
                'required': True,
                'allow_blank': False,
            }
        }

    def _get_request(self):
        request = self.context.get('request')
        if request and not isinstance(request, HttpRequest) and hasattr(request, '_request'):
            request = request._request
        return request

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def create(self, validated_data):

        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        middle_name = validated_data.get('middle_name')
        username = validated_data.get('username')
        if username is None or username == "":
            username = generate_unique_username([
                first_name,
                last_name,
                'user'
            ])

        user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            username=username
        )

        user.set_password(validated_data.get('password'))
        user.save()
        print(validated_data)
        request = self._get_request()
        setup_user_email(request, user, [])
        return user

    def save(self, request=None):
        """rest_auth passes request so we must override to accept it"""
        return super().save()


class PasswordSerializer(PasswordResetSerializer):
    """Custom serializer for rest_auth to solve reset password error"""
    password_reset_form_class = ResetPasswordForm


class CustomPasswordChangeSerializer(PasswordChangeSerializer):
    old_password = serializers.CharField(max_length=128)
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)

    set_password_form_class = SetPasswordForm


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name']


class UserInstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'first_name', 'last_name', ]


class UserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class UserGroupSerializer(serializers.ModelSerializer):
    permissions = UserPermissionSerializer(many=True)

    class Meta:
        model = UserGroup
        fields = '__all__'


class UserStudentGroupSerializer(serializers.ModelSerializer):
    # permissions = UserPermissionSerializer(many=True)

    class Meta:
        model = UserGroup
        fields = ['id', 'name']


# class UserStudentInfoSerializer(serializers.ModelSerializer):
#     # instructor = UserInstructorSerializer()
#     # company = UserCompanySerializer()
#
#     class Meta:
#         model = StudentInfo
#         fields = '__all__'
#
#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         # print(instance.user.student_info.instructor)
#         # print(instance.user.student_info.company)
#         # response['instructor'] = instance.instructor
#         try:
#             # response['instructor'] = instance.instructor
#             if instance.instructor:
#                 response['instructor'] = UserInstructorSerializer(instance.instructor, many=False,
#                                                                   read_only=True).data
#             else:
#                 response['instructor'] = None
#         except User.DoesNotExist:
#             response['instructor'] = None
#
#         try:
#             if instance.company:
#                 response['company'] = UserCompanySerializer(instance.company, many=False, read_only=True).data
#             else:
#                 response['company'] = None
#
#         except:
#             response['company'] = None
#         return response


class AdminUserListSerializer(serializers.ModelSerializer):
    # info = UserStudentInfoSerializer(many=False, source='student_info', read_only=True)

    # groups = UserStudentGroupSerializer(many=True)
    def to_representation(self, instance):
        response = super().to_representation(instance)
        try:
            # response['instructor'] = instance.instructor
            if instance.is_instructor:
                response['instructor_profile'] = UserInstructorProfileSerializer(instance.instructor_profile,
                                                                                 many=False,
                                                                                 read_only=True).data
            else:
                response['instructor_profile'] = None
        except:
            response['instructor_profile'] = None

        return response

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('groups', 'user_permissions')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
        }


class AdminUserDetailSerializer(serializers.ModelSerializer):
    # info = UserStudentInfoSerializer(many=False, source='student_info', )

    # groups = UserStudentGroupSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
        # exclude = ('groups', 'user_permissions')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
        }

    def update(self, instance, validated_data):
        # if "student_info" in validated_data:
        #     info = validated_data.pop('student_info')
        #     try:
        #         UserStudentInfoSerializer().update(instance.student_info, info)
        #     except StudentInfo.DoesNotExist:
        #         StudentInfo.objects.create(student=instance, **info)
        # info_serializer = user()
        # info_instance = instance.student_info
        # info_serializer.update(info_instance, info)
        # student_info = StudentInfo.objects.get(id=instance.student_info.id)
        # # student_info.update(**info)
        # student_info.save(**info)
        # print(student_info.value)
        return super(AdminUserDetailSerializer, self).update(instance, validated_data)


class UserStudentSerializer(serializers.ModelSerializer):
    # groups = UserGroupSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'full_name',
            'username',
            'is_student',
        )


class LoggedUserStudentProfileSerializer(serializers.ModelSerializer):
    groups = UserGroupSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'username',
            'password',
            'groups',
            'last_login',
            'date_joined',
            'is_student',
        )

        extra_kwargs = {'password': {'write_only': True}}


class LoggedUserAdminProfileSerializer(serializers.ModelSerializer):
    groups = UserGroupSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class StudentListSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        from safe_driver.api.v1.serializers import StudentInfoSerializer
        res = super(StudentListSerializer, self).to_representation(instance)
        try:
            res['info'] = StudentInfoSerializer(instance.student_info).data
        except:
            res['info'] = None

        return res

    class Meta:
        model = User
        exclude = ('groups', 'user_permissions')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
        }


class RegisterInstructorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=False, read_only=True)
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    profile = UserInstructorProfileSerializer(many=False, source='instructor_profile')

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('groups', 'user_permissions')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
        }

    def _get_request(self):
        request = self.context.get('request')
        if request and not isinstance(request, HttpRequest) and hasattr(request, '_request'):
            request = request._request
        return request

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def create(self, validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        username = validated_data.get('username')
        profile = validated_data.pop('instructor_profile')
        if username is None or username == "":
            username = generate_unique_username([
                first_name,
                last_name,
                'user'
            ])

        validated_data['username'] = username
        validated_data['is_instructor'] = True
        validated_data['is_student'] = False

        user = User(**validated_data)

        user.set_password(validated_data.get('password'))
        user.save()
        if profile:
            # validated_data['profile']['user'] = user
            InstructorProfile.objects.create(user=user, **profile)
        # print(validated_data)
        request = self._get_request()
        setup_user_email(request, user, [])
        return user

    def save(self, request=None):
        """rest_auth passes request so we must override to accept it"""
        return super().save()


class InstructorUserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'full_name', 'email', ]
