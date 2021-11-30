from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from safe_driver.models import *
from .functions import *


def class_a_field_names(model):
    field_list = []
    fields = model._meta.get_fields()

    for field in fields:
        try:
            related_model = model._meta.get_field(str(field.name)).related_model
            related_fields = related_model._meta.get_fields()
            if related_fields:
                for rel_field in related_fields:
                    # print(rel_field.verbose_name)
                    if rel_field.get_internal_type() == 'IntegerField':
                        field_list.append(
                            (rel_field.name, rel_field.verbose_name)
                        )
        except:
            pass
    return field_list


def html_field_data(my_model):
    field_list = []
    fields = my_model._meta.get_fields()

    for field in fields:
        try:
            related_model = my_model._meta.get_field(str(field.name)).related_model
            db_table = related_model._meta.db_table
            model_name = related_model._meta.verbose_name.title()
            related_fields = related_model._meta.get_fields()
            if related_fields:
                model_data = {
                    'db_table': db_table,
                    'title': model_name,
                    'data': []
                }
                for rel_field in related_fields:
                    # print(rel_field.get_internal_type())
                    if rel_field.get_internal_type() == 'IntegerField':
                        model_data['data'].append({
                            'title': rel_field.verbose_name,
                            'field': rel_field.name,
                        })
                field_list.append(model_data)
        except:
            pass
    # print(field_list)
    html_content = render_to_string('fields/field_list.html', {'fields': field_list})
    # print(html_content)

    return mark_safe(html_content)


def model_field_list(my_model):
    field_list = []
    fields = my_model._meta.get_fields()

    for field in fields:
        try:
            related_model = my_model._meta.get_field(str(field.name)).related_model
            db_table = related_model._meta.db_table
            model_name = related_model._meta.verbose_name.title()
            related_fields = related_model._meta.get_fields()
            if related_fields:
                model_data = {
                    'db_table': db_table,
                    'title': model_name,
                    'data': []
                }
                for rel_field in related_fields:
                    # print(rel_field.get_internal_type())
                    if rel_field.get_internal_type() == 'IntegerField':
                        model_data['data'].append({
                            'title': rel_field.verbose_name,
                            'field': rel_field.name,
                        })
                field_list.append(model_data)
        except:
            pass
    return field_list


class BTWClassAFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(BTWClassAFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = class_a_field_names(BTWClassA)

    class Meta:
        model = AccidentProbabilityValueBTWClassA
        fields = '__all__'


class BTWClassBFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(BTWClassBFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = class_a_field_names(BTWClassB)

    class Meta:
        model = AccidentProbabilityValueBTWClassB
        fields = '__all__'


class BTWClassCFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(BTWClassCFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = class_a_field_names(BTWClassC)

    class Meta:
        model = AccidentProbabilityValueBTWClassC
        fields = '__all__'


class BTWClassPFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(BTWClassPFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = class_a_field_names(BTWClassP)

    class Meta:
        model = AccidentProbabilityValueBTWClassP
        fields = '__all__'


class BTWBusFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(BTWBusFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = class_a_field_names(BTWBus)

    class Meta:
        model = AccidentProbabilityValueBTWBus
        fields = '__all__'


# pretrips
class PreTripClassAFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(PreTripClassAFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = class_a_field_names(PreTripClassA)

    class Meta:
        model = AccidentProbabilityValuePreTripClassA
        fields = '__all__'


class PreTripClassBFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(PreTripClassBFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = class_a_field_names(PreTripClassB)

    class Meta:
        model = AccidentProbabilityValuePreTripClassB
        fields = '__all__'


class PreTripClassCFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(PreTripClassCFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = class_a_field_names(PreTripClassC)

    class Meta:
        model = AccidentProbabilityValuePreTripClassC
        fields = '__all__'


# class p
class PreTripClassPFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = class_a_field_names(PreTripClassP)

    class Meta:
        model = AccidentProbabilityValuePreTripClassP
        fields = '__all__'


class PreTripBusFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(PreTripBusFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = class_a_field_names(PreTripBus)

    class Meta:
        model = AccidentProbabilityValuePreTripBus
        fields = '__all__'


class SWPInjuryProbabiltyFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())
    db_table = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(SWPInjuryProbabiltyFrom, self).__init__(*args, **kwargs)
        # self.fields['field_name'].choices = class_a_field_names(SafeDriveSWP)
        self.fields['db_table'].choices = db_table_list(SafeDriveSWP)
        self.fields['field_name'].choices = model_integer_field_names_with_boolean(SafeDriveSWP)

    class Meta:
        model = InjuryProbabilityValueSWP
        fields = '__all__'
