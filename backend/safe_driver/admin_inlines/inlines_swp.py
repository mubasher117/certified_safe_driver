from django.contrib import admin
from safe_driver.models import (
    SWPEmployeesInterview,
    SWPPowerEquipment,
    SWPJobSetup,
    SWPExpectTheUnexpected,
    SWPPushingAndPulling,
    SWPEndRangeMotion,
    SWPKeysLiftingAndLowering,
    SWPCuttingHazardsAndSharpObjects,
    SWPKeysToAvoidingSlipsAndFalls
)

swp_inlines = []


class SWPEmployeesInterviewInline(admin.TabularInline):
    model = SWPEmployeesInterview


swp_inlines += [SWPEmployeesInterviewInline]


class SWPPowerEquipmentInline(admin.TabularInline):
    model = SWPPowerEquipment


swp_inlines += [SWPPowerEquipmentInline]


class SWPJobSetupInline(admin.TabularInline):
    model = SWPJobSetup


swp_inlines += [SWPJobSetupInline]


class SWPExpectTheUnexpectedInline(admin.TabularInline):
    model = SWPExpectTheUnexpected


swp_inlines += [SWPExpectTheUnexpectedInline]


class SWPPushingAndPullingInline(admin.TabularInline):
    model = SWPPushingAndPulling


swp_inlines += [SWPPushingAndPullingInline]


class SWPEndRangeMotionInline(admin.TabularInline):
    model = SWPEndRangeMotion


swp_inlines += [SWPEndRangeMotionInline]


class SWPKeysLiftingAndLoweringInline(admin.TabularInline):
    model = SWPKeysLiftingAndLowering


swp_inlines += [SWPKeysLiftingAndLoweringInline]


class SWPCuttingHazardsAndSharpObjectsInline(admin.TabularInline):
    model = SWPCuttingHazardsAndSharpObjects


swp_inlines += [SWPCuttingHazardsAndSharpObjectsInline]


class SWPKeysToAvoidingSlipsAndFallsnline(admin.TabularInline):
    model = SWPKeysToAvoidingSlipsAndFalls


swp_inlines += [SWPKeysToAvoidingSlipsAndFallsnline]
