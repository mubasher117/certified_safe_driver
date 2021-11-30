from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelectMultiple
from django.db.models import Q
from django.urls import reverse
from users.models import User
from ..models import *


class SWPAdminForm(forms.ModelForm):
    class Meta:
        model = SafeDriveSWP
        fields = '__all__'


class VehicleRoadTestAdminForm(forms.ModelForm):
    class Meta:
        model = VehicleRoadTest
        fields = '__all__'


class UserAutocompleteSelectMultiple(AutocompleteSelectMultiple):
    def get_url(self):
        model = User
        return reverse(self.url_name % (self.admin_site.name, model._meta.app_label, model._meta.model_name))


class UserMultipleChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, queryset=None, widget=None, **kwargs):
        if queryset is None:
            queryset = User.objects.filter(Q(is_superuser=True) | Q(is_instructor=True))
        if widget is None:
            widget = UserAutocompleteSelectMultiple(None, admin.site)  # pass `None` for `rel`
        super().__init__(queryset, widget=widget, **kwargs)


class CompanyAdminForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
