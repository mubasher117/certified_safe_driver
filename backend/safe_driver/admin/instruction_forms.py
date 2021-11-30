from django.contrib import admin
from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from safe_driver.models import *
# from .utils import *
from .functions import *


class InstructionBTWClassAFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(InstructionBTWClassAFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = model_integer_field_names(BTWClassA)

    class Meta:
        model = InstructionBTWClassA
        fields = '__all__'


class InstructionBTWClassBFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(InstructionBTWClassBFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = model_integer_field_names(BTWClassB)

    class Meta:
        model = InstructionBTWClassB
        fields = '__all__'


class InstructionBTWClassCFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(InstructionBTWClassCFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = model_integer_field_names(BTWClassC)

    class Meta:
        model = InstructionBTWClassC
        fields = '__all__'


class InstructionBTWClassPFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(InstructionBTWClassPFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = model_integer_field_names(BTWClassP)

    class Meta:
        model = InstructionBTWClassP
        fields = '__all__'


class InstructionBTWBusFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(InstructionBTWBusFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = model_integer_field_names(BTWBus)

    class Meta:
        model = InstructionBTWBus
        fields = '__all__'


# pretrips forms
class InstructionPreTripClassAFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(InstructionPreTripClassAFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = model_integer_field_names(PreTripClassA)

    class Meta:
        model = InstructionPreTripClassA
        fields = '__all__'


class InstructionPreTripClassBFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(InstructionPreTripClassBFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = model_integer_field_names(PreTripClassB)

    class Meta:
        model = InstructionPreTripClassB
        fields = '__all__'


class InstructionPreTripClassCFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(InstructionPreTripClassCFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = model_integer_field_names(PreTripClassC)

    class Meta:
        model = InstructionPreTripClassC
        fields = '__all__'


class InstructionPreTripClassPFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(InstructionPreTripClassPFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = model_integer_field_names(PreTripClassP)

    class Meta:
        model = InstructionPreTripClassP
        fields = '__all__'


class InstructionPreTripBusFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(InstructionPreTripBusFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = model_integer_field_names(PreTripBus)

    class Meta:
        model = InstructionPreTripBus
        fields = '__all__'


# vrt
class InstructionVRTFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(InstructionVRTFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = model_integer_field_names(VehicleRoadTest)

    class Meta:
        model = InstructionVRT
        fields = '__all__'


# swp
class InstructionSWPFrom(forms.ModelForm):
    field_name = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super(InstructionSWPFrom, self).__init__(*args, **kwargs)
        self.fields['field_name'].choices = model_integer_field_names_with_boolean(SafeDriveSWP)

    class Meta:
        model = InstructionSWP
        fields = '__all__'
