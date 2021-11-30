from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import HttpRequest
from django.utils.translation import ugettext_lazy as _
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists, generate_unique_username
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email, send_email_confirmation
from rest_framework import serializers

from safe_driver.image_functions import base64_to_image_content
from safe_driver.models import *

from users.api.v1.serializers import (UserInstructorSerializer, UserStudentSerializer,
                                      UserStudentGroupSerializer)
from safe_driver.api.v1.tests.serializers import (StudentTestInfoSerializer)

User = get_user_model()


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class InstructorProfileSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['company'] = CompanySerializer(instance.company).data
        return ret

    class Meta:
        model = InstructorProfile
        fields = '__all__'


class InstructorListSerializer(serializers.ModelSerializer):
    profile = InstructorProfileSerializer(source='instructor_profile')

    class Meta:
        model = User
        exclude = ('user_permissions', 'groups',)

        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }


class StudentInfoCreateSerializer(serializers.ModelSerializer):
    # company = serializers.IntegerField(write_only=True, required=True)
    # group = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = StudentInfo
        fields = '__all__'


class StudentInfoSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    # company = serializers.SerializerMethodField(method_name='get_company', read_only=True)
    # group = StudentGroupSerializer(read_only=True)

    def to_representation(self, instance):
        res = super(StudentInfoSerializer, self).to_representation(instance)
        # res['company'] = CompanySerializer(instance.company).data
        # if instance.company:
        #     res['company'] = CompanySerializer(instance.company).data
        #     try:
        #         res['company'] = CompanySerializer(instance.student_company).data
        #     except Company.DoesNotExist:
        #         res['company'] = None
        #
        try:
            res['group'] = StudentGroupSerializer(instance.group).data
        except StudentGroup.DoesNotExist:
            res['group'] = None
        return res

    def get_company(self, instance):
        # print(instance.company)
        company = CompanySerializer(instance.company)
        return company.data

    class Meta:
        model = StudentInfo
        fields = '__all__'


class NewStudentRegisterSerializer(serializers.ModelSerializer):
    # info = StudentInfoCreateSerializer(source='student_info', read_only=True)

    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def to_representation(self, instance):
        res = super(NewStudentRegisterSerializer, self).to_representation(instance)
        try:
            res['info'] = StudentInfoSerializer(instance.student_info).data

        except StudentInfo.DoesNotExist:
            res['info'] = None
        return res

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('user_permissions', 'is_superuser', 'is_instructor', 'is_staff')
        read_only_fields = ['groups', ]

        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
        }
        # depth = 3

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

    def validate(self, attrs):

        request = self.context.get("request")
        if 'info' not in request.data:
            raise serializers.ValidationError({
                'info': _("Info is required.")
            })

        if 'company' not in request.data.get('info'):
            raise serializers.ValidationError(
                _("Company field is required in Info.")
            )

        elif 'company' in request.data.get('info'):
            company = request.data.get('info')['company']
            if not isinstance(company, int):
                raise serializers.ValidationError({
                    'info': {
                        'company': [
                            _("Invalid Value Type. Should be pk int value.")
                        ]
                    }
                })
            else:
                try:
                    Company.objects.get(pk=company)
                except Company.DoesNotExist:
                    raise serializers.ValidationError({
                        'info': {
                            'company': [
                                _("Invalid pk. Does not exist.")
                            ]
                        }
                    })

        if 'group' not in request.data.get('info'):
            raise serializers.ValidationError(
                _("Group field is required in Info.")
            )

        elif 'group' in request.data.get('info'):
            group = request.data.get('info')['group']
            if not isinstance(group, int):
                raise serializers.ValidationError({
                    'info': {
                        'group': [
                            _("Invalid Value Type. Should be pk int value.")
                        ]
                    }
                })
            else:
                try:
                    StudentGroup.objects.get(pk=group)
                except StudentGroup.DoesNotExist:
                    raise serializers.ValidationError({
                        'info': {
                            'group': [
                                _("Invalid pk. Does not exist.")
                            ]
                        }
                    })

        # if 'group' in request.data.get('info'):
        #     attrs['group'] = request.data.get('group')

        # if 'info' in request.data:
        #     attrs['info'] = request.data.get('info')

        # print(dict(attrs))
        # attrs['instructor'] = request.user

        # attrs['info']['company'] = request.data.get('info')['company']
        # attrs['info']['group'] = request.data.get('info')['group']
        # print(request.data.get('info'))
        print(attrs)
        return attrs

    def create(self, validated_data):
        request = self.context.get("request")
        groups = request.data.get('groups')
        # print(Group.objects.filter(id__in=validated_data.get('groups')))
        # company = request.data.get('info')['company']
        # group = request.data.get('info')['group']
        # company = Company.objects.get(pk=request.data.get('info')['company'])
        info = request.data.get('info')
        # info = validated_data.pop('info')

        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        username = validated_data.get('username')
        validated_data['is_student'] = True
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
        try:
            group = info.pop('group')
            company = info.pop('company')
            StudentInfo.objects.create(student=user, company_id=company, group_id=group, **info)
        except:
            pass
        request = self._get_request()

        setup_user_email(request, user, [])
        # user.groups.set(Group.objects.filter(id__in=groups))
        # StudentInfo.objects.create(student=user, company_id=company, instructor=request.user, **info)

        try:
            user.groups.set(Group.objects.filter(id__in=groups))
        except:
            pass

        # try:
        #     send_email_confirmation(request, user, signup=True)
        # except:
        #     pass
        return user

    def save(self, request=None):
        """rest_auth passes request so we must override to accept it"""
        return super().save()


