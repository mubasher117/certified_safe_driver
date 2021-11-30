from django.contrib import admin
from import_export.admin import ImportMixin
from .probability_chart_form import *
from .functions import *
from ..utils import DeleteAllMixin


def import_excel_format_html(my_model=None, choices=None):
    # field_keys = class_a_field_names(my_model)
    html_content = render_to_string('import/import_sample_format.html', {
        'sample_data': None, 'choices': choices})
    return mark_safe(html_content)


@admin.register(AccidentProbabilityValueBTWClassA)
class AdminAccidentProbabilityValueBTWClassA(ImportMixin, admin.ModelAdmin):
    list_display = ['key', 'field_name', 'db_table', 'value', ]
    form = BTWClassAFrom
    readonly_fields = ['get_field_names']
    search_fields = ['key', 'field_name', 'db_table', 'value', ]
    list_filter = ['key', ]
    list_editable = ['value', ]

    def get_field_names(self, instance):
        return html_field_data(BTWClassA)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_field_names.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminAccidentProbabilityValueBTWClassA, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['choices'] = FACTOR_CHOICES
        ctx['field_list'] = model_field_list(BTWClassA)
        return ctx


@admin.register(AccidentProbabilityValueBTWClassB)
class AdminAccidentProbabilityValueBTWClassB(ImportMixin, admin.ModelAdmin):
    list_display = ['key', 'field_name', 'db_table', 'value', ]
    form = BTWClassBFrom
    readonly_fields = ['get_field_names']
    search_fields = ['key', 'field_name', 'db_table', 'value', ]
    list_filter = ['key', ]
    list_editable = ['value', ]

    def get_field_names(self, instance):
        return html_field_data(BTWClassB)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_field_names.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminAccidentProbabilityValueBTWClassB, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['choices'] = FACTOR_CHOICES
        ctx['field_list'] = model_field_list(BTWClassB)
        return ctx


@admin.register(AccidentProbabilityValueBTWClassC)
class AdminAccidentProbabilityValueBTWClassC(ImportMixin, admin.ModelAdmin):
    list_display = ['key', 'field_name', 'db_table', 'value', ]
    form = BTWClassCFrom
    readonly_fields = ['get_field_names']
    search_fields = ['key', 'field_name', 'db_table', 'value', ]
    list_filter = ['key', ]
    list_editable = ['value', ]

    def get_field_names(self, instance):
        return html_field_data(BTWClassC)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_field_names.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminAccidentProbabilityValueBTWClassC, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['choices'] = FACTOR_CHOICES
        ctx['field_list'] = model_field_list(BTWClassC)
        return ctx


