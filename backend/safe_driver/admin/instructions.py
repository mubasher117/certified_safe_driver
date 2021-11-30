from django.contrib import admin
from import_export import resources
from import_export.admin import ImportMixin, ImportExportMixin

from safe_driver.models import *
from .instruction_forms import *
from .functions import *


class InstructionBTWClassAResource(resources.ModelResource):
    class Meta:
        model = InstructionBTWClassA


@admin.register(InstructionBTWClassA)
class AdminInstructionBTWClassA(ImportExportMixin, admin.ModelAdmin):
    list_display = ['field_name', 'instruction']
    readonly_fields = ['get_field_names']

    form = InstructionBTWClassAFrom

    def get_field_names(self, instance):
        return html_field_data(BTWClassA)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_fields_instructions.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminInstructionBTWClassA, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['field_list'] = model_field_list(BTWClassA)
        return ctx


@admin.register(InstructionBTWClassB)
class AdminInstructionBTWClassB(ImportExportMixin, admin.ModelAdmin):
    list_display = ['field_name', 'instruction']
    readonly_fields = ['get_field_names']

    form = InstructionBTWClassBFrom

    def get_field_names(self, instance):
        return html_field_data(BTWClassB)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_fields_instructions.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminInstructionBTWClassB, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['field_list'] = model_field_list(BTWClassB)
        return ctx


@admin.register(InstructionBTWClassC)
class AdminInstructionBTWClassC(ImportExportMixin, admin.ModelAdmin):
    list_display = ['field_name', 'instruction']
    readonly_fields = ['get_field_names']

    form = InstructionBTWClassCFrom

    def get_field_names(self, instance):
        return html_field_data(BTWClassC)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_fields_instructions.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminInstructionBTWClassC, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['field_list'] = model_field_list(BTWClassC)
        return ctx


@admin.register(InstructionBTWClassP)
class AdminInstructionBTWClassP(ImportExportMixin, admin.ModelAdmin):
    list_display = ['field_name', 'instruction']
    readonly_fields = ['get_field_names']

    form = InstructionBTWClassPFrom

    def get_field_names(self, instance):
        return html_field_data(BTWClassP)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_fields_instructions.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminInstructionBTWClassP, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['field_list'] = model_field_list(BTWClassP)
        return ctx


@admin.register(InstructionBTWBus)
class AdminInstructionBTWBus(ImportExportMixin, admin.ModelAdmin):
    list_display = ['field_name', 'instruction']
    readonly_fields = ['get_field_names']

    form = InstructionBTWBusFrom

    def get_field_names(self, instance):
        return html_field_data(BTWBus)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_fields_instructions.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminInstructionBTWBus, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['field_list'] = model_field_list(BTWBus)
        return ctx


#  pretrips
@admin.register(InstructionPreTripClassA)
class AdminInstructionPreTripClassA(ImportExportMixin, admin.ModelAdmin):
    list_display = ['field_name', 'instruction']
    readonly_fields = ['get_field_names']

    form = InstructionPreTripClassAFrom

    def get_field_names(self, instance):
        return html_field_data(PreTripClassA)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_fields_instructions.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminInstructionPreTripClassA, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['field_list'] = model_field_list(PreTripClassA)
        return ctx


@admin.register(InstructionPreTripClassB)
class AdminInstructionPreTripClassB(ImportExportMixin, admin.ModelAdmin):
    list_display = ['field_name', 'instruction']
    readonly_fields = ['get_field_names']

    form = InstructionPreTripClassBFrom

    def get_field_names(self, instance):
        return html_field_data(PreTripClassB)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_fields_instructions.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminInstructionPreTripClassB, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['field_list'] = model_field_list(PreTripClassB)
        return ctx


@admin.register(InstructionPreTripClassC)
class AdminInstructionPreTripClassC(ImportExportMixin, admin.ModelAdmin):
    list_display = ['field_name', 'instruction']
    readonly_fields = ['get_field_names']

    form = InstructionPreTripClassCFrom

    def get_field_names(self, instance):
        return html_field_data(PreTripClassC)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_fields_instructions.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminInstructionPreTripClassC, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['field_list'] = model_field_list(PreTripClassC)
        return ctx


@admin.register(InstructionPreTripClassP)
class AdminInstructionPreTripClassP(ImportExportMixin, admin.ModelAdmin):
    list_display = ['field_name', 'instruction']
    readonly_fields = ['get_field_names']

    form = InstructionPreTripClassPFrom

    def get_field_names(self, instance):
        return html_field_data(PreTripClassP)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_fields_instructions.html'

    def get_context_data(self, **kwargs):
        ctx = super(self.__class__, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['field_list'] = model_field_list(PreTripClassP)
        return ctx


@admin.register(InstructionPreTripBus)
class AdminInstructionPreTripBus(ImportExportMixin, admin.ModelAdmin):
    list_display = ['field_name', 'instruction']
    readonly_fields = ['get_field_names']

    form = InstructionPreTripBusFrom

    def get_field_names(self, instance):
        return html_field_data(PreTripBus)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_fields_instructions.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminInstructionPreTripBus, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['field_list'] = model_field_list(PreTripBus)
        return ctx


# vrt
@admin.register(InstructionVRT)
class AdminInstructionVRT(ImportExportMixin, admin.ModelAdmin):
    list_display = ['field_name', 'instruction']
    readonly_fields = ['get_field_names']

    form = InstructionVRTFrom

    def get_field_names(self, instance):
        return html_field_data(VehicleRoadTest)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_fields_instructions.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminInstructionVRT, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['field_list'] = model_field_list(VehicleRoadTest)
        return ctx


# swp
@admin.register(InstructionSWP)
class AdminInstructionSWP(ImportExportMixin, admin.ModelAdmin):
    list_display = ['field_name', 'instruction']
    readonly_fields = ['get_field_names']

    form = InstructionSWPFrom

    def get_field_names(self, instance):
        return html_field_data_with_boolean(SafeDriveSWP)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_fields_instructions.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminInstructionSWP, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['field_list'] = model_field_list_with_boolean(SafeDriveSWP)
        return ctx
