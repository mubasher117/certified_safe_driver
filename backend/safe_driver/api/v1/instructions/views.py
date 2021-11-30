import json

from django.core import serializers
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *
from safe_driver.models import *


class InstructionsListBTWClassA(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    @staticmethod
    def get(request, *args, **kwargs):
        instructions = InstructionBTWClassA.objects.all().order_by('field_name')
        serializer = InstructionBTWClassASerializer(instructions, many=True)
        if serializer:
            return Response(serializer.data)
        return Response(status=400)


class InstructionsListBTWClassB(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]

    @staticmethod
    def get(request, *args, **kwargs):
        instructions = InstructionBTWClassB.objects.all().order_by('field_name')
        serializer = InstructionBTWClassBSerializer(instructions, many=True)
        if serializer:
            return Response(serializer.data)
        return Response(status=400)


class InstructionsListBTWClassC(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]

    @staticmethod
    def get(request, *args, **kwargs):
        instructions = InstructionBTWClassC.objects.all().order_by('field_name')
        serializer = InstructionBTWClassCSerializer(instructions, many=True)
        if serializer:
            return Response(serializer.data)
        return Response(status=400)


class InstructionsListBTWClassP(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]

    @staticmethod
    def get(request, *args, **kwargs):
        instructions = InstructionBTWClassP.objects.all().order_by('field_name')
        serializer = InstructionBTWClassPSerializer(instructions, many=True)
        if serializer:
            return Response(serializer.data)
        return Response(status=400)


class InstructionsListBTWBus(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]

    @staticmethod
    def get(request, *args, **kwargs):
        instructions = InstructionBTWBus.objects.all().order_by('field_name')
        serializer = InstructionBTWBusSerializer(instructions, many=True)
        if serializer:
            return Response(serializer.data)
        return Response(status=400)


# pre trips
class InstructionsListPreTripClassA(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]

    @staticmethod
    def get(request, *args, **kwargs):
        instructions = InstructionPreTripClassA.objects.all().order_by('field_name')
        serializer = InstructionPreTripClassASerializer(instructions, many=True)
        if serializer:
            return Response(serializer.data)
        return Response(status=400)


class InstructionsListPreTripClassB(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]

    @staticmethod
    def get(request, *args, **kwargs):
        instructions = InstructionPreTripClassB.objects.all().order_by('field_name')
        serializer = InstructionPreTripClassBSerializer(instructions, many=True)
        if serializer:
            return Response(serializer.data)
        return Response(status=400)


class InstructionsListPreTripClassC(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]

    @staticmethod
    def get(request, *args, **kwargs):
        instructions = InstructionPreTripClassC.objects.all().order_by('field_name')
        serializer = InstructionPreTripClassCSerializer(instructions, many=True)
        if serializer:
            return Response(serializer.data)
        return Response(status=400)


class InstructionsListPreTripClassP(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]

    @staticmethod
    def get(request, *args, **kwargs):
        instructions = InstructionPreTripClassP.objects.all().order_by('field_name')
        serializer = InstructionPreTripClassPSerializer(instructions, many=True)
        if serializer:
            return Response(serializer.data)
        return Response(status=400)


class InstructionsListPreTripBus(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]

    @staticmethod
    def get(request, *args, **kwargs):
        instructions = InstructionPreTripBus.objects.all().order_by('field_name')
        serializer = InstructionPreTripBusSerializer(instructions, many=True)
        if serializer:
            return Response(serializer.data)
        return Response(status=400)


# vrt
class InstructionsListVRT(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]

    @staticmethod
    def get(request, *args, **kwargs):
        instructions = InstructionVRT.objects.all().order_by('field_name')
        serializer = InstructionVRTSerializer(instructions, many=True)
        if serializer:
            return Response(serializer.data)
        return Response(status=400)


# swp
class InstructionsListSWP(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]

    @staticmethod
    def get(request, *args, **kwargs):
        instructions = InstructionSWP.objects.all().order_by('field_name')
        serializer = InstructionSWPSerializer(instructions, many=True)
        if serializer:
            return Response(serializer.data)
        return Response(status=400)
