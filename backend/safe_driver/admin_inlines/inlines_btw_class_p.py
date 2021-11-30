from django.contrib import admin
from ..models.btw_class_p import *


class BTWCabSafetyClassPInline(admin.TabularInline):
    model = BTWCabSafetyClassP


class BTWStartEngineClassPInline(admin.TabularInline):
    model = BTWStartEngineClassP


class BTWEngineOperationClassPInline(admin.TabularInline):
    model = BTWEngineOperationClassP


class BTWPassengerSafetyClassPInline(admin.TabularInline):
    model = BTWPassengerSafetyClassP


class BTWBrakesAndStoppingsClassPInline(admin.TabularInline):
    model = BTWBrakesAndStoppingsClassP


class BTWEyeMovementAndMirrorClassPInline(admin.TabularInline):
    model = BTWEyeMovementAndMirrorClassP


class BTWRecognizesHazardsClassPInline(admin.TabularInline):
    model = BTWRecognizesHazardsClassP


class BTWLightsAndSignalsClassPInline(admin.TabularInline):
    model = BTWLightsAndSignalsClassP


class BTWSteeringClassPInline(admin.TabularInline):
    model = BTWSteeringClassP


class BTWBackingClassPInline(admin.TabularInline):
    model = BTWBackingClassP


class BTWSpeedClassPInline(admin.TabularInline):
    model = BTWSpeedClassP


# 12
class BTWIntersectionsClassPInline(admin.TabularInline):
    model = BTWIntersectionsClassP


# 13
class BTWTurningClassPInline(admin.TabularInline):
    model = BTWTurningClassP


# 15
class BTWParkingClassPInline(admin.TabularInline):
    model = BTWParkingClassP


# 15
class BTWHillsClassPInline(admin.TabularInline):
    model = BTWHillsClassP


# 16
class BTWPassingClassPInline(admin.TabularInline):
    model = BTWPassingClassP


# 17
class BTWRailroadCrossingClassPInline(admin.TabularInline):
    model = BTWRailroadCrossingClassP


# 18
class BTWGeneralSafetyAndDOTAdherenceClassPInline(admin.TabularInline):
    model = BTWGeneralSafetyAndDOTAdherenceClassP


# 19
class BTWInternalEnvironmentClassPInline(admin.TabularInline):
    model = BTWInternalEnvironmentClassP
