from django.contrib.auth import get_user_model
from rest_framework import serializers

from safe_driver.api.v1.btw_serializers import SafeDriveBTWSerializer
from safe_driver.api.v1.pas_serializers import PassengerVehiclesSerializer
from safe_driver.api.v1.pretrip_serializers import SafeDrivePreTripSerializer
from safe_driver.api.v1.serializers import EquipReportSerializer, EyeReportSerializer, \
    NoteInReportSerializers, ProdReportSerializer
from safe_driver.api.v1.swp_serializers import SafeDriveSWPSerializer
from safe_driver.api.v1.vrt_serializers import SafeDriveVRTSerializer
from safe_driver.models import Equipment, SafeDriveEye, SafeDriveNote, SafeDriveProd, \
    SafeDrivePreTrip, SafeDriveBTW, SafeDriveSWP, VehicleRoadTest, PassengerVehicles

User = get_user_model()


class StudentReportSerializer(serializers.ModelSerializer):
    # info = StudentInfoSerializer(source='student_info', read_only=True)
    # info = serializers.SerializerMethodField(method_name='get_info', read_only=True)
    equip = serializers.SerializerMethodField(method_name='get_equip', read_only=True)
    eye = serializers.SerializerMethodField(method_name='get_eye', read_only=True)
    notes = serializers.SerializerMethodField(method_name='get_notes', read_only=True)
    prod = serializers.SerializerMethodField(method_name='get_prod', read_only=True)
    pre_trip = serializers.SerializerMethodField(method_name='get_pretrip', read_only=True)
    btw = serializers.SerializerMethodField(method_name='get_btw', read_only=True)
    swp = serializers.SerializerMethodField(method_name='get_swp', read_only=True)
    vrt = serializers.SerializerMethodField(method_name='get_vrt', read_only=True)
    pas = serializers.SerializerMethodField(method_name='get_pas', read_only=True)

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('password', 'groups', 'user_permissions')

        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
        }

    # def get_info(self, instance):
    #     try:
    #         student_info = StudentInfo.objects.select_related(
    #             'company', 'instructor'
    #         ).get(user=instance)
    #         return StudentInfoSerializer(student_info).data
    #     except StudentInfo.DoesNotExist:
    #         return None

    def get_equip(self, instance):
        try:
            # equip_info = SafeDriveEquipment.objects.get(student=instance)
            return EquipReportSerializer(instance.equip_student).data
        except Equipment.DoesNotExist:
            return None

    def get_eye(self, instance):
        try:
            return EyeReportSerializer(instance.eye_student).data
        except SafeDriveEye.DoesNotExist:
            return None

    def get_notes(self, instance):
        try:
            return NoteInReportSerializers(instance.note_student, many=True).data
        except SafeDriveNote.DoesNotExist:
            return None

    def get_prod(self, instance):
        try:
            return ProdReportSerializer(instance.prod_student).data
        except SafeDriveProd.DoesNotExist:
            return None

    def get_pretrip(self, instance):
        try:
            pretrip_info = SafeDrivePreTrip.objects.select_related(
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
            ).get(student=instance)
            return SafeDrivePreTripSerializer(pretrip_info).data
        except SafeDrivePreTrip.DoesNotExist:
            return None

    def get_btw(self, instance):
        try:
            btw_info = SafeDriveBTW.objects.select_related(
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
            ).get(student=instance)
            return SafeDriveBTWSerializer(btw_info).data
        except SafeDriveBTW.DoesNotExist:
            return None

    def get_swp(self, instance):
        try:
            swp_info = SafeDriveSWP.objects.select_related(
                'swpemployeesinterview',
                'swppowerequipment',
                'swpjobsetup',
                'swpexpecttheunexpected',
                'swppushingandpulling',
                'swpendrangemotion',
                'swpkeysliftingandlowering',
                'swpcuttinghazardsandsharpobjects',
                'swpkeystoavoidingslipsandfalls',
            ).get(student=instance)
            return SafeDriveSWPSerializer(swp_info).data
        except SafeDriveSWP.DoesNotExist:
            return None

    def get_vrt(self, instance):
        try:
            vrt_info = VehicleRoadTest.objects.select_related(
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
            ).get(student=instance)
            return SafeDriveVRTSerializer(vrt_info).data
        except VehicleRoadTest.DoesNotExist:
            return None

    def get_pas(self, instance):
        try:
            pas_info = PassengerVehicles.objects.select_related(
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
            ).get(student=instance)
            return PassengerVehiclesSerializer(pas_info).data

        except PassengerVehicles.DoesNotExist:
            return None
