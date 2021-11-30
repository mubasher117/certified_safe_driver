from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import *


# User = get_user_model()
#
# @receiver(post_save, sender=User)


@receiver(post_save, sender=SafeDrivePreTrip)
def create_pre_trip_objects(sender, instance, created, **kwargs):
    if created:
        try:
            PreTripInsideCab.objects.create(pre_trip=instance)
        except:
            pass
        try:
            PreTripCOALS.objects.create(pre_trip=instance)
        except:
            pass

        try:
            PreTripEngineCompartment.objects.create(pre_trip=instance)
        except:
            pass

        try:
            PreTripVehicleFront.objects.create(pre_trip=instance)
        except:
            pass

        try:
            PreTripBothSidesVehicle.objects.create(pre_trip=instance)
        except:
            pass

        try:
            PreTripVehicleOrTractorRear.objects.create(pre_trip=instance)
        except:
            pass

        try:
            PreTripFrontTrailerBox.objects.create(pre_trip=instance)
        except:
            pass

        try:
            PreTripDriverSideTrailerBox.objects.create(pre_trip=instance)
        except:
            pass

        try:
            PreTripRearTrailerBox.objects.create(pre_trip=instance)
        except:
            pass

        try:
            PreTripPassengerSideTrailerBox.objects.create(pre_trip=instance)
        except:
            pass

        try:
            PreTripDolly.objects.create(pre_trip=instance)
        except:
            pass

        try:
            PreTripCombinationVehicles.objects.create(pre_trip=instance)
        except:
            pass

        try:
            PreTripPostTrip.objects.create(pre_trip=instance)
        except:
            pass


@receiver(post_save, sender=SafeDriveBTW)
def create_btw_objects_intance(sender, instance, created, **kwargs):
    if instance:
        try:
            instance.btwcabsafety
        except BTWCabSafety.DoesNotExist:
            BTWCabSafety.objects.create(btw=instance)

        try:
            instance.btwstartengine
        except BTWStartEngine.DoesNotExist:
            BTWStartEngine.objects.create(btw=instance)

        try:
            instance.btwengineoperation
        except BTWEngineOperation.DoesNotExist:
            BTWEngineOperation.objects.create(btw=instance)

        try:
            instance.btwclutchandtransmission
        except BTWClutchAndTransmission.DoesNotExist:
            BTWClutchAndTransmission.objects.create(btw=instance)

        try:
            instance.btwcoupling
        except BTWCoupling.DoesNotExist:
            BTWCoupling.objects.create(btw=instance)

        try:
            instance.btwuncoupling
        except BTWUncoupling.DoesNotExist:
            BTWUncoupling.objects.create(btw=instance)

        try:
            instance.btwbrakesandstoppings
        except BTWBrakesAndStoppings.DoesNotExist:
            BTWBrakesAndStoppings.objects.create(btw=instance)

        try:
            instance.btweyemovementandmirror
        except BTWEyeMovementAndMirror.DoesNotExist:
            BTWEyeMovementAndMirror.objects.create(btw=instance)

        try:
            instance.btwrecognizeshazards
        except BTWRecognizesHazards.DoesNotExist:
            BTWRecognizesHazards.objects.create(btw=instance)

        try:
            instance.btwlightsandsignals
        except BTWLightsAndSignals.DoesNotExist:
            BTWLightsAndSignals.objects.create(btw=instance)

        try:
            instance.btwsteering
        except BTWSteering.DoesNotExist:
            BTWSteering.objects.create(btw=instance)

        try:
            instance.btwbacking
        except BTWBacking.DoesNotExist:
            BTWBacking.objects.create(btw=instance)

        try:
            instance.btwspeed
        except BTWSpeed.DoesNotExist:
            BTWSpeed.objects.create(btw=instance)

        try:
            instance.btwintersections
        except BTWIntersections.DoesNotExist:
            BTWIntersections.objects.create(btw=instance)

        try:
            instance.btwturning
        except BTWTurning.DoesNotExist:
            BTWTurning.objects.create(btw=instance)

        try:
            instance.btwparking
        except BTWParking.DoesNotExist:
            BTWParking.objects.create(btw=instance)

        try:
            instance.btwmultipletrailers
        except BTWMultipleTrailers.DoesNotExist:
            BTWMultipleTrailers.objects.create(btw=instance)

        try:
            instance.btwhills
        except BTWHills.DoesNotExist:
            BTWHills.objects.create(btw=instance)

        try:
            instance.btwpassing
        except BTWPassing.DoesNotExist:
            BTWPassing.objects.create(btw=instance)

        try:
            instance.btwgeneralsafetyanddotadherence
        except BTWGeneralSafetyAndDOTAdherence.DoesNotExist:
            BTWGeneralSafetyAndDOTAdherence.objects.create(btw=instance)