class StudentDetailSerializer(serializers.ModelSerializer):
    info = StudentInfoSerializer(many=False, source='student_info', read_only=True)

    # total_tests = serializers.IntegerField(read_only=True)
    # groups = UserStudentGroupSerializer(many=True)

    class Meta:
        model = User
        exclude = ('user_permissions', 'is_superuser', 'is_instructor', 'is_staff', 'groups')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
        }
        # depth = 1

    def update(self, instance, validated_data):
        return super(StudentDetailSerializer, self).update(instance, validated_data)


class StudentDetailUpdateSerializer(serializers.ModelSerializer):
    info = StudentInfoSerializer(many=False, source='student_info')

    # total_tests = serializers.IntegerField(read_only=True)

    class Meta:
        model = User

        exclude = ('user_permissions', 'is_superuser', 'is_instructor', 'is_staff', 'groups')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
        }

    def update(self, instance, validated_data):
        # print(validated_data)
        if 'student_info' in validated_data:
            info = validated_data.pop('student_info')
            info_serializer = StudentInfoSerializer()
            try:
                info_serializer.update(instance.student_info, info)
            except StudentInfo.DoesNotExist:
                StudentInfo.objects.create(student=instance, **info)

            # print(info)
        return super(StudentDetailUpdateSerializer, self).update(instance, validated_data)


class StudentTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTest
        fields = '__all__'


class StudentTestListSerializer(serializers.ModelSerializer):
    student = StudentDetailSerializer(read_only=True)
    # instructor = InstructorProfileSerializer(read_only=True, source='student_test_info_instructor')
    # company = CompanySerializer(read_only=True, source='student_test_info_company')

    def to_representation(self, instance):
        response = super(self.__class__, self).to_representation(instance)
        if instance.instructor:
            from users.api.v1.serializers import UserInstructorSerializer
            response['instructor'] = UserInstructorSerializer(instance.instructor).data
        else:
            response['instructor'] = None

        return response

    class Meta:
        model = StudentTest
        fields = '__all__'


class StudentTestDetailSerializer(serializers.ModelSerializer):
    student = StudentDetailSerializer(read_only=True)
    is_instructor = serializers.SerializerMethodField(method_name='check_is_instructor')

    def check_is_instructor(self, instance):
        request = self.context['request']
        company_instructors = instance.student.student_info.company.instructors.filter(id__in=[request.user.id])
        if company_instructors.exists():
            return True
        return False

    def to_representation(self, instance):

        response = super(StudentTestDetailSerializer, self).to_representation(instance)

        if instance.instructor:
            from users.api.v1.serializers import UserInstructorSerializer
            response['instructor'] = UserInstructorSerializer(instance.instructor).data
        else:
            response['instructor'] = None

        return response

    class Meta:
        model = StudentTest
        fields = '__all__'

    # def cre


class EquipmentSerializer(serializers.ModelSerializer):
    # instructor = UserInstructorSerializer(read_only=True)
    # company = CompanySerializer(read_only=True)
    # student = UserStudentSerializer(read_only=True)
    test = StudentTestSerializer(read_only=True)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

    class Meta:
        model = Equipment
        fields = '__all__'

    # def validate(self, attrs):
    #     # print(attrs)
    #     try:
    #         obj_user = attrs['instructor']
    #         # print(obj_user.is_superuser)
    #         # print(obj_user.is_instructor)
    #         if not (obj_user.is_instructor or obj_user.is_superuser):
    #             raise serializers.ValidationError(
    #                 {
    #                     'instructor': _('Selected user is not an instructor/admin.')
    #                 }
    #             )
    #     except:
    #         pass
    #     # print(obj_user)
    #     return attrs


class SafeDriveNoteSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        response = super().to_representation(instance)
        try:
            response['instructor'] = UserInstructorSerializer(instance.student.student_info.instructor,
                                                              read_only=True).data
        except:
            response['instructor'] = None
        try:
            response['company'] = CompanySerializer(instance.student.student_info.company, read_only=True).data
        except:
            response['company'] = None

        response['student'] = UserStudentSerializer(instance.student, read_only=True).data
        # if instance.student.student_info and instance.student.student_info.instructor is None:
        #     response['instructor'] = None
        #
        # if instance.student.student_info and instance.student.student_info.company is None:

        # return super(SafeDriveEquipmentSerializer, self).to_representation(instance)
        return response

    class Meta:
        model = SafeDriveNote
        fields = '__all__'

        extra_kwargs = {
            'student': {
                'read_only': True,
            },
        }


class SafeDriveEyeSerializer(serializers.ModelSerializer):
    test = StudentTestSerializer(read_only=True)

    def to_representation(self, instance):
        response = super(SafeDriveEyeSerializer, self).to_representation(instance)
        response['student'] = StudentDetailSerializer(instance.test.student).data
        # try:
        #     response['info'] = StudentInfoSerializer(instance.test.student.student_info, read_only=True).data
        # except:
        #     response['info'] = None
        return response

    class Meta:
        model = SafeDriveEye
        fields = '__all__'


class ProdItemSerializer(serializers.ModelSerializer):
    total_number = serializers.IntegerField(read_only=True)

    class Meta:
        model = ProdItem
        fields = '__all__'

        extra_kwargs = {
            'prod': {
                'read_only': True
            }
        }


class SafeDriveProdSerializer(serializers.ModelSerializer):
    test = StudentTestSerializer(read_only=True)
    total_number = serializers.IntegerField(read_only=True)
    prod_items = ProdItemSerializer(source='prod_item', many=True, read_only=True)

    driver_signature = serializers.CharField(required=False, write_only=True)
    evaluator_signature = serializers.CharField(required=False, write_only=True)
    company_rep_signature = serializers.CharField(required=False, write_only=True)

    def to_representation(self, instance):
        response = super(SafeDriveProdSerializer, self).to_representation(instance)
        response['student'] = StudentDetailSerializer(instance.test.student).data
        if instance.driver_signature:
            response['driver_signature'] = instance.driver_signature.url
        else:
            response['driver_signature'] = None
        if instance.evaluator_signature:
            response['evaluator_signature'] = instance.evaluator_signature.url
        else:
            response['evaluator_signature'] = None

        if instance.company_rep_signature:
            response['company_rep_signature'] = instance.company_rep_signature.url
        else:
            response['company_rep_signature'] = None
        return response

    class Meta:
        model = SafeDriveProd
        fields = '__all__'

    def update(self, instance, validated_data):
        super(SafeDriveProdSerializer, self).update(instance, validated_data)
        data = self.context['request'].data
        query_params = self.context['request'].GET

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

        if 'delete_items' in query_params and query_params.get('delete_items') != "":
            delete_items = [int(ID) for ID in query_params.get('delete_items').split(',') if ID.isdigit()]
            # print(delete_items)
            try:
                ProdItem.objects.filter(prod=instance, id__in=delete_items).delete()
            except:
                pass

        prod_item_serializer = ProdItemSerializer()
        if 'prod_items' in data:
            prod_items = data['prod_items']
            for item in prod_items:
                if 'id' in item:
                    try:
                        item_obj = ProdItem.objects.get(id=item['id'])
                        # print(item_obj)
                        if item_obj:
                            # item.pop('id')
                            prod_item_serializer.update(item_obj, item)

                    except ProdItem.DoesNotExist:
                        # print('no item')
                        ProdItem.objects.create(prod=instance, **item)
                else:
                    ProdItem.objects.create(prod=instance, **item)
        return instance


class NoteInReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = SafeDriveNote
        fields = ['id', 'student', 'note', 'created', 'updated']


class EquipReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class EyeReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafeDriveEye
        fields = '__all__'


class ProdReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafeDriveProd
        fields = '__all__'
