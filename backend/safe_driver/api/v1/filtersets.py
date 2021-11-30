import django_filters
from django.contrib.auth import get_user_model
from django_filters.rest_framework import filters

User = get_user_model()


class SudentListInfoFilterSet(django_filters.FilterSet):
    state = django_filters.CharFilter(
        field_name='student_info__state',
        label='State',
        lookup_expr='icontains'
    )
    city = django_filters.CharFilter(
        field_name='student_info__city',
        label='City',
        lookup_expr='icontains'
    )
    country = django_filters.CharFilter(
        field_name='student_info__country',
        label='Country',
        lookup_expr='icontains'
    )
    territory = django_filters.CharFilter(
        field_name='student_info__territory',
        label='Territory',
        lookup_expr='icontains'
    )
    zip_code = django_filters.CharFilter(
        field_name='student_info__zip_code',
        label='Zip Code',
        lookup_expr='icontains'
    )
    driver_license_number = django_filters.CharFilter(
        field_name='student_info__driver_license_number',
        label='Driver License Number',
        lookup_expr='icontains'
    )
    driver_license_state = django_filters.CharFilter(
        field_name='student_info__driver_license_state',
        label='Driver License State',
        lookup_expr='icontains'
    )
    driver_license_expire_date = django_filters.DateFilter(
        field_name='student_info__driver_license_expire_date',
        label='Driver License Expire Date',
    )
    company_name = django_filters.CharFilter(
        field_name='student_info__company__name',
        label='Company Name',
        lookup_expr='icontains'
    )
    company_id = django_filters.CharFilter(
        field_name='student_info__company__id',
        label='Company ID',
        lookup_expr='exact'
    )
    group_name = django_filters.CharFilter(
        field_name='student_info__group__name',
        label='Group Name',
        lookup_expr='icontains'
    )
    group_id = django_filters.CharFilter(
        field_name='student_info__group__id',
        label='Group ID',
        lookup_expr='exact'
    )

    class Meta:
        model = User
        fields = {
            'sex', 'date_joined', 'date_of_birth', 'email', 'first_name',
            'home_phone_number', 'is_active', 'is_instructor', 'is_staff', 'is_student', 'is_superuser',
            'last_login', 'last_name', 'middle_name', 'mobile_number', 'phone', 'send_gps_location', 'sex',
            'surname', 'username', 'work_phone_number',
        }

    # fields = ['date_joined', 'date_of_birth', 'email', 'first_name',
    #           'home_phone_number', 'is_active', 'is_instructor', 'is_staff', 'is_student', 'is_superuser',
    #           'last_login', 'last_name', 'middle_name', 'mobile_number', 'phone', 'send_gps_location', 'sex',
    #           'surname', 'username', 'work_phone_number',
    #           'student_info__city',
    #           'student_info__state',
    #           'student_info__country',
    #           'student_info__territory',
    #           'student_info__zip_code',
    #           'student_info__customer_number',
    #           'student_info__date_of_hire',
    #           'student_info__driver_license_number',
    #           'student_info__dot_expiration_date',
    #           'student_info__manager_name',
    #           'student_info__manager_employee_id',
    #           'student_info__manager_record_id',
    #           ]


class InstructorListFilterSet(django_filters.FilterSet):
    driver_license_number = django_filters.CharFilter(
        field_name='instructor_profile__driver_license_number',
        label='Driver License Number',
        lookup_expr='icontains'
    )
    driver_license_state = django_filters.CharFilter(
        field_name='instructor_profile__driver_license_state',
        label='Driver License State',
        lookup_expr='icontains'
    )
    driver_license_expire_date = django_filters.DateFilter(
        field_name='instructor_profile__driver_license_expire_date',
        label='Driver License Expire Date',
    )
    company_name = django_filters.CharFilter(
        field_name='instructor_profile__company__name',
        label='Company Name',
        lookup_expr='icontains'
    )
    company_id = django_filters.CharFilter(
        field_name='instructor_profile__company_id',
        label='Company ID',
        lookup_expr='exact'
    )

    class Meta:
        model = User
        fields = {
            'sex', 'date_joined', 'date_of_birth', 'email', 'first_name',
            'home_phone_number', 'is_active', 'is_instructor', 'is_staff', 'is_student', 'is_superuser',
            'last_login', 'last_name', 'middle_name', 'mobile_number', 'phone', 'send_gps_location', 'sex',
            'surname', 'username', 'work_phone_number',
        }