@receiver(post_save, sender=VehicleRoadTest)
def create_vrt_objects_intance(sender, instance, created, **kwargs):
    if instance:
        try:
            instance.vrtpretrip
        except VRTPreTrip.DoesNotExist:
            VRTPreTrip.objects.create(vrt=instance)

        try:
            instance.vrtcoupling
        except VRTCoupling.DoesNotExist:
            VRTCoupling.objects.create(vrt=instance)

        try:
            instance.vrtuncoupling
        except VRTUncoupling.DoesNotExist:
            VRTUncoupling.objects.create(vrt=instance)

        try:
            instance.vrtengineoperations
        except VRTEngineOperations.DoesNotExist:
            VRTEngineOperations.objects.create(vrt=instance)

        try:
            instance.vrtstartengine
        except VRTStartEngine.DoesNotExist:
            VRTStartEngine.objects.create(vrt=instance)

        try:
            instance.vrtuseclutch
        except VRTUseClutch.DoesNotExist:
            VRTUseClutch.objects.create(vrt=instance)

        try:
            instance.vrtuseoftransmission
        except VRTUseOfTransmission.DoesNotExist:
            VRTUseOfTransmission.objects.create(vrt=instance)

        try:
            instance.vrtuseofbrakes
        except VRTUseOfBrakes.DoesNotExist:
            VRTUseOfBrakes.objects.create(vrt=instance)

        try:
            instance.vrtbacking
        except VRTBacking.DoesNotExist:
            VRTBacking.objects.create(vrt=instance)

        try:
            instance.vrtparking
        except VRTParking.DoesNotExist:
            VRTParking.objects.create(vrt=instance)

        try:
            instance.vrtdrivinghabits
        except VRTDrivingHabits.DoesNotExist:
            VRTDrivingHabits.objects.create(vrt=instance)

        try:
            instance.vrtposttrip
        except VRTPostTrip.DoesNotExist:
            VRTPostTrip.objects.create(vrt=instance)


@receiver(post_save, sender=PassengerVehicles)
def create_pas_objects_intance(sender, instance, created, **kwargs):
    if instance:
        try:
            instance.pascabsafety
        except PASCabSafety.DoesNotExist:
            PASCabSafety.objects.create(pas=instance)

        try:
            instance.passtartengine
        except PASStartEngine.DoesNotExist:
            PASStartEngine.objects.create(pas=instance)

        try:
            instance.pasengineoperation
        except PASEngineOperation.DoesNotExist:
            PASEngineOperation.objects.create(pas=instance)

        try:
            instance.pasbrakesandstoppings
        except PASBrakesAndStoppings.DoesNotExist:
            PASBrakesAndStoppings.objects.create(pas=instance)

        try:
            instance.paspassengersafety
        except PASPassengerSafety.DoesNotExist:
            PASPassengerSafety.objects.create(pas=instance)

        try:
            instance.paseyemovementandmirror
        except PASEyeMovementAndMirror.DoesNotExist:
            PASEyeMovementAndMirror.objects.create(pas=instance)

        try:
            instance.pasrecognizeshazards
        except PASRecognizesHazards.DoesNotExist:
            PASRecognizesHazards.objects.create(pas=instance)

        try:
            instance.paslightsandsignals
        except PASLightsAndSignals.DoesNotExist:
            PASLightsAndSignals.objects.create(pas=instance)

        try:
            instance.passteering
        except PASSteering.DoesNotExist:
            PASSteering.objects.create(pas=instance)

        try:
            instance.pasbacking
        except PASBacking.DoesNotExist:
            PASBacking.objects.create(pas=instance)

        try:
            instance.passpeed
        except PASSpeed.DoesNotExist:
            PASSpeed.objects.create(pas=instance)

        try:
            instance.pasintersections
        except PASIntersections.DoesNotExist:
            PASIntersections.objects.create(pas=instance)

        try:
            instance.pasturning
        except PASTurning.DoesNotExist:
            PASTurning.objects.create(pas=instance)

        try:
            instance.pasparking
        except PASParking.DoesNotExist:
            PASParking.objects.create(pas=instance)

        try:
            instance.pashills
        except PASHills.DoesNotExist:
            PASHills.objects.create(pas=instance)

        try:
            instance.paspassing
        except PASPassing.DoesNotExist:
            PASPassing.objects.create(pas=instance)

        try:
            instance.pasrailroadcrossing
        except PASRailroadCrossing.DoesNotExist:
            PASRailroadCrossing.objects.create(pas=instance)

        try:
            instance.pasgeneralsafetyanddotadherence
        except PASGeneralSafetyAndDOTAdherence.DoesNotExist:
            PASGeneralSafetyAndDOTAdherence.objects.create(pas=instance)


@receiver(post_save, sender=SafeDriveSWP)
def create_swp_objects_intance(sender, instance, created, **kwargs):
    try:
        instance.swpemployeesinterview
    except SWPEmployeesInterview.DoesNotExist:
        SWPEmployeesInterview.objects.create(swp=instance)

    try:
        instance.swppowerequipment
    except SWPPowerEquipment.DoesNotExist:
        SWPPowerEquipment.objects.create(swp=instance)

    try:
        instance.swpjobsetup
    except SWPJobSetup.DoesNotExist:
        SWPJobSetup.objects.create(swp=instance)

    try:
        instance.swpexpecttheunexpected
    except SWPExpectTheUnexpected.DoesNotExist:
        SWPExpectTheUnexpected.objects.create(swp=instance)

    try:
        instance.swppushingandpulling
    except SWPPushingAndPulling.DoesNotExist:
        SWPPushingAndPulling.objects.create(swp=instance)

    try:
        instance.swpendrangemotion
    except SWPEndRangeMotion.DoesNotExist:
        SWPEndRangeMotion.objects.create(swp=instance)

    try:
        instance.swpkeysliftingandlowering
    except SWPKeysLiftingAndLowering.DoesNotExist:
        SWPKeysLiftingAndLowering.objects.create(swp=instance)

    try:
        instance.swpcuttinghazardsandsharpobjects
    except SWPCuttingHazardsAndSharpObjects.DoesNotExist:
        SWPCuttingHazardsAndSharpObjects.objects.create(swp=instance)

    try:
        instance.swpkeystoavoidingslipsandfalls
    except SWPKeysToAvoidingSlipsAndFalls.DoesNotExist:
        SWPKeysToAvoidingSlipsAndFalls.objects.create(swp=instance)
