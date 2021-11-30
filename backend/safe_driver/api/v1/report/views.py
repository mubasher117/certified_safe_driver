# Student Report View
from django.contrib.auth import get_user_model
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from safe_driver.api.v1.report.serializers import StudentReportSerializer
from users.api.v1.permissions import InstructorPermission

User = get_user_model()


class StudentReportDetail(RetrieveAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions or InstructorPermission]
    authentication_classes = [JWTAuthentication, SessionAuthentication, ]
    serializer_class = StudentReportSerializer
    queryset = User.objects.all()

    def get_object(self):
        return User.objects.select_related(
            'student_info',
            'student_info__company',
            'student_info__instructor',
            'equip_student',
            'prod_student',
            'eye_student',
            # 'pretrip_student',
            # 'pretrip_student__pretripinsidecab',
            # 'pretrip_student__pretripcoals',
            # 'pretrip_student__pretripenginecompartment',
            # 'pretrip_student__pretripvehiclefront',
            # 'pretrip_student__pretripbothsidesvehicle',
            # 'pretrip_student__pretripvehicleortractorrear',
            # 'pretrip_student__pretripfronttrailerbox',
            # 'pretrip_student__pretripdriversidetrailerbox',
            # 'pretrip_student__pretripreartrailerbox',
            # 'pretrip_student__pretrippassengersidetrailerbox',
            # 'pretrip_student__pretripdolly',
            # 'pretrip_student__pretripcombinationvehicles',
            # 'pretrip_student__pretripcombinationvehicles__pre_trip',
            # 'pretrip_student__pretripposttrip',
            # 'btw_student',
            # # 'btw_student__btwcabsafety',
            # # 'btw_student__btwstartengine',
            # # 'btw_student__btwengineoperation',
            # # 'btw_student__btwclutchandtransmission',
            # # 'btw_student__btwcoupling',
            # # 'btw_student__btwuncoupling',
            # # 'btw_student__btwbrakesandstoppings',
            # # 'btw_student__btweyemovementandmirror',
            # # 'btw_student__btwrecognizeshazards',
            # # 'btw_student__btwlightsandsignals',
            # # 'btw_student__btwsteering',
            # # 'btw_student__btwbacking',
            # # 'btw_student__btwspeed',
            # # 'btw_student__btwintersections',
            # # 'btw_student__btwturning',
            # # 'btw_student__btwparking',
            # # 'btw_student__btwmultipletrailers',
            # # 'btw_student__btwhills',
            # # 'btw_student__btwpassing',
            # # 'btw_student__btwgeneralsafetyanddotadherence',
            # 'vrt_student',
            # 'vrt_student__vrtpretrip',
            # 'vrt_student__vrtcoupling',
            # 'vrt_student__vrtuncoupling',
            # 'vrt_student__vrtengineoperations',
            # 'vrt_student__vrtstartengine',
            # 'vrt_student__vrtuseclutch',
            # 'vrt_student__vrtuseofbrakes',
            # 'vrt_student__vrtuseoftransmission',
            # 'vrt_student__vrtbacking',
            # 'vrt_student__vrtparking',
            # 'vrt_student__vrtdrivinghabits',
            # 'vrt_student__vrtposttrip',
            # 'swp_student',
            # 'swp_student__swpemployeesinterview',
            # 'swp_student__swppowerequipment',
            # 'swp_student__swpjobsetup',
            # 'swp_student__swpexpecttheunexpected',
            # 'swp_student__swppushingandpulling',
            # 'swp_student__swpendrangemotion',
            # 'swp_student__swpkeysliftingandlowering',
            # 'swp_student__swpcuttinghazardsandsharpobjects',
            # 'swp_student__swpkeystoavoidingslipsandfalls',
            # 'pas_student',
            # 'pas_student__pascabsafety',
            # 'passtartengine',
            # 'pasengineoperation',
            # 'pasbrakesandstoppings',
            # 'paspassengersafety',
            # 'paseyemovementandmirror',
            # 'pasrecognizeshazards',
            # 'paslightsandsignals',
            # 'passteering',
            # 'pasbacking',
            # 'passpeed',
            # 'pasintersections',
            # 'pasturning',
            # 'pasparking',
            # 'pashills',
            # 'paspassing',
            # 'pasrailroadcrossing',
            # 'pasgeneralsafetyanddotadherence',
        ).get(id=self.kwargs['student_id'])

# class StudentReportDetailAPIView(APIView):
#
#     def get(self, request, *args, **kwargs):
