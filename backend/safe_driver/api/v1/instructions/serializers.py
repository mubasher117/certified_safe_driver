from rest_framework import serializers

from safe_driver.models import *


class InstructionBTWClassASerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionBTWClassA
        fields = '__all__'


class InstructionBTWClassBSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionBTWClassB
        fields = '__all__'


class InstructionBTWClassCSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionBTWClassC
        fields = '__all__'


class InstructionBTWClassPSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionBTWClassP
        fields = '__all__'


class InstructionBTWBusSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionBTWBus
        fields = '__all__'


# pre trips
class InstructionPreTripClassASerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionPreTripClassA
        fields = '__all__'


class InstructionPreTripClassBSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionPreTripClassB
        fields = '__all__'


class InstructionPreTripClassCSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionPreTripClassC
        fields = '__all__'


class InstructionPreTripClassPSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionPreTripClassP
        fields = '__all__'


class InstructionPreTripBusSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionPreTripBus
        fields = '__all__'


class InstructionVRTSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionVRT
        fields = '__all__'


class InstructionSWPSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionSWP
        fields = '__all__'
