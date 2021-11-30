from django.contrib.auth import get_user_model
from rest_framework import serializers

from safe_driver.models import StudentTestInfo, StudentTestNote, StudentTest, InstructorProfile, Company, StudentInfo

# from safe_driver.api.v1.student_serializers import StudentInfoSerializer

# from safe_driver.api.v1.serializers import (StudentTestSerializer)


User = get_user_model()


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        depth = 1


class InstructorProfileSerializer(serializers.ModelSerializer):
    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['company'] = CompanySerializer(instance.company).data
    #     return ret

    class Meta:
        model = InstructorProfile
        fields = '__all__'


class StudentTestSerializerInline(serializers.ModelSerializer):
    class Meta:
        model = StudentTest
        fields = '__all__'


class StudentTestInfoSerializer(serializers.ModelSerializer):
    test = StudentTestSerializerInline(read_only=True)

    # instructor = InstructorProfileSerializer(read_only=True)
    # company = CompanySerializer(read_only=True)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        try:
            from safe_driver.api.v1.serializers import StudentInfoSerializer
            response['info'] = StudentInfoSerializer(instance.test.student.student_info,
                                                     read_only=True).data
        except StudentInfo.DoesNotExist:
            response['info'] = None
        if instance.instructor:
            from users.api.v1.serializers import UserInstructorSerializer
            response['instructor'] = UserInstructorSerializer(instance.test.instructor).data
        else:
            response['instructor'] = None

        return response

    class Meta:
        model = StudentTestInfo
        fields = '__all__'

    # def update(self, instance, validated_data):


class StudentTestNoteSerializer(serializers.ModelSerializer):
    test = StudentTestSerializerInline(read_only=True)

    class Meta:
        model = StudentTestNote
        fields = '__all__'


class StudentTestNoteCreateSerializer(serializers.ModelSerializer):
    test = StudentTestSerializerInline(read_only=True)
    image = serializers.CharField(required=False, write_only=True)

    def to_representation(self, instance):
        res = super(StudentTestNoteCreateSerializer, self).to_representation(instance)
        if instance.image:
            res['image'] = self.context['request'].build_absolute_uri(instance.image.url)
        else:
            res['image'] = None
        return res

    class Meta:
        model = StudentTestNote
        fields = '__all__'

    def create(self, validated_data):
        if 'image' in validated_data:
            image = validated_data.pop('image')
            from safe_driver.image_functions import base64_to_image_content
            image_content_file = base64_to_image_content(image)
            validated_data['image'] = image_content_file

        return super(StudentTestNoteCreateSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        request_data = self.context['request'].data
        if 'image' in request_data:
            image = request_data.get('image')
            if image == "" or image is None:
                instance.image = None
                instance.save()
        if 'image' in validated_data:
            image = validated_data.pop('image')
            if image != "":
                from safe_driver.image_functions import base64_to_image_content
                image_content_file = base64_to_image_content(image)
                validated_data['image'] = image_content_file

        return super(StudentTestNoteCreateSerializer, self).update(instance, validated_data)