# class p
@admin.register(AccidentProbabilityValueBTWClassP)
class AdminAccidentProbabilityValueBTWClassP(ImportMixin, admin.ModelAdmin):
    list_display = ['key', 'field_name', 'db_table', 'value', ]
    form = BTWClassPFrom
    readonly_fields = ['get_field_names']
    search_fields = ['key', 'field_name', 'db_table', 'value', ]
    list_filter = ['key', ]
    list_editable = ['value', ]

    def get_field_names(self, instance):
        return html_field_data(BTWClassP)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_field_names.html'

    def get_context_data(self, **kwargs):
        ctx = super(self.__class__, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['choices'] = FACTOR_CHOICES
        ctx['field_list'] = model_field_list(BTWClassP)
        return ctx


@admin.register(AccidentProbabilityValueBTWBus)
class AdminAccidentProbabilityValueBTWBus(ImportMixin, admin.ModelAdmin):
    list_display = ['key', 'field_name', 'db_table', 'value', ]
    form = BTWBusFrom
    readonly_fields = ['get_field_names']
    search_fields = ['key', 'field_name', 'db_table', 'value', ]
    list_filter = ['key', ]
    list_editable = ['value', ]

    def get_field_names(self, instance):
        return html_field_data(BTWBus)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_field_names.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminAccidentProbabilityValueBTWBus, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['choices'] = FACTOR_CHOICES
        ctx['field_list'] = model_field_list(BTWBus)
        return ctx


# pretrips
@admin.register(AccidentProbabilityValuePreTripClassA)
class AdminAccidentProbabilityValuePreTripClassA(ImportMixin, admin.ModelAdmin):
    list_display = ['key', 'field_name', 'db_table', 'value', ]
    form = PreTripClassAFrom
    readonly_fields = ['get_field_names']
    search_fields = ['key', 'field_name', 'db_table', 'value', ]
    list_filter = ['key', ]
    list_editable = ['value', ]

    def get_field_names(self, instance):
        return html_field_data(PreTripClassA)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_field_names.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminAccidentProbabilityValuePreTripClassA, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['choices'] = FACTOR_CHOICES_PRETRIPS
        ctx['field_list'] = model_field_list(PreTripClassA)
        return ctx


@admin.register(AccidentProbabilityValuePreTripClassB)
class AdminAccidentProbabilityValuePreTripClassB(ImportMixin, admin.ModelAdmin):
    list_display = ['key', 'field_name', 'db_table', 'value', ]
    form = PreTripClassBFrom
    readonly_fields = ['get_field_names']
    search_fields = ['key', 'field_name', 'db_table', 'value', ]
    list_filter = ['key', ]
    list_editable = ['value', ]

    def get_field_names(self, instance):
        return html_field_data(PreTripClassB)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_field_names.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminAccidentProbabilityValuePreTripClassB, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['choices'] = FACTOR_CHOICES_PRETRIPS
        ctx['field_list'] = model_field_list(PreTripClassB)
        return ctx


@admin.register(AccidentProbabilityValuePreTripClassC)
class AdminAccidentProbabilityValuePreTripClassC(ImportMixin, admin.ModelAdmin):
    list_display = ['key', 'field_name', 'db_table', 'value', ]
    form = PreTripClassCFrom
    readonly_fields = ['get_field_names']
    search_fields = ['key', 'field_name', 'db_table', 'value', ]
    list_filter = ['key', ]
    list_editable = ['value', ]

    def get_field_names(self, instance):
        return html_field_data(PreTripClassC)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_field_names.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminAccidentProbabilityValuePreTripClassC, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['choices'] = FACTOR_CHOICES_PRETRIPS
        ctx['field_list'] = model_field_list(PreTripClassC)
        return ctx


# class p
@admin.register(AccidentProbabilityValuePreTripClassP)
class AdminAccidentProbabilityValuePreTripClassP(ImportMixin, admin.ModelAdmin):
    list_display = ['key', 'field_name', 'db_table', 'value', ]
    form = PreTripClassPFrom
    readonly_fields = ['get_field_names']
    search_fields = ['key', 'field_name', 'db_table', 'value', ]
    list_filter = ['key', ]
    list_editable = ['value', ]

    def get_field_names(self, instance):
        return html_field_data(PreTripClassP)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_field_names.html'

    def get_context_data(self, **kwargs):
        ctx = super(self.__class__, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['choices'] = FACTOR_CHOICES_PRETRIPS
        ctx['field_list'] = model_field_list(PreTripClassP)
        return ctx


@admin.register(AccidentProbabilityValuePreTripBus)
class AdminAccidentProbabilityValuePreTripBus(ImportMixin, admin.ModelAdmin):
    list_display = ['key', 'field_name', 'db_table', 'value', ]
    form = PreTripBusFrom
    readonly_fields = ['get_field_names']
    search_fields = ['key', 'field_name', 'db_table', 'value', ]
    list_filter = ['key', ]
    list_editable = ['value', ]

    def get_field_names(self, instance):
        return html_field_data(PreTripBus)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_field_names.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminAccidentProbabilityValuePreTripBus, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['choices'] = FACTOR_CHOICES_PRETRIPS
        ctx['field_list'] = model_field_list(PreTripBus)
        return ctx


@admin.register(InjuryProbabilityValueSWP)
class AdminInjuryProbabilityValueSWP(ImportMixin, admin.ModelAdmin):
    list_display = ['get_db_table', 'key', 'get_field_name', 'value', ]
    form = SWPInjuryProbabiltyFrom
    readonly_fields = ['get_field_names']
    search_fields = ['key', 'field_name', 'value', ]
    list_filter = ['key', ]
    list_editable = ['value', ]

    def get_db_table(self, instance):
        choice_list = dict(db_table_list(SafeDriveSWP))
        return choice_list[instance.db_table]

    get_db_table.short_description = 'DB Table'
    get_db_table.admin_order_field = 'db_table'

    def get_field_name(self, instance):
        choice_list = dict(model_integer_field_names_with_boolean(SafeDriveSWP))
        return choice_list[instance.field_name]

    get_field_name.short_description = 'Field Name'
    get_field_name.admin_order_field = 'field_name'

    def get_field_names(self, instance):
        # return html_field_data(SafeDriveSWP)
        return html_field_data_with_boolean(SafeDriveSWP)

    get_field_names.short_description = 'Field Names'

    import_template_name = 'safe_driver/import_show_field_names.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdminInjuryProbabilityValueSWP, self).get_context_data(**kwargs)
        ctx['field_names'] = self.get_field_names(instance=None)
        ctx['choices'] = SWP_FACTOR_CHOICES
        ctx['field_list'] = model_field_list_with_boolean(SafeDriveSWP)
        # print(ctx['field_names'])
        return ctx
