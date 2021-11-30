from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
CLASS_CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)


# student group
class StudentGroup(models.Model):
    name = models.CharField(_('Name'), max_length=500, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Student Group'
        verbose_name_plural = 'Student Groups'


# student info
class StudentInfo(models.Model):
    student = models.OneToOneField('users.User', on_delete=models.CASCADE, null=False, related_name='student_info')

    #     instructor = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True,
    #                                    related_name='student_instructor')
    company = models.ForeignKey('safe_driver.Company', on_delete=models.CASCADE, blank=True, null=True,
                                related_name='student_company')

    group = models.ForeignKey('safe_driver.StudentGroup', on_delete=models.CASCADE, blank=True, null=True,
                              related_name='student_group')

    #     # addresses
    cell = models.CharField(_("Cell"), default=None, blank=True, null=True, max_length=20)
    city = models.CharField(_("City"), default=None, blank=True, null=True, max_length=120)
    country = models.CharField(_("Country"), default=None, blank=True, null=True, max_length=120)
    state = models.CharField(_("State"), default=None, blank=True, null=True, max_length=120)
    territory = models.CharField(_("Territory"), default=None, blank=True, null=True, max_length=120)
    address1 = models.CharField(_("Address 1"), default=None, blank=True, null=True, max_length=120)
    address2 = models.CharField(_("Address 2"), default=None, blank=True, null=True, max_length=120)
    zip_code = models.CharField(_("ZIP Code"), default=None, blank=True, null=True, max_length=32)
    contact_name = models.CharField(_("Contact Name"), default=None, blank=True, null=True, max_length=120)
    current_user_identity = models.CharField(_("Current User Idenity"), default=None, blank=True, null=True,
                                             max_length=120)
    #     budget = models.CharField(_("Budget"), default=None, blank=True, null=True, max_length=120)
    #
    #     # categories
    #     category1_name = models.CharField(_("Category 1 Name"), default=None, blank=True, null=True, max_length=120)
    #     category1_value = models.CharField(_("Category 1 Value"), default=None, blank=True, null=True, max_length=120)
    #     category2_name = models.CharField(_("Category 2 Name"), default=None, blank=True, null=True, max_length=120)
    #     category2_value = models.CharField(_("Category 2 Value"), default=None, blank=True, null=True, max_length=120)
    #     category3_name = models.CharField(_("Category 3 Name"), default=None, blank=True, null=True, max_length=120)
    #     category3_value = models.CharField(_("Category 3 Value"), default=None, blank=True, null=True, max_length=120)
    #     category4_name = models.CharField(_("Category 4 Name"), default=None, blank=True, null=True, max_length=120)
    #     category4_value = models.CharField(_("Category 4 Value"), default=None, blank=True, null=True, max_length=120)
    #     category5_name = models.CharField(_("Category 5 Name"), default=None, blank=True, null=True, max_length=120)
    #     category5_value = models.CharField(_("Category 5 Value"), default=None, blank=True, null=True, max_length=120)
    #     category6_name = models.CharField(_("Category 6 Name"), default=None, blank=True, null=True, max_length=120)
    #     category6_value = models.CharField(_("Category 6 Value"), default=None, blank=True, null=True, max_length=120)
    #
    #     chart_ref = models.CharField(_("Chart Ref"), default=None, blank=True, null=True, max_length=120)
    #     client_name = models.CharField(_("Client Name"), default=None, blank=True, null=True, max_length=120)
    #     client_number = models.CharField(_("Client Number"), default=None, blank=True, null=True, max_length=20)
    #     customer_number = models.CharField(_("Customer Number"), default=None, blank=True, null=True, max_length=20)
    #     date_of_hire = models.DateField(_("Date of Hire"), default=None, null=True, blank=True)
    #
    #     detractors = models.CharField(_("Detractors"), default=None, blank=True, null=True,
    #                                   max_length=120)
    #     discount_item = models.CharField(_("Discount Item"), default=None, blank=True, null=True,
    #                                      max_length=120)
    #     discount_service = models.CharField(_("Discount Service"), default=None, blank=True, null=True,
    #                                         max_length=120)
    #
    # driver info
    driver_id = models.CharField(_("Driver ID"), default=None, blank=True, null=True,
                                 max_length=32)
    driver_license_number = models.CharField(_("Driver License Num"), default=None, blank=True, null=True,
                                             max_length=120)
    driver_license_state = models.CharField(_("Driver License State"), default=None, blank=True, null=True,
                                            max_length=250)
    driver_license_expire_date = models.DateField(_("Dirver License Expiration Date"), default=None, null=True,
                                                  blank=True)
    driver_eld_exempt = models.CharField(_('Driver ELD Exempt'), default=None, blank=True, null=True,
                                         max_length=120)

    endorsements = models.BooleanField(_("Endorsement"), default=False)
    driver_license_class = models.CharField(_('Driver License Class'), default=None, max_length=1,
                                            choices=CLASS_CHOICES,
                                            null=True, blank=True)
    location = models.CharField(_('Location'), max_length=32, default=None, null=True, blank=True)
    corrective_lense_required = models.BooleanField(_("Corrective Lense Required"), default=False)

    dot_expiration_date = models.DateField(_("DOT Expiration Date"), default=None, null=True, blank=True)
    driver_duty_status = models.CharField(_("Driver Duty Status"), default=None, blank=True, null=True, max_length=120)
    #     history_reviewed = models.BooleanField(_('History Reviewed'), default=False)
    #
    #     start_time = models.TimeField(_('Start Time'), default=None, null=True, blank=True, )
    #     end_time = models.TimeField(_('End Time'), default=None, null=True, blank=True, )
    #
    #     restrictions = models.CharField(_('Restrictions'), max_length=255, default=None, null=True, blank=True)
    #
    #     comments = models.CharField(_('Comments'), max_length=255, default=None, null=True, blank=True)
    #
    #     # type of training completed
    #     equipement = models.BooleanField(_('Equipment'), default=False)
    #     pre_post_trip = models.BooleanField(_('Pre/Trip - Post/Trip'), default=False)
    #     behind_the_wheel = models.BooleanField(_('Behind The Wheel'), default=False)
    #     eye_movement = models.BooleanField(_('Eye Movement'), default=False)
    #     safe_work_practice = models.BooleanField(_('Safe Work Practice'), default=False)
    #     production = models.BooleanField(_('Production'), default=False)
    #     vehicle_road_test = models.BooleanField(_('Vehicle Road Test'), default=False)
    #     passenger_evacuation = models.BooleanField(_('Passenger Evacaution'), default=False)
    #     passenger_pre_trip = models.BooleanField(_('Passenger Pre/Trip'), default=False)
    #
    #     # reason for training
    #     new_hire = models.BooleanField(_('New Hire'), default=False)
    #     near_miss = models.BooleanField(_('Near Miss'), default=False)
    #     incident_follow_up = models.BooleanField(_('Incident Follow-up'), default=False)
    #     change_job = models.BooleanField(_('Change Job'), default=False)
    #     change_of_equipment = models.BooleanField(_('Change of Equipment'), default=False)
    #     annual = models.BooleanField(_('Annual'), default=False)
    #
    #     # dates
    #     injury_date = models.DateField(_('Injury Date'), default=None, null=True, blank=True)
    #     accident_date = models.DateField(_('Accident Date'), default=None, null=True, blank=True)
    #     taw_start_date = models.DateField(_('TAW Start Date'), default=None, null=True, blank=True)
    #     taw_end_date = models.DateField(_('TAW End Date'), default=None, null=True, blank=True)
    #     lost_time_start_date = models.DateField(_('Lost Time Start Date'), default=None, null=True, blank=True)
    #     return_work_date = models.DateField(_('Return to Work Date'), default=None, null=True, blank=True)
    #
    #     employee_number = models.CharField(_("Employee Number"), default=None, blank=True, null=True, max_length=32)
    #     growth = models.CharField(_("Growth"), default=None, blank=True, null=True, max_length=32)
    #
    #     job_type = models.CharField(_("Job Type"), default=None, blank=True, null=True, max_length=32)
    #     latitude = models.FloatField(_('Latitude'), default=None, blank=True, null=True)
    #     longitude = models.FloatField(_('Longitude'), default=None, blank=True, null=True)
    #     lead_source = models.CharField(_("Lead Source"), default=None, blank=True, null=True, max_length=120)
    #     mail_code = models.CharField(_("Mail Code"), default=None, blank=True, null=True, max_length=120)
    #     national_identitfier = models.CharField(_("National Identifier"), default=None, blank=True, null=True,
    #                                             max_length=120)
    #     next_step = models.CharField(_("Next Step"), default=None, blank=True, null=True, max_length=120)
    #     notify_group_name = models.CharField(_("Notify Group Name"), default=None, blank=True, null=True, max_length=120)
    #     qouta = models.CharField(_("Quota"), default=None, blank=True, null=True, max_length=120)
    #     referral = models.CharField(_("Referral"), default=None, blank=True, null=True, max_length=120)
    #
    #     # manager
    #     manager_employee_id = models.CharField(_("Manager Employee ID"), default=None, blank=True, null=True,
    #                                            max_length=120)
    #     manager_name = models.CharField(_("Manager Name"), default=None, blank=True, null=True, max_length=120)
    #     manager_record_id = models.CharField(_("Manager Record ID"), default=None, blank=True, null=True, max_length=120)
    #
    #     sales_tax_rate_record_id = models.CharField(_("Sales Tax Rate Record ID"), default=None, blank=True, null=True,
    #                                                 max_length=120)
    #     salutation = models.CharField(_("Salutation"), default=None, blank=True, null=True, max_length=120)
    #     title = models.CharField(_("Title"), default=None, blank=True, null=True, max_length=120)
    #     url = models.URLField(_("URL"), default=None, blank=True, null=True, )
    #     user_group_name = models.CharField(_("User Group Name"), default=None, blank=True, null=True, max_length=32)
    #     timer_auto_sync = models.CharField(_("Time Auto Sync"), default=None, blank=True, null=True, max_length=120)
    #     user_identity = models.CharField(_("User Identity"), default=None, blank=True, null=True, max_length=120)
    #     user_number = models.CharField(_("User Number"), default=None, blank=True, null=True, max_length=120)
    #     user_type = models.CharField(_("User Type"), default=None, blank=True, null=True, max_length=32)
    #     user_note1 = models.TextField(_("User Note 1"), default=None, blank=True, null=True)
    #     user_note2 = models.TextField(_("User Note 2"), default=None, blank=True, null=True)
    #     value = models.CharField(_("Value"), default=None, blank=True, null=True, max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.pk

    def __str__(self):
        return "%s" % self.student.username

    class Meta:
        ordering = ('student__username',)
        verbose_name = 'Student Info'
        verbose_name_plural = 'Students Info'


#

# class TypeOfTrainingCompleted(models.Model):
#     user = models.OneToOneField('users.User', on_delete=models.CASCADE, null=False,
#                                 related_name='type_of_training_completed')
#
#     equipement = models.BooleanField(_('Equipment'), default=False)
#     pre_post_trip = models.BooleanField(_('Pre/Trip - Post/Trip'), default=False)
#     behind_the_wheel = models.BooleanField(_('Behind The Wheel'), default=False)
#     eye_movement = models.BooleanField(_('Eye Movement'), default=False)
#     safe_work_practice = models.BooleanField(_('Safe Work Practice'), default=False)
#     production = models.BooleanField(_('Production'), default=False)
#     vehicle_road_test = models.BooleanField(_('Vehicle Road Test'), default=False)
#     passenger_evacuation = models.BooleanField(_('Passenger Evacaution'), default=False)
#     passenger_pre_trip = models.BooleanField(_('Passenger Pre/Trip'), default=False)
#
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def __unicode__(self):
#         return "%s" % self.pk
#
#     def __str__(self):
#         return "%s" % self.user.username
#
#     class Meta:
#         ordering = ('user__username',)
#         verbose_name = 'Student Type of Training Completed'
#         verbose_name_plural = 'Students Type of Training Completed'
#
#
# class ReasonForTraining(models.Model):
#     user = models.OneToOneField('users.User', on_delete=models.CASCADE, null=False,
#                                 related_name='reason_for_training')
#
#     new_hire = models.BooleanField(_('New Hire'), default=False)
#     near_miss = models.BooleanField(_('Near Miss'), default=False)
#     incident_follow_up = models.BooleanField(_('Incident Follow-up'), default=False)
#     change_job = models.BooleanField(_('Change Job'), default=False)
#     change_of_equipment = models.BooleanField(_('Change of Equipment'), default=False)
#     annual = models.BooleanField(_('Annual'), default=False)
#
#     # dates
#     injury_date = models.DateField(_('Injury Date'), default=None, null=True, blank=True)
#     accident_date = models.DateField(_('Accident Date'), default=None, null=True, blank=True)
#     taw_start_date = models.DateField(_('TAW Start Date'), default=None, null=True, blank=True)
#     taw_end_date = models.DateField(_('TAW End Date'), default=None, null=True, blank=True)
#     lost_time_start_date = models.DateField(_('Lost Time Start Date'), default=None, null=True, blank=True)
#     return_work_date = models.DateField(_('Return to Work Date'), default=None, null=True, blank=True)
#
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def __unicode__(self):
#         return "%s" % self.pk
#
#     def __str__(self):
#         return "%s" % self.user.username
#
#     class Meta:
#         ordering = ('user__username',)
#         verbose_name = 'Student Reason for Training'
#         verbose_name_plural = 'Students Reason for Training'


class StudentTestInfo(models.Model):
    test = models.OneToOneField('safe_driver.StudentTest', on_delete=models.CASCADE, null=False,
                                related_name='student_test_info')
    instructor = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='student_test_info_instructor')

    location = models.CharField(_('Location'), max_length=200, default=None, null=True, blank=True)

    # addresses
    cell = models.CharField(_("Cell"), default=None, blank=True, null=True, max_length=20)
    city = models.CharField(_("City"), default=None, blank=True, null=True, max_length=120)
    country = models.CharField(_("Country"), default=None, blank=True, null=True, max_length=120)
    state = models.CharField(_("State"), default=None, blank=True, null=True, max_length=120)
    territory = models.CharField(_("Territory"), default=None, blank=True, null=True, max_length=120)
    address1 = models.CharField(_("Address 1"), default=None, blank=True, null=True, max_length=120)
    address2 = models.CharField(_("Address 2"), default=None, blank=True, null=True, max_length=120)
    zip_code = models.CharField(_("ZIP Code"), default=None, blank=True, null=True, max_length=32)
    contact_name = models.CharField(_("Contact Name"), default=None, blank=True, null=True, max_length=120)
    current_user_identity = models.CharField(_("Current User Idenity"), default=None, blank=True, null=True,
                                             max_length=120)
    budget = models.CharField(_("Budget"), default=None, blank=True, null=True, max_length=120)

    # categories
    category1_name = models.CharField(_("Category 1 Name"), default=None, blank=True, null=True, max_length=120)
    category1_value = models.CharField(_("Category 1 Value"), default=None, blank=True, null=True, max_length=120)
    category2_name = models.CharField(_("Category 2 Name"), default=None, blank=True, null=True, max_length=120)
    category2_value = models.CharField(_("Category 2 Value"), default=None, blank=True, null=True, max_length=120)
    category3_name = models.CharField(_("Category 3 Name"), default=None, blank=True, null=True, max_length=120)
    category3_value = models.CharField(_("Category 3 Value"), default=None, blank=True, null=True, max_length=120)
    category4_name = models.CharField(_("Category 4 Name"), default=None, blank=True, null=True, max_length=120)
    category4_value = models.CharField(_("Category 4 Value"), default=None, blank=True, null=True, max_length=120)
    category5_name = models.CharField(_("Category 5 Name"), default=None, blank=True, null=True, max_length=120)
    category5_value = models.CharField(_("Category 5 Value"), default=None, blank=True, null=True, max_length=120)
    category6_name = models.CharField(_("Category 6 Name"), default=None, blank=True, null=True, max_length=120)
    category6_value = models.CharField(_("Category 6 Value"), default=None, blank=True, null=True, max_length=120)

    chart_ref = models.CharField(_("Chart Ref"), default=None, blank=True, null=True, max_length=120)
    client_name = models.CharField(_("Client Name"), default=None, blank=True, null=True, max_length=120)
    client_number = models.CharField(_("Client Number"), default=None, blank=True, null=True, max_length=20)
    customer_number = models.CharField(_("Customer Number"), default=None, blank=True, null=True, max_length=20)
    date_of_hire = models.DateField(_("Date of Hire"), default=None, null=True, blank=True)

    detractors = models.CharField(_("Detractors"), default=None, blank=True, null=True,
                                  max_length=120)
    discount_item = models.CharField(_("Discount Item"), default=None, blank=True, null=True,
                                     max_length=120)
    discount_service = models.CharField(_("Discount Service"), default=None, blank=True, null=True,
                                        max_length=120)

    # # driver info
    # driver_id = models.CharField(_("Driver ID"), default=None, blank=True, null=True,
    #                              max_length=32)
    # driver_license_number = models.CharField(_("Driver License Num"), default=None, blank=True, null=True,
    #                                          max_length=120)
    # driver_license_state = models.CharField(_("Driver License State"), default=None, blank=True, null=True,
    #                                         max_length=250)
    # driver_license_expire_date = models.DateField(_("Dirver License Expiration Date"), default=None, null=True,
    #                                               blank=True)
    # driver_eld_exempt = models.CharField(_('Driver ELD Exempt'), default=None, blank=True, null=True,
    #                                      max_length=120)
    #
    # endorsements = models.BooleanField(_("Endorsement"), default=False)
    # driver_license_class = models.CharField(_('Driver License Class'), default=None, max_length=1,
    #                                         choices=CLASS_CHOICES,
    #                                         null=True, blank=True)
    # location = models.CharField(_('Location'), max_length=32, default=None, null=True, blank=True)
    # corrective_lense_required = models.BooleanField(_("Corrective Lense Required"), default=False)
    #
    # dot_expiration_date = models.DateField(_("DOT Expiration Date"), default=None, null=True, blank=True)
    # driver_duty_status = models.CharField(_("Driver Duty Status"), default=None, blank=True, null=True,
    #                                       max_length=120)
    history_reviewed = models.BooleanField(_('History Reviewed'), default=False)

    start_time = models.TimeField(_('Start Time'), default=None, null=True, blank=True, )
    end_time = models.TimeField(_('End Time'), default=None, null=True, blank=True, )

    restrictions = models.CharField(_('Restrictions'), max_length=255, default=None, null=True, blank=True)

    comments = models.CharField(_('Comments'), max_length=255, default=None, null=True, blank=True)

    # type of training completed
    equipement = models.BooleanField(_('Equipment'), default=False)
    pre_post_trip = models.BooleanField(_('Pre/Trip - Post/Trip'), default=False)
    behind_the_wheel = models.BooleanField(_('Behind The Wheel'), default=False)
    eye_movement = models.BooleanField(_('Eye Movement'), default=False)
    safe_work_practice = models.BooleanField(_('Safe Work Practice'), default=False)
    production = models.BooleanField(_('Production'), default=False)
    vehicle_road_test = models.BooleanField(_('Vehicle Road Test'), default=False)
    passenger_evacuation = models.BooleanField(_('Passenger Evacaution'), default=False)
    passenger_pre_trip = models.BooleanField(_('Passenger Pre/Trip'), default=False)

    # reason for training
    new_hire = models.BooleanField(_('New Hire'), default=False)
    near_miss = models.BooleanField(_('Near Miss'), default=False)
    incident_follow_up = models.BooleanField(_('Incident Follow-up'), default=False)
    change_job = models.BooleanField(_('Change Job'), default=False)
    change_of_equipment = models.BooleanField(_('Change of Equipment'), default=False)
    annual = models.BooleanField(_('Annual'), default=False)

    # dates
    injury_date = models.DateField(_('Injury Date'), default=None, null=True, blank=True)
    accident_date = models.DateField(_('Accident Date'), default=None, null=True, blank=True)
    taw_start_date = models.DateField(_('TAW Start Date'), default=None, null=True, blank=True)
    taw_end_date = models.DateField(_('TAW End Date'), default=None, null=True, blank=True)
    lost_time_start_date = models.DateField(_('Lost Time Start Date'), default=None, null=True, blank=True)
    return_work_date = models.DateField(_('Return to Work Date'), default=None, null=True, blank=True)

    employee_number = models.CharField(_("Employee Number"), default=None, blank=True, null=True, max_length=32)
    growth = models.CharField(_("Growth"), default=None, blank=True, null=True, max_length=32)

    job_type = models.CharField(_("Job Type"), default=None, blank=True, null=True, max_length=32)
    latitude = models.FloatField(_('Latitude'), default=None, blank=True, null=True)
    longitude = models.FloatField(_('Longitude'), default=None, blank=True, null=True)
    lead_source = models.CharField(_("Lead Source"), default=None, blank=True, null=True, max_length=120)
    mail_code = models.CharField(_("Mail Code"), default=None, blank=True, null=True, max_length=120)
    national_identitfier = models.CharField(_("National Identifier"), default=None, blank=True, null=True,
                                            max_length=120)
    next_step = models.CharField(_("Next Step"), default=None, blank=True, null=True, max_length=120)
    notify_group_name = models.CharField(_("Notify Group Name"), default=None, blank=True, null=True, max_length=120)
    qouta = models.CharField(_("Quota"), default=None, blank=True, null=True, max_length=120)
    referral = models.CharField(_("Referral"), default=None, blank=True, null=True, max_length=120)

    # manager
    manager_employee_id = models.CharField(_("Manager Employee ID"), default=None, blank=True, null=True,
                                           max_length=120)
    manager_name = models.CharField(_("Manager Name"), default=None, blank=True, null=True, max_length=120)
    manager_record_id = models.CharField(_("Manager Record ID"), default=None, blank=True, null=True, max_length=120)

    sales_tax_rate_record_id = models.CharField(_("Sales Tax Rate Record ID"), default=None, blank=True, null=True,
                                                max_length=120)
    salutation = models.CharField(_("Salutation"), default=None, blank=True, null=True, max_length=120)
    title = models.CharField(_("Title"), default=None, blank=True, null=True, max_length=120)
    url = models.URLField(_("URL"), default=None, blank=True, null=True, )
    user_group_name = models.CharField(_("User Group Name"), default=None, blank=True, null=True, max_length=32)
    timer_auto_sync = models.CharField(_("Time Auto Sync"), default=None, blank=True, null=True, max_length=120)
    user_identity = models.CharField(_("User Identity"), default=None, blank=True, null=True, max_length=120)
    user_number = models.CharField(_("User Number"), default=None, blank=True, null=True, max_length=120)
    user_type = models.CharField(_("User Type"), default=None, blank=True, null=True, max_length=32)
    user_note1 = models.TextField(_("User Note 1"), default=None, blank=True, null=True)
    user_note2 = models.TextField(_("User Note 2"), default=None, blank=True, null=True)
    value = models.CharField(_("Value"), default=None, blank=True, null=True, max_length=120)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.pk

    def __str__(self):
        return "%s" % self.test.student.username

    class Meta:
        ordering = ('test__student__username',)
        verbose_name = 'Student Test Info'
        verbose_name_plural = 'Students Test Info'
