import urllib

from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django_filters.filters import *
from rangefilter.filter import DateRangeFilter
from users.forms import UserChangeForm, UserCreationForm
from .models import *

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
            }
        ),
        (
            None, {
                'classes': ('wide',),
                'fields': ('is_superuser', 'is_staff', 'is_student', 'is_instructor', 'is_active')
            }
        ),
    )
    # fieldsets = (
    #                 ("User", {"fields": ()}),
    #                 ("Permissions", {"fields": ("is_student", "is_instructor")}),
    #             ) + auth_admin.UserAdmin.fieldsets
    fieldsets = (
        ('User', {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'middle_name',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_student', 'is_instructor', 'is_active')}),
        ('Groups', {'fields': ('groups',)}),
        ('User Permissions', {'fields': ('user_permissions',)}),
        ('Important Dates', {'fields': ('last_login', 'date_joined',)}),
    )
    list_display = ["username", "full_name", "email", "is_superuser", "is_staff", "is_student", "is_instructor",
                    "date_joined"]
    list_editable = ("is_superuser", "is_staff", "is_student", "is_instructor",)
    search_fields = ["first_name", "last_name", "email", "username", "is_instructor"]
    date_hierarchy = 'date_joined'
    list_filter = (
        ("date_joined", DateRangeFilter),
        "is_superuser", "is_staff", "is_student", "is_instructor", "is_active",

    )

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if 'autocomplete' in request.path and 'safe_driver/company' in request.META.get('HTTP_REFERER', ''):
            queryset = queryset.filter(is_instructor=True)
        return queryset, use_distinct
