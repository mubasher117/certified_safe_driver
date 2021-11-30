from rest_framework import serializers

from safe_driver.api.v1.serializers import CompanySerializer
from safe_driver.models import StudentInfo


class StudentInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = '__all__'


class StudentInfoSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = StudentInfo
        fields = '__all__'
