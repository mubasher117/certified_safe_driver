from django.db import models
from django.utils.translation import ugettext_lazy as _


NUMBER_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (0, "N/A"),
)


class Company(models.Model):
    name = models.CharField(_("Company Name"), max_length=150, default=None, null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.pk

    def __str__(self):
        return "%s" % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class StudentInfo(models.Model):
    CLASS_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )

    user = models.OneToOneField('users.User', on_delete=models.CASCADE, null=False, related_name='student_info')
    instructor = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='student_instructor')
    company = models.ForeignKey('safe_driver.Company', on_delete=models.CASCADE, blank=True, null=True,
                                related_name='student_company')

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

    # driver info
    driver_license_number = models.CharField(_("Driver License Num"), default=None, blank=True, null=True,
                                             max_length=120)
    driver_license_state = models.CharField(_("Driver License State"), default=None, blank=True, null=True,
                                            max_length=32)
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
    driver_duty_status = models.CharField(_("Driver Duty Status"), default=None, blank=True, null=True,
                                          max_length=120)
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
    longitude = models.FloatField(_('Latitude'), default=None, blank=True, null=True)
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
        return "%s" % self.user.username

    class Meta:
        ordering = ('user__username',)
        verbose_name = 'Student Info'
        verbose_name_plural = 'Students Info'


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


class SafeDriveEquipment(models.Model):
    # company = models.ForeignKey('safe_driver.Company', on_delete=models.CASCADE, related_name='equip_company',
    #                             null=True)
    #
    # instructor = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='equip_instructor',
    #                                null=True, )

    student = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='equip_student',
                                   null=False)

    # power unit
    power_unit_number = models.CharField(max_length=32, default=None, null=True, blank=True,
                                         verbose_name='Power Unit Number')
    transmission_type = models.CharField(max_length=32, default=None, null=True, blank=True,
                                         verbose_name='Permission Type')
    vehicle_type = models.CharField(max_length=32, default=None, null=True, blank=True,
                                    verbose_name='Vehicle Type')
    vehicle_type_other = models.CharField(max_length=32, default=None, null=True, blank=True,
                                          verbose_name='Vehicle Type Other')
    vehicle_manufacturer = models.CharField(max_length=32, default=None, null=True, blank=True,
                                            verbose_name='Vehicle Manufacturer')
    vehicle_manufacturer_other = models.CharField(max_length=32, default=None, null=True, blank=True,
                                                  verbose_name='Vehicle Manufacturer Other')

    # Combination Vehicle - Train or Chain
    single_trailer_length = models.CharField(max_length=32, default=None, null=True, blank=True,
                                             verbose_name='Single Trailer Length')
    single_trailer_length_other = models.CharField(max_length=32, default=None, null=True,
                                                   blank=True, verbose_name='Single Trailer Length Other')
    combination_vehicles = models.CharField(max_length=32, default=None, null=True, blank=True,
                                            verbose_name='Combination Vehicles')
    combinations_vehicles_other = models.CharField(max_length=32, default=None, null=True, blank=True,
                                                   verbose_name='Combination Vehicles Other')
    combination_vehicles_length = models.CharField(max_length=32, default=None, null=True,
                                                   blank=True, verbose_name='Combination Vehicles Other')
    combination_vehicles_length_other = models.CharField(max_length=32, default=None, null=True,
                                                         blank=True,
                                                         verbose_name='Combination Vehicles Length Other')
    dolly_or_gear_type = models.CharField(max_length=32, default=None, null=True, blank=True,
                                          verbose_name='Dolly/Gear Type')
    dolly_or_gear_type_other = models.CharField(max_length=32, default=None, null=True, blank=True,
                                                verbose_name='Dolly/Gear Type Other')

    # vehicle numbers
    trailer_1 = models.CharField(max_length=32, default=None, null=True, blank=True)
    trailer_2 = models.CharField(max_length=32, default=None, null=True, blank=True)
    trailer_3 = models.CharField(max_length=32, default=None, null=True, blank=True)
    dolly_1 = models.CharField(max_length=32, default=None, null=True, blank=True)
    dolly_2 = models.CharField(max_length=32, default=None, null=True, blank=True)
    dolly_3 = models.CharField(max_length=32, default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s Equip - %s' % (self.student.full_name, self.pk)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"


class SafeDriveNote(models.Model):
    student = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='note_student',
                                null=False)

    note = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s Note - %s' % (self.student.full_name, self.pk)

    class Meta:
        ordering = ('student__first_name', 'student__last_name', '-created',)
        verbose_name = "Note"
        verbose_name_plural = "Notes"


NUMBER_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (0, "N/A"),
)


class SafeDriveProd(models.Model):
    # company = models.ForeignKey('safe_driver.Company', on_delete=models.CASCADE, related_name='prod_company',
    #                             null=True)
    #
    # instructor = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='prod_instructor',
    #                                null=True, )

    student = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='prod_student',
                                   null=False)

    date = models.DateField(null=True, blank=True, default=None, verbose_name='Date')
    start_time = models.TimeField(null=True, blank=True, default=None, verbose_name='Start Time')
    end_time = models.TimeField(null=True, blank=True, default=None, verbose_name='End Time')

    department = models.CharField(max_length=150, null=True, blank=True, default=None, verbose_name='Department')

    # route number
    on_time = models.BooleanField(default=False, verbose_name='On Time')
    keys_ready = models.BooleanField(default=False, verbose_name='Keys Ready')
    timecard_system_ready = models.BooleanField(default=False, verbose_name='Timecard System Ready')
    equipment_ready = models.BooleanField(default=False, verbose_name='Equipment Ready')
    equipment_clean = models.BooleanField(default=False, verbose_name='Equipment Clean')

    start_odometer = models.CharField(max_length=150, null=True, blank=True, default=None,
                                      verbose_name='Start Odometer')
    finish_odometer = models.CharField(max_length=150, null=True, blank=True, default=None,
                                       verbose_name='Finish Odometer')

    miles = models.DecimalField(max_digits=4, decimal_places=2, null=True, default=None, blank=True,
                                verbose_name='Miles')

    location = models.CharField(max_length=150, null=True, blank=True, default=None, verbose_name='Location')
    trailer = models.CharField(max_length=150, null=True, blank=True, default=None, verbose_name='Trailer')

    start_work = models.IntegerField(choices=NUMBER_CHOICES, default=0, null=True, blank=True,
                                     verbose_name="Start Work")
    leave_building = models.IntegerField(choices=NUMBER_CHOICES, default=0, verbose_name="Leave Building")
    travel_path = models.IntegerField(choices=NUMBER_CHOICES, default=0, verbose_name="Travel Path")
    speed = models.IntegerField(choices=NUMBER_CHOICES, default=0, verbose_name="Speed")
    idle_time = models.IntegerField(choices=NUMBER_CHOICES, default=0, verbose_name="Idle Time")
    plan_ahead = models.IntegerField(choices=NUMBER_CHOICES, default=0, verbose_name="Plan Ahead")
    turn_around = models.IntegerField(choices=NUMBER_CHOICES, default=0, verbose_name="Turn Around")
    on_schedule = models.IntegerField(choices=NUMBER_CHOICES, default=0, verbose_name="On Schedule")
    customer_contact = models.IntegerField(choices=NUMBER_CHOICES, default=0,
                                           verbose_name="Customer Contact")
    not_ready_situations = models.IntegerField(choices=NUMBER_CHOICES, default=0,
                                               verbose_name="Not Ready Situations")
    brisk_pace = models.IntegerField(choices=NUMBER_CHOICES, default=0, verbose_name="Brisk Pace")
    finish_work = models.IntegerField(choices=NUMBER_CHOICES, default=0, verbose_name="Finish Work")

    odometer = models.CharField(max_length=150, null=True, blank=True, default=None,
                                verbose_name='Odometer')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    driver_signature = models.ImageField(upload_to='signatures/driver/', default=None, null=True, blank=True)
    evaluator_signature = models.ImageField(upload_to='signatures/evaluator/', default=None, null=True, blank=True)
    company_rep_signature = models.ImageField(upload_to='signatures/company/', default=None, null=True, blank=True)
    company_rep_name = models.CharField(max_length=150, null=True, blank=True, default=None,
                                        verbose_name='Company Rep. Name')

    observer_first_name = models.CharField(max_length=150, null=True, blank=True, default=None,
                                           verbose_name='Observer First Name')

    observer_last_name = models.CharField(max_length=150, null=True, blank=True, default=None,
                                          verbose_name='Observer Last Name')

    @property
    def total_number(self):
        total = self.start_work + self.leave_building + self.travel_path + self.speed + self.idle_time + \
                self.plan_ahead + self.turn_around + self.on_schedule + self.customer_contact + \
                self.not_ready_situations + self.brisk_pace + \
                self.finish_work

        return total

    class Meta:
        verbose_name = "Prod"
        verbose_name_plural = "Prods"


# pre trip
class SafeDrivePreTrip(models.Model):
    student = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='pretrip_student',
                                   null=False)

    date = models.DateField(null=True, blank=True, default=None, verbose_name='Date')
    start_time = models.TimeField(null=True, blank=True, default=None, verbose_name='Start Time')
    end_time = models.TimeField(null=True, blank=True, default=None, verbose_name='End Time')
    driver_signature = models.ImageField(upload_to='signatures/pre-trip/driver/', default=None, null=True, blank=True)
    evaluator_signature = models.ImageField(upload_to='signatures/pre-trip/evaluator/', default=None, null=True,
                                            blank=True)
    company_rep_signature = models.ImageField(upload_to='signatures/pre-trip/company/', default=None, null=True,
                                              blank=True)
    company_rep_name = models.CharField(max_length=150, null=True, blank=True, default=None,
                                        verbose_name='Company Rep. Name')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip"
        verbose_name_plural = "Pre Trips"


# 1. Pre trip inside cab
class PreTripInsideCab(models.Model):
    pre_trip = models.OneToOneField('safe_driver.SafeDrivePreTrip', on_delete=models.CASCADE, null=False)

    fhwa = models.IntegerField(_('FHWA'), choices=NUMBER_CHOICES, default=0, )
    emergency_response_book = models.IntegerField(_('Emergency Response Book'), choices=NUMBER_CHOICES, default=0, )
    dvir = models.IntegerField(_('DVIR'), choices=NUMBER_CHOICES, default=0, )
    parking_brake_applied = models.IntegerField(_('Parking Brake Applied'), choices=NUMBER_CHOICES, default=0, )
    transmission_neutral_or_park = models.IntegerField(_('Transmission Neutral/Park'), choices=NUMBER_CHOICES,
                                                       default=0, )
    seat_adjustment = models.IntegerField(_('Seat Adjustment'), choices=NUMBER_CHOICES, default=0, )
    seat_belt = models.IntegerField(_('Seat Belt'), choices=NUMBER_CHOICES, default=0, )
    cab_or_berth = models.IntegerField(_('Cab/Berth'), choices=NUMBER_CHOICES, default=0, )
    dome_and_map_lights = models.IntegerField(_('Dome and Map Lights'), choices=NUMBER_CHOICES, default=0, )
    windows = models.IntegerField(_('Windows'), choices=NUMBER_CHOICES, default=0, )
    mirros_adjustments = models.IntegerField(_('Mirrors Adjustment'), choices=NUMBER_CHOICES, default=0, )
    steering_wheel = models.IntegerField(_('Steering Wheel'), choices=NUMBER_CHOICES, default=0, )
    horn = models.IntegerField(_('Horn'), choices=NUMBER_CHOICES, default=0, )
    indicators = models.IntegerField(_('Indicators'), choices=NUMBER_CHOICES, default=0, )
    wipers = models.IntegerField(_('Wipers'), choices=NUMBER_CHOICES, default=0, )
    gauges = models.IntegerField(_('Gauges'), choices=NUMBER_CHOICES, default=0, )
    air_heater_defrost = models.IntegerField(_('Air, Heater, Defrost'), choices=NUMBER_CHOICES, default=0, )
    bi_directional_triangles = models.IntegerField(_('Bi-directional Triangles'), choices=NUMBER_CHOICES, default=0, )
    shifter_straight_and_secure = models.IntegerField(_('Shifter Straight and Secure'), choices=NUMBER_CHOICES,
                                                      default=0, )
    splitter = models.IntegerField(_('Splitter'), choices=NUMBER_CHOICES, default=0, )
    clear_floor_board = models.IntegerField(_('Clear floor Board'), choices=NUMBER_CHOICES, default=0, )
    pedals = models.IntegerField(_('Pedals'), choices=NUMBER_CHOICES, default=0, )
    park_brake = models.IntegerField(_('Park Brake'), choices=NUMBER_CHOICES, default=0, )
    service_brake_test = models.IntegerField(_('Service Brake Test'), choices=NUMBER_CHOICES, default=0, )
    trailer_brake_test = models.IntegerField(_('Trailer Brake Test'), choices=NUMBER_CHOICES, default=0, )
    pull_key = models.IntegerField(_('Pull Key'), choices=NUMBER_CHOICES, default=0, )
    exit_safely = models.IntegerField(_('Exit Safely'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Inside Cab"
        verbose_name_plural = "Pre Trip Inside Cabs"

    pass


# 2. Pre trip C.O.A.L.S
class PreTripCOALS(models.Model):
    pre_trip = models.OneToOneField('safe_driver.SafeDrivePreTrip', on_delete=models.CASCADE, null=False)

    chock_wheels = models.IntegerField(_('Chock Wheels'), choices=NUMBER_CHOICES, default=0, )
    cut_in = models.IntegerField(_('Cut in'), choices=NUMBER_CHOICES, default=0, )
    cut_out = models.IntegerField(_('Cut out'), choices=NUMBER_CHOICES, default=0, )
    air_leak_test = models.IntegerField(_('Air Leak Test'), choices=NUMBER_CHOICES, default=0, )
    low_air_warning = models.IntegerField(_('Low Air Warning'), choices=NUMBER_CHOICES, default=0, )
    spring = models.IntegerField(_('Spring'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip C.O.A.L.S"
        verbose_name_plural = "Pre Trip C.O.A.L.S"


# 3. Pre Trip Engine Compartment
class PreTripEngineCompartment(models.Model):
    pre_trip = models.OneToOneField('safe_driver.SafeDrivePreTrip', on_delete=models.CASCADE, null=False)

    fuses = models.IntegerField(_('Fuses'), choices=NUMBER_CHOICES, default=0, )
    hood_latches = models.IntegerField(_('Hood Latches'), choices=NUMBER_CHOICES, default=0, )
    hood_locking_device = models.IntegerField(_('Hood Locking Device'), choices=NUMBER_CHOICES, default=0, )
    engine_oil = models.IntegerField(_('Engine Oil'), choices=NUMBER_CHOICES, default=0, )
    transmission_oil = models.IntegerField(_('Transmission Oil'), choices=NUMBER_CHOICES, default=0, )
    power_steering_fluid = models.IntegerField(_('Power Steering Fluid'), choices=NUMBER_CHOICES, default=0, )
    washer_fluid = models.IntegerField(_('Washer Fluid'), choices=NUMBER_CHOICES, default=0, )
    coolant = models.IntegerField(_('Coolant'), choices=NUMBER_CHOICES, default=0, )
    belts_and_hoses = models.IntegerField(_('Belts and Hoses'), choices=NUMBER_CHOICES, default=0, )
    filters = models.IntegerField(_('Filters'), choices=NUMBER_CHOICES, default=0, )
    components = models.IntegerField(_('Components'), choices=NUMBER_CHOICES, default=0, )
    leaks_air_and_fluid = models.IntegerField(_('Leaks(Air & Fluid)'), choices=NUMBER_CHOICES, default=0, )
    frame = models.IntegerField(_('Frame'), choices=NUMBER_CHOICES, default=0, )
    suspension = models.IntegerField(_('Suspension'), choices=NUMBER_CHOICES, default=0, )
    steering_components = models.IntegerField(_('Steering Components'), choices=NUMBER_CHOICES, default=0, )
    brake_chambers_or_slack_adj = models.IntegerField(_('Brake Chambers/Slack Adj'), choices=NUMBER_CHOICES,
                                                      default=0, )
    brake_drums_and_pads = models.IntegerField(_('Brake Drums & Pads'), choices=NUMBER_CHOICES, default=0, )
    wheel_bearings = models.IntegerField(_('Wheel Bearings'), choices=NUMBER_CHOICES, default=0, )
    tire_inflation = models.IntegerField(_('Tire Inflation'), choices=NUMBER_CHOICES, default=0, )
    tire_and_rin_condition = models.IntegerField(_('Tire & Rim Condition'), choices=NUMBER_CHOICES, default=0, )
    valve_stems_and_hub_oil = models.IntegerField(_('Valve Stems & Hub Oil'), choices=NUMBER_CHOICES, default=0, )
    mud_flaps = models.IntegerField(_('Mud Flaps'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Engine Compartment"
        verbose_name_plural = "Pre Trip Engine Compartments"


# 4. Pre Trip Vehicle Front
class PreTripVehicleFront(models.Model):
    pre_trip = models.OneToOneField('safe_driver.SafeDrivePreTrip', on_delete=models.CASCADE, null=False)

    body_damage = models.IntegerField(_('Body Damage'), choices=NUMBER_CHOICES, default=0, )
    lights_id_and_others = models.IntegerField(_('Lights-I.D. mkr, head, 4way, road'), choices=NUMBER_CHOICES,
                                               default=0, )
    bumper_and_tow_hooks = models.IntegerField(_('Bumper and Tow Hooks'), choices=NUMBER_CHOICES, default=0, )
    license_plate = models.IntegerField(_('License Plate'), choices=NUMBER_CHOICES, default=0, )
    sensors = models.IntegerField(_('Sensors'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Vehicle Front"
        verbose_name_plural = "Pre Trip Vehicle Fronts"


# 5. Pre Trip Both Sides Vehicle
class PreTripBothSidesVehicle(models.Model):
    pre_trip = models.OneToOneField('safe_driver.SafeDrivePreTrip', on_delete=models.CASCADE, null=False)

    mirrors = models.IntegerField(_('Mirrors'), choices=NUMBER_CHOICES, default=0, )
    vehicle_markings_or_decals = models.IntegerField(_('Vehicle Markings/Decals'), choices=NUMBER_CHOICES, default=0, )
    dots = models.IntegerField(_('DOT’s, CA, MC #’s'), choices=NUMBER_CHOICES, default=0, )
    ifta_permit = models.IntegerField(_('IFTA Permit'), choices=NUMBER_CHOICES, default=0, )
    air_tanks = models.IntegerField(_('Air Tanks'), choices=NUMBER_CHOICES, default=0, )
    fuel_tank_alternative = models.IntegerField(_('Fuel Tank - Alternative Fuel'), choices=NUMBER_CHOICES, default=0, )
    _def = models.IntegerField(_('DEF'), choices=NUMBER_CHOICES, default=0, )
    battery_box = models.IntegerField(_('Battery Box'), choices=NUMBER_CHOICES, default=0, )
    deck_plate = models.IntegerField(_('Deck Plate'), choices=NUMBER_CHOICES, default=0, )
    air_lines_lights_cord_spring = models.IntegerField(_('Air Lines, Light Cord, Spring'), choices=NUMBER_CHOICES,
                                                       default=0, )
    frame = models.IntegerField(_('Frame'), choices=NUMBER_CHOICES, default=0, )
    fifth_wheel = models.IntegerField(_('5th Wheel'), choices=NUMBER_CHOICES, default=0, )
    mud_flaps = models.IntegerField(_('Mud Flaps'), choices=NUMBER_CHOICES, default=0, )
    drive_line = models.IntegerField(_('Drive Line'), choices=NUMBER_CHOICES, default=0, )
    air_cans_or_lines = models.IntegerField(_('Air Cans/Lines'), choices=NUMBER_CHOICES, default=0, )
    brake_chambers_or_slack_adj = models.IntegerField(_('Brake Chambers/Slack Adj'), choices=NUMBER_CHOICES,
                                                      default=0, )
    suspension = models.IntegerField(_('Suspension'), choices=NUMBER_CHOICES, default=0, )
    brake_drums_and_lining = models.IntegerField(_('Brake Drums & Lining'), choices=NUMBER_CHOICES, default=0, )
    tire_inflation = models.IntegerField(_('Tire Inflation'), choices=NUMBER_CHOICES, default=0, )
    tire_and_rim_condition = models.IntegerField(_('Tire & Rim Condition - Space'), choices=NUMBER_CHOICES, default=0, )
    valve_stem_and_hub_oil = models.IntegerField(_('Valve Stem & Hub Oil'), choices=NUMBER_CHOICES, default=0, )
    body_condition = models.IntegerField(_('Body Condition'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Both Sides Vehicle"
        verbose_name_plural = "Pre Trip Both Sides Vehicles"


# 6. Pre Trip Vehicle/Tractor Rear
class PreTripVehicleOrTractorRear(models.Model):
    pre_trip = models.OneToOneField('safe_driver.SafeDrivePreTrip', on_delete=models.CASCADE, null=False)

    brake_and_others = models.IntegerField(_('Brake, Tail, 4way, Signal Lights'), choices=NUMBER_CHOICES, default=0, )
    body_condition = models.IntegerField(_('Body Condition'), choices=NUMBER_CHOICES, default=0, )
    reflectors_and_work_light = models.IntegerField(_('Reflectors & Work Light'), choices=NUMBER_CHOICES, default=0, )
    mud_flaps = models.IntegerField(_('Mud Flaps'), choices=NUMBER_CHOICES, default=0, )
    couple_devices = models.IntegerField(_('Couple Devices'), choices=NUMBER_CHOICES, default=0, )
    license_plate_and_light = models.IntegerField(_('Licenses Plate & Light'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Trip Vehicle/Tractor Rear"
        verbose_name_plural = "Trip Vehicle/Tractor Rears"


# 7. Pre Trip Front of Trailer Box
class PreTripFrontTrailerBox(models.Model):
    pre_trip = models.OneToOneField('safe_driver.SafeDrivePreTrip', on_delete=models.CASCADE, null=False)

    equipment_height_and_condition = models.IntegerField(_('Equipment Height & Condition'), choices=NUMBER_CHOICES,
                                                         default=0, )
    clearance_lights = models.IntegerField(_('Clearance Lights'), choices=NUMBER_CHOICES, default=0, )
    reflectors = models.IntegerField(_('Reflectors'), choices=NUMBER_CHOICES, default=0, )
    chassis_and_locks = models.IntegerField(_('Chassis and Chassis Locks'), choices=NUMBER_CHOICES, default=0, )
    refrigeration_system = models.IntegerField(_('Refrigeration System'), choices=NUMBER_CHOICES, default=0, )
    federal_inspection_or_bit = models.IntegerField(_('Federal Inspection or BIT'), choices=NUMBER_CHOICES, default=0, )
    utility_box = models.IntegerField(_('Utility Box'), choices=NUMBER_CHOICES, default=0, )
    electric_plug = models.IntegerField(_('Electric Plug'), choices=NUMBER_CHOICES, default=0, )
    glad_hands_and_grommets = models.IntegerField(_('Glad Hands and Grommets'), choices=NUMBER_CHOICES, default=0, )
    air_lines = models.IntegerField(_('Air Lines'), choices=NUMBER_CHOICES, default=0, )
    equipement_number_and_markings = models.IntegerField(_('Equipment Number and Markings'), choices=NUMBER_CHOICES,
                                                         default=0, )

    notes = models.TextField(default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Front of Trailer Box"
        verbose_name_plural = "Front of Trailer Box"


# 8. Pre Trip Driver Side Trailer Box
class PreTripDriverSideTrailerBox(models.Model):
    pre_trip = models.OneToOneField('safe_driver.SafeDrivePreTrip', on_delete=models.CASCADE, null=False)

    condition = models.IntegerField(_('Condition'), choices=NUMBER_CHOICES, default=0, )
    reflectors = models.IntegerField(_('Reflectors'), choices=NUMBER_CHOICES, default=0, )
    marker_lights = models.IntegerField(_('Marker Lights'), choices=NUMBER_CHOICES, default=0, )
    coupling = models.IntegerField(_('Coupling'), choices=NUMBER_CHOICES, default=0, )
    frame_and_chassis = models.IntegerField(_('Frame & Chassis'), choices=NUMBER_CHOICES, default=0, )
    landing_gear = models.IntegerField(_('Landing Gear'), choices=NUMBER_CHOICES, default=0, )
    air_cans = models.IntegerField(_('Air Cans'), choices=NUMBER_CHOICES, default=0, )
    brake_chambers_or_slack_adj = models.IntegerField(_('Brake Chambers/Slack Adj'), choices=NUMBER_CHOICES,
                                                      default=0, )
    axel = models.IntegerField(_('Axel'), choices=NUMBER_CHOICES, default=0, )
    suspension = models.IntegerField(_('Suspension'), choices=NUMBER_CHOICES, default=0, )
    brake_drums_and_lining = models.IntegerField(_('Brake Drums & Lining'), choices=NUMBER_CHOICES, default=0, )
    tire_inflation = models.IntegerField(_('Tire Inflation'), choices=NUMBER_CHOICES, default=0, )
    tire_and_rim_condition = models.IntegerField(_('Tire & Rim Condition - Space'), choices=NUMBER_CHOICES, default=0, )
    valve_stem_and_hub_oil = models.IntegerField(_('Valve Stem & Hub Oil'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Driver Side Trailer Box"
        verbose_name_plural = "Driver Side Trailer Box"


# 9. Pre Trip Rear Trailer Box
class PreTripRearTrailerBox(models.Model):
    pre_trip = models.OneToOneField('safe_driver.SafeDrivePreTrip', on_delete=models.CASCADE, null=False)

    brake_and_others = models.IntegerField(_('Brake, Tail, 4way, Signal Lights'), choices=NUMBER_CHOICES, default=0, )
    all_cargo_door = models.IntegerField(_('All Cargo Door'), choices=NUMBER_CHOICES, default=0, )
    cargo_load_area = models.IntegerField(_('Cargo Load Area'), choices=NUMBER_CHOICES, default=0, )
    all_securing_devices = models.IntegerField(_('All Securing Devices'), choices=NUMBER_CHOICES, default=0, )
    chassis = models.IntegerField(_('Chassis'), choices=NUMBER_CHOICES, default=0, )
    coupling_devices_or_plintle = models.IntegerField(_('Coupling Devices/Pintle'), choices=NUMBER_CHOICES, default=0, )
    air_elctrical = models.IntegerField(_('Air, Electrical'), choices=NUMBER_CHOICES, default=0, )
    safety_loops = models.IntegerField(_('Safety Loops'), choices=NUMBER_CHOICES, default=0, )
    license_plate = models.IntegerField(_('License Plate'), choices=NUMBER_CHOICES, default=0, )
    flector_devices = models.IntegerField(_('Flector Devices'), choices=NUMBER_CHOICES, default=0, )
    mud_flaps = models.IntegerField(_('Mud Flaps'), choices=NUMBER_CHOICES, default=0, )
    notes = models.TextField(default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Rear Trailer Box"
        verbose_name_plural = "Pre Trip Rear Trailer Box"


# 10. Pre Trip Passenger Side Trailer or Box
class PreTripPassengerSideTrailerBox(models.Model):
    pre_trip = models.OneToOneField('safe_driver.SafeDrivePreTrip', on_delete=models.CASCADE, null=False)

    condition = models.IntegerField(_('Condition'), choices=NUMBER_CHOICES, default=0, )
    reflectors = models.IntegerField(_('Reflectors'), choices=NUMBER_CHOICES, default=0, )
    marker_lights = models.IntegerField(_('Marker Lights'), choices=NUMBER_CHOICES, default=0, )
    coupling = models.IntegerField(_('Coupling'), choices=NUMBER_CHOICES, default=0, )
    frame_and_chassis = models.IntegerField(_('Frame & Chassis'), choices=NUMBER_CHOICES, default=0, )
    landing_gear = models.IntegerField(_('Landing Gear'), choices=NUMBER_CHOICES, default=0, )
    air_cans = models.IntegerField(_('Air Cans'), choices=NUMBER_CHOICES, default=0, )
    brake_chambers_or_slack_adj = models.IntegerField(_('Brake Chambers/Slack Adj'), choices=NUMBER_CHOICES,
                                                      default=0, )
    axel = models.IntegerField(_('Axel'), choices=NUMBER_CHOICES, default=0, )
    suspension = models.IntegerField(_('Suspension'), choices=NUMBER_CHOICES, default=0, )
    brake_drums_and_lining = models.IntegerField(_('Brake Drums & Lining'), choices=NUMBER_CHOICES, default=0, )
    tire_inflation = models.IntegerField(_('Tire Inflation'), choices=NUMBER_CHOICES, default=0, )
    tire_and_rim_condition = models.IntegerField(_('Tire & Rim Condition - Space'), choices=NUMBER_CHOICES, default=0, )
    valve_stem_and_hub_oil = models.IntegerField(_('Valve Stem & Hub Oil'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Passenger Side Trailer or Box"
        verbose_name_plural = "Passenger Side Trailer or Box"


# 11. Pre Trip Dolly
class PreTripDolly(models.Model):
    pre_trip = models.OneToOneField('safe_driver.SafeDrivePreTrip', on_delete=models.CASCADE, null=False)

    condition = models.IntegerField(_('Condition'), choices=NUMBER_CHOICES, default=0, )
    reflectors = models.IntegerField(_('Reflectors'), choices=NUMBER_CHOICES, default=0, )
    brake_and_others = models.IntegerField(_('Brake, Tail, 4way, Signal Lights'), choices=NUMBER_CHOICES, default=0, )
    markings = models.IntegerField(_('Markings'), choices=NUMBER_CHOICES, default=0, )
    frame = models.IntegerField(_('Frame'), choices=NUMBER_CHOICES, default=0, )
    registration = models.IntegerField(_('Registration'), choices=NUMBER_CHOICES, default=0, )
    air_cans = models.IntegerField(_('Air Cans'), choices=NUMBER_CHOICES, default=0, )
    brake_chambers_or_slack_adj = models.IntegerField(_('Brake Chambers/Slack Adj'), choices=NUMBER_CHOICES,
                                                      default=0, )
    wheel = models.IntegerField(_('Wheel'), choices=NUMBER_CHOICES, default=0, )
    suspension = models.IntegerField(_('Suspension'), choices=NUMBER_CHOICES, default=0, )
    brake_drums_and_lining = models.IntegerField(_('Brake Drums & Lining'), choices=NUMBER_CHOICES, default=0, )
    tire_inflation = models.IntegerField(_('Tire Inflation'), choices=NUMBER_CHOICES, default=0, )
    tire_and_rim_condition = models.IntegerField(_('Tire & Rim Condition - Space'), choices=NUMBER_CHOICES, default=0, )
    valve_stem_and_hub_oil = models.IntegerField(_('Valve Stems & Hub Oil'), choices=NUMBER_CHOICES, default=0, )
    handles = models.IntegerField(_('Handles'), choices=NUMBER_CHOICES, default=0, )
    dolly_eye = models.IntegerField(_('Dolly Eye'), choices=NUMBER_CHOICES, default=0, )
    air_lines_and_light_cord = models.IntegerField(_('Air Lines & Light Cord'), choices=NUMBER_CHOICES, default=0, )
    safety_chains = models.IntegerField(_('Safety Chains'), choices=NUMBER_CHOICES, default=0, )
    fifth_wheel = models.IntegerField(_('5th wheel'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Dolly"
        verbose_name_plural = "Pre Trip Dollys"


# 12. Pre Trip Combination Vehicles
class PreTripCombinationVehicles(models.Model):
    pre_trip = models.OneToOneField('safe_driver.SafeDrivePreTrip', on_delete=models.CASCADE, null=False)

    heavier_trailer_in_front = models.IntegerField(_('Heavier Trailer in front'), choices=NUMBER_CHOICES, default=0, )
    builds_equip_properly = models.IntegerField(_('Builds Equip Properly'), choices=NUMBER_CHOICES, default=0, )
    understand_types_of_dollies = models.IntegerField(_('Understand Types of Dollies'), choices=NUMBER_CHOICES,
                                                      default=0, )
    secures_dolly_properly = models.IntegerField(_('Secures Dolly Properly'), choices=NUMBER_CHOICES, default=0, )
    speed_control_on_turns = models.IntegerField(_('Speed Control on Turns'), choices=NUMBER_CHOICES, default=0, )
    avoids_abrupt_maneuvers = models.IntegerField(_('Avoids Abrupt Maneuvers'), choices=NUMBER_CHOICES, default=0, )
    air_conditioner = models.IntegerField(_('Air Conditioner'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Combination Vehicle"
        verbose_name_plural = "Combination Vehicles"


# 13. Pre Trip Post Trip
class PreTripPostTrip(models.Model):
    pre_trip = models.OneToOneField('safe_driver.SafeDrivePreTrip', on_delete=models.CASCADE, null=False)

    condition = models.IntegerField(_('Condition'), choices=NUMBER_CHOICES, default=0, )
    all_lights = models.IntegerField(_('All Lights'), choices=NUMBER_CHOICES, default=0, )
    tire_condition = models.IntegerField(_('Tire Condition'), choices=NUMBER_CHOICES, default=0, )
    tire_inflation = models.IntegerField(_('Tire Inflation'), choices=NUMBER_CHOICES, default=0, )
    hub_heat = models.IntegerField(_('Hub Heat'), choices=NUMBER_CHOICES, default=0, )
    reflective_devices = models.IntegerField(_('Reflective Devices'), choices=NUMBER_CHOICES, default=0, )
    fluid_air_leaks = models.IntegerField(_('Fluid & Air Leaks'), choices=NUMBER_CHOICES, default=0, )
    equipment_parked_secure = models.IntegerField(_('Equipement Parked - Secure'), choices=NUMBER_CHOICES, default=0, )
    avoid_shifting_lead = models.IntegerField(_('Avoid Shifting Lead'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Post Trip"
        verbose_name_plural = "Pre Trip Post Trips"


class SafeDriveEye(models.Model):
    student = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='eye_student',
                                   null=False)

    start_time = models.TimeField(default=None, null=True, blank=True)
    stop_time = models.TimeField(default=None, null=True, blank=True)

    eye_movement = models.CharField(_('Eye Movement'), max_length=120, default=None, null=True, blank=True)

    eye_lead_counter = models.IntegerField(_('Eye Lead Counter'), default=None, null=True, blank=True)
    parked_counter = models.IntegerField(_('Parked Counter'), default=None, null=True, blank=True)
    intersections_counter = models.IntegerField(_('Intersections Counter'), default=None, null=True, blank=True)
    parked_cars_counter = models.IntegerField(_('Parked Cars Counter'), default=None, null=True, blank=True)
    predestrians_counter = models.IntegerField(_('Predestrians Counter'), default=None, null=True, blank=True)
    follow_time_counter = models.IntegerField(_('Follow Time Counter'), default=None, null=True, blank=True)
    rear_counter = models.IntegerField(_('Rear Counter'), default=None, null=True, blank=True)
    front_counter = models.IntegerField(_('Front Counter'), default=None, null=True, blank=True)
    gauges_counter = models.IntegerField(_('Front Counter'), default=None, null=True, blank=True)
    left_mirror_counter = models.IntegerField(_('Left Mirror Counter'), default=None, null=True, blank=True)
    right_mirror_counter = models.IntegerField(_('Right Mirror Counter'), default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s Eye - %s' % (self.student.full_name, self.pk)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Eye"


# student BTW
class SafeDriveBTW(models.Model):
    student = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='btw_student',
                                   null=False)

    date = models.DateField(null=True, blank=True, default=None, verbose_name='Date')
    start_time = models.TimeField(null=True, blank=True, default=None, verbose_name='Start Time')
    end_time = models.TimeField(null=True, blank=True, default=None, verbose_name='End Time')
    driver_signature = models.ImageField(_('Driver Signature'), upload_to='signatures/btw/driver/', default=None,
                                         null=True, blank=True)
    evaluator_signature = models.ImageField(_('Evaluator Signature'), upload_to='signatures/btw/evaluator/',
                                            default=None, null=True,
                                            blank=True)
    company_rep_signature = models.ImageField(_('Company Rep Signature'), upload_to='signatures/btw/company/',
                                              default=None, null=True,
                                              blank=True)
    company_rep_name = models.CharField(max_length=150, null=True, blank=True, default=None,
                                        verbose_name='Company Rep. Name')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s BTW - %s' % (self.student.full_name, self.pk)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Behind The Wheel"


# 1. Cab safety
class BTWCabSafety(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    seat_belt = models.IntegerField(_('Seat Belt'), choices=NUMBER_CHOICES, default=0, )
    can_distractions = models.IntegerField(_('Cab distractions'), choices=NUMBER_CHOICES, default=0, )
    cab_obstructions = models.IntegerField(_('Cab Obstructions'), choices=NUMBER_CHOICES, default=0, )
    cab_chemicals = models.IntegerField(_('Cab Chemicals'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW Cab Safety"


# 2. Start Engine
class BTWStartEngine(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    park_brake_applied = models.IntegerField(_('Park Brake Applied'), choices=NUMBER_CHOICES, default=0, )
    trans_in_park_or_neutral = models.IntegerField(_('Trans in Park or Neutral'), choices=NUMBER_CHOICES, default=0, )
    clutch_depressed = models.IntegerField(_('Clutch depressed'), choices=NUMBER_CHOICES, default=0, )
    uses_starter_properly = models.IntegerField(_('Uses Starter Properly'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW Start Engine"


# 3. Engine Operation
class BTWEngineOperation(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    lugging = models.IntegerField(_('Lugging'), choices=NUMBER_CHOICES, default=0, )
    over_revving = models.IntegerField(_('Over Revving'), choices=NUMBER_CHOICES, default=0, )
    check_gauges = models.IntegerField(_('Check Gauges'), choices=NUMBER_CHOICES, default=0, )
    does_not_ride = models.IntegerField(_('Doesn’t Ride'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW Engine Operation"


# 4. Clutch and Transmission
class BTWClutchAndTransmission(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    start_off_smoothly = models.IntegerField(_('Start off smoothly'), choices=NUMBER_CHOICES, default=0, )
    proper_gear_use = models.IntegerField(_('Proper gear use'), choices=NUMBER_CHOICES, default=0, )
    shift_smoothly = models.IntegerField(_('Shift smoothly'), choices=NUMBER_CHOICES, default=0, )
    proper_gear_sequence = models.IntegerField(_('Proper gear sequence'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW Clutch and Transmission"


# 5. Coupling
class BTWCoupling(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    check_for_hazards = models.IntegerField(_('Check for Hazards'), choices=NUMBER_CHOICES, default=0, )
    backs_under_slowly = models.IntegerField(_('Backs under slowly'), choices=NUMBER_CHOICES, default=0, )
    secures_equipment = models.IntegerField(_('Secures equipment'), choices=NUMBER_CHOICES, default=0, )
    physical_check_coupling = models.IntegerField(_('Physical check coupling'), choices=NUMBER_CHOICES, default=0, )
    charges_system_correctly = models.IntegerField(_('Charges system correctly'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW Coupling"


# 6. Uncoupling
class BTWUncoupling(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    secures_equipment = models.IntegerField(_('Secures equipment'), choices=NUMBER_CHOICES, default=0, )
    chock_wheels = models.IntegerField(_('Chock Wheels'), choices=NUMBER_CHOICES, default=0, )
    lower_landing_gear = models.IntegerField(_('Lower Landing Gear'), choices=NUMBER_CHOICES, default=0, )
    pull_away_or_trailer_secure = models.IntegerField(_('Pull away/trailer secure'), choices=NUMBER_CHOICES,
                                                      default=0, )
    leve_or_firm_ground = models.IntegerField(_('Leve/firm ground'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW Uncoupling"


# 7. Use of Brakes and Stopping
class BTWBrakesAndStoppings(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    checks_rear_or_gives_warning = models.IntegerField(_('Checks rear/gives warning'), choices=NUMBER_CHOICES,
                                                       default=0, )
    full_stop_or_smooth = models.IntegerField(_('Full Stop/Smooth(no rebound)'), choices=NUMBER_CHOICES, default=0, )
    does_not_fan = models.IntegerField(_('Doesn’t fan'), choices=NUMBER_CHOICES, default=0, )
    down_shifts = models.IntegerField(_('Down Shifts'), choices=NUMBER_CHOICES, default=0, )
    uses_foot_brake_only = models.IntegerField(_('Uses foot brake only'), choices=NUMBER_CHOICES, default=0, )
    hand_valve_use = models.IntegerField(_('Hand valve use'), choices=NUMBER_CHOICES, default=0, )
    does_not_roll_back = models.IntegerField(_('Doesn’t roll back'), choices=NUMBER_CHOICES, default=0, )
    engine_assist = models.IntegerField(_('Engine Assist'), choices=NUMBER_CHOICES, default=0, )
    avoids_sudden_stops = models.IntegerField(_('Avoids sudden stops'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Use of Brakes and Stopping"


# 8. Eye movement and mirror use
class BTWEyeMovementAndMirror(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    eyes_ahead = models.IntegerField(_('Eyes ahead'), choices=NUMBER_CHOICES, default=0, )
    follow_up_in_mirror = models.IntegerField(_('Follow-up in mirror'), choices=NUMBER_CHOICES, default=0, )
    checks_mirror = models.IntegerField(_('Checks mirrors 5 to 8 sec’s'), choices=NUMBER_CHOICES, default=0, )
    scans_does_not_stare = models.IntegerField(_('Scans doesn’t stare'), choices=NUMBER_CHOICES, default=0, )
    avoid_billboards = models.IntegerField(_('Avoid Billboards'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Eye movement and mirror use"


# 9. Recognizes Hazards
class BTWRecognizesHazards(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    uses_horn = models.IntegerField(_('Uses Horn to communicate'), choices=NUMBER_CHOICES, default=0, )
    makes_adjustments = models.IntegerField(_('Makes Adjustments'), choices=NUMBER_CHOICES, default=0, )
    path_of_least_resistance = models.IntegerField(_('Path of least resistance'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Recognizes Hazards"


# 10. Lights and Signals
class BTWLightsAndSignals(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    proper_use_of_lights = models.IntegerField(_('Proper use of lights'), choices=NUMBER_CHOICES, default=0, )
    adjust_speed = models.IntegerField(_('Adjust Speed'), choices=NUMBER_CHOICES, default=0, )
    signals_well_in_advance = models.IntegerField(_('Signals well in advance'), choices=NUMBER_CHOICES, default=0, )
    cancels_signal = models.IntegerField(_('Cancels signal'), choices=NUMBER_CHOICES, default=0, )
    use_of_4_ways = models.IntegerField(_('Use of 4 Ways'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Lights and Signals"


# 11. Steering
class BTWSteering(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    over_steers = models.IntegerField(_('Over Steers'), choices=NUMBER_CHOICES, default=0, )
    floats = models.IntegerField(_('Floats'), choices=NUMBER_CHOICES, default=0, )
    poisture_and_grip = models.IntegerField(_('Posture and Grip'), choices=NUMBER_CHOICES, default=0, )
    centered_in_lane = models.IntegerField(_('Centered in lane'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Steering"


# 12. Backing
class BTWBacking(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    size_up_situation = models.IntegerField(_('Size up situation'), choices=NUMBER_CHOICES, default=0, )
    driver_side_back = models.IntegerField(_('Driver side back'), choices=NUMBER_CHOICES, default=0, )
    check_rear = models.IntegerField(_('Check rear'), choices=NUMBER_CHOICES, default=0, )
    gets_attention = models.IntegerField(_('Gets Attention'), choices=NUMBER_CHOICES, default=0, )
    backs_slowly = models.IntegerField(_('Backs slowly'), choices=NUMBER_CHOICES, default=0, )
    rechecks_conditions = models.IntegerField(_('Re-checks conditions'), choices=NUMBER_CHOICES, default=0, )
    uses_other_aids = models.IntegerField(_('Uses other aids'), choices=NUMBER_CHOICES, default=0, )
    steers_correctly = models.IntegerField(_('Steers correctly'), choices=NUMBER_CHOICES, default=0, )
    does_not_hit_dock = models.IntegerField(_('Doesn’t hit dock'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Backing"


# 13. Speed
class BTWSpeed(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    adjust_to_conditions = models.IntegerField(_('Adjust to conditions'), choices=NUMBER_CHOICES, default=0, )
    speed = models.IntegerField(_('Speed'), choices=NUMBER_CHOICES, default=0, )
    proper_following_distance = models.IntegerField(_('Proper Following distance'), choices=NUMBER_CHOICES, default=0, )
    speed_on_curves = models.IntegerField(_('Speed on Curves'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Speed"


# 14. Intersections
class BTWIntersections(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    approach_decision_point = models.IntegerField(_('Approach -decision point'), choices=NUMBER_CHOICES, default=0, )
    clear_intersection = models.IntegerField(_('Clear Intersection L-R-L'), choices=NUMBER_CHOICES, default=0, )
    check_mirrors = models.IntegerField(_('Check Mirrors'), choices=NUMBER_CHOICES, default=0, )
    full_stop = models.IntegerField(_('Full stop when needed'), choices=NUMBER_CHOICES, default=0, )
    times_light_or_starts = models.IntegerField(_('Times light or starts too fast'), choices=NUMBER_CHOICES,
                                                default=0, )
    steering_axel_staright = models.IntegerField(_('Steering axel straight'), choices=NUMBER_CHOICES, default=0, )
    yields_right_of_way = models.IntegerField(_('Yields right-of-way'), choices=NUMBER_CHOICES, default=0, )
    proper_speed_or_gear = models.IntegerField(_('Proper speed/gear'), choices=NUMBER_CHOICES, default=0, )
    leaves_space = models.IntegerField(_('Leaves space for an out'), choices=NUMBER_CHOICES, default=0, )
    stop_lines = models.IntegerField(_('Stop Lines - crosswalks'), choices=NUMBER_CHOICES, default=0, )
    railroad_crossings = models.IntegerField(_('Railroad crossings'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Intersections"


# 15. Turning
class BTWTurning(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    signals_correctly = models.IntegerField(_('Signals correctly'), choices=NUMBER_CHOICES, default=0, )
    gets_in_proper_time = models.IntegerField(_('Gets in proper lane'), choices=NUMBER_CHOICES, default=0, )
    downshifts_to_pulling_gear = models.IntegerField(_('Downshifts to pulling gear'), choices=NUMBER_CHOICES,
                                                     default=0, )
    handles_light_correctly = models.IntegerField(_('Handles light correctly'), choices=NUMBER_CHOICES, default=0, )
    setup_and_execution = models.IntegerField(_('Set up and execution'), choices=NUMBER_CHOICES, default=0, )
    turn_speed = models.IntegerField(_('Turn Speed'), choices=NUMBER_CHOICES, default=0, )
    mirror_follow_up = models.IntegerField(_('Mirror follow up'), choices=NUMBER_CHOICES, default=0, )
    turns_lane_to_lane = models.IntegerField(_('Turns lane to lane'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Turning"


# 16. Parking
class BTWParking(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    does_not_hit_curb = models.IntegerField(_('Doesn’t hit curb'), choices=NUMBER_CHOICES, default=0, )
    curbs_wheels = models.IntegerField(_('Curbs wheels'), choices=NUMBER_CHOICES, default=0, )
    chock_wheels = models.IntegerField(_('Chock wheels (if required)'), choices=NUMBER_CHOICES, default=0, )
    park_brake_applied = models.IntegerField(_('Park Brake applied'), choices=NUMBER_CHOICES, default=0, )
    trans_in_neutral = models.IntegerField(_('Trans in neutral'), choices=NUMBER_CHOICES, default=0, )
    engine_off = models.IntegerField(_('Engine off - Take keys'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Parking"


# 17. Multiple trailers
class BTWMultipleTrailers(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    heavier_trailer_in_front = models.IntegerField(_('Heavier trailer in front'), choices=NUMBER_CHOICES, default=0, )
    builds_equip_properly = models.IntegerField(_('Builds equip properly'), choices=NUMBER_CHOICES, default=0, )
    understand_types_of_dollies = models.IntegerField(_('Understand types of dollies'), choices=NUMBER_CHOICES,
                                                      default=0, )
    secures_dolly_properly = models.IntegerField(_('Secures dolly properly'), choices=NUMBER_CHOICES, default=0, )
    speed_control_on_turns = models.IntegerField(_('Speed control on turns'), choices=NUMBER_CHOICES, default=0, )
    avoids_abrupt_meneuvers = models.IntegerField(_('Avoids abrupt maneuvers'), choices=NUMBER_CHOICES, default=0, )
    backs_one_item = models.IntegerField(_('Backs one item at a time'), choices=NUMBER_CHOICES, default=0, )
    safe_while_connecting_dolly = models.IntegerField(_('Safe while connecting dolly'),
                                                      choices=NUMBER_CHOICES,
                                                      default=0, )
    avoid_shifting_load = models.IntegerField(_('Avoid Shifting load'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Multiple trailers"


# 18. Hills
class BTWHills(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    proper_gear_up_down = models.IntegerField(_('Proper gear up or down'), choices=NUMBER_CHOICES, default=0, )
    avoids_rolling_back = models.IntegerField(_('Avoids rolling back H/V'), choices=NUMBER_CHOICES, default=0, )
    test_brakes_prior = models.IntegerField(_('Test brakes prior'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Hills"


# 19. Passing
class BTWPassing(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    sufficient_space_to_pass = models.IntegerField(_('Sufficient Space to Pass'), choices=NUMBER_CHOICES, default=0, )
    signals_property = models.IntegerField(_('Signals Property'), choices=NUMBER_CHOICES, default=0, )
    check_mirrors = models.IntegerField(_('Checks Mirrors'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Passing"


# 20. General Safety and DOT adherence
class BTWGeneralSafetyAndDOTAdherence(models.Model):
    btw = models.OneToOneField('safe_driver.SafeDriveBTW', on_delete=models.CASCADE, null=False)

    avoids_crowding_effect = models.IntegerField(_('Avoids crowding effect'), choices=NUMBER_CHOICES, default=0, )
    stays_right_or_correct_lane = models.IntegerField(_('Stays to the right/correct lane'), choices=NUMBER_CHOICES,
                                                      default=0, )
    aware_hours_of_service = models.IntegerField(_('Aware of hours of service'), choices=NUMBER_CHOICES, default=0, )
    proper_use_off_mirrors = models.IntegerField(_('Proper use of mirrors'), choices=NUMBER_CHOICES, default=0, )
    self_confident_not_complacement = models.IntegerField(_('Self confident not complacent'), choices=NUMBER_CHOICES,
                                                          default=0, )
    check_instruments = models.IntegerField(_('Checks instruments'), choices=NUMBER_CHOICES, default=0, )
    uses_horn_properly = models.IntegerField(_('Uses horn properly'), choices=NUMBER_CHOICES, default=0, )
    maintains_dot_log = models.IntegerField(_('Maintains DOT log'), choices=NUMBER_CHOICES, default=0, )
    drives_defensively = models.IntegerField(_('Drives defensively'), choices=NUMBER_CHOICES, default=0, )
    company_haz_mat_protocol = models.IntegerField(_('Company Haz Mat protocol'), choices=NUMBER_CHOICES, default=0, )
    air_cans_or_line_moisture_free = models.IntegerField(_('Air cans/lines free of moisture'), choices=NUMBER_CHOICES,
                                                         default=0, )
    avoid_distractions_while_driving = models.IntegerField(_('Avoid distractions while driving'),
                                                           choices=NUMBER_CHOICES,
                                                           default=0, )
    works_safely_to_avoid_injuries = models.IntegerField(_('Works safely to avoid injuries'), choices=NUMBER_CHOICES,
                                                         default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - General Safety and DOT adherence"


# VRT
class SafeDriveVRT(models.Model):
    student = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='vrt_student',
                                   null=False)

    date = models.DateField(_('Date'), default=None, null=True, blank=True)
    start_time = models.TimeField(_('Start Time'), null=True, blank=True, default=None, )
    end_time = models.TimeField(_('End Time'), null=True, blank=True, default=None)
    equiment_used = models.CharField(_('Equipment'), default=None, max_length=120, null=True, blank=True)

    remarks = models.TextField(_('Remarks'), default=None, null=True, blank=True)

    medical_card_expire_date = models.DateField(_('Medical Card Expiration Date'), default=None, null=True, blank=True)
    state = models.CharField(_('State'), default=None, max_length=120, null=True, blank=True)

    type_of_power_unit = models.CharField(_('Type of Power Unit'), default=None, max_length=120, null=True, blank=True)
    trailer_length = models.CharField(_('Trailer Unit'), max_length=120, null=True, blank=True)
    number_of_trailers = models.IntegerField(_('Number of Trailers'), default=None, null=True, blank=True)
    miles = models.IntegerField(_('Miles'), default=None, null=True, blank=True)

    driver_signature = models.ImageField(_('Driver Signature'), upload_to='signatures/vrt/driver/', default=None,
                                         null=True, blank=True)
    evaluator_signature = models.ImageField(_('Evaluator Signature'), upload_to='signatures/vrt/evaluator/',
                                            default=None, null=True,
                                            blank=True)

    print = models.CharField(_('Print'), default=None, max_length=120, null=True, blank=True)
    title = models.CharField(_('Title'), default=None, max_length=250, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "Vehicle Registration Tax"


VRT_CHOICES = (
    (0, 'N/A'),
    (1, 'Imp'),
    (2, 'Ok'),
)


# 1. VRT Pre Trip
class VRTPreTrip(models.Model):
    vrt = models.OneToOneField('safe_driver.SafeDriveVRT', on_delete=models.CASCADE, null=False)

    emergency_device = models.IntegerField(_('Emergency Device'), choices=VRT_CHOICES, default=0, )
    documents = models.IntegerField(_('Documents'), choices=VRT_CHOICES, default=0, )
    htr_air_dfr = models.IntegerField(_('Htr/Air/Dfr'), choices=VRT_CHOICES, default=0, )
    wipers = models.IntegerField(_('Wipers'), choices=VRT_CHOICES, default=0, )
    pedals = models.IntegerField(_('Pedals'), choices=VRT_CHOICES, default=0, )
    gauges = models.IntegerField(_('Gauges'), choices=VRT_CHOICES, default=0, )
    switches = models.IntegerField(_('Switches'), choices=VRT_CHOICES, default=0, )
    steering = models.IntegerField(_('Steering'), choices=VRT_CHOICES, default=0, )
    mirrors = models.IntegerField(_('Mirrors'), choices=VRT_CHOICES, default=0, )
    horn = models.IntegerField(_('Horn'), choices=VRT_CHOICES, default=0, )
    engine = models.IntegerField(_('Engine'), choices=VRT_CHOICES, default=0, )
    fluids = models.IntegerField(_('Fluids'), choices=VRT_CHOICES, default=0, )
    lights = models.IntegerField(_('Lights'), choices=VRT_CHOICES, default=0, )
    reflectors = models.IntegerField(_('Reflectors'), choices=VRT_CHOICES, default=0, )
    air_lines = models.IntegerField(_('Air Lines'), choices=VRT_CHOICES, default=0, )
    coupling_devices = models.IntegerField(_('Coupling Devices'), choices=VRT_CHOICES, default=0, )
    tires = models.IntegerField(_('Tires'), choices=VRT_CHOICES, default=0, )
    wheels = models.IntegerField(_('Wheels'), choices=VRT_CHOICES, default=0, )
    chassis_undercarriage = models.IntegerField(_('Chassis Undercarriage'), choices=VRT_CHOICES, default=0, )
    leaks_air_fluid = models.IntegerField(_('Leaks/Air/Fluid'), choices=VRT_CHOICES, default=0, )
    drain_air_tanks = models.IntegerField(_('Drain Air Tanks'), choices=VRT_CHOICES, default=0, )
    park_or_emer_brake = models.IntegerField(_('Park/Emer Brake'), choices=VRT_CHOICES, default=0, )
    serv_brake_test = models.IntegerField(_('Serv Brake Test'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Pre Trip"


# 2. VRT Coupling
class VRTCoupling(models.Model):
    vrt = models.OneToOneField('safe_driver.SafeDriveVRT', on_delete=models.CASCADE, null=False)

    equipment_alignment = models.IntegerField(_('Equipment Alignment'), choices=VRT_CHOICES, default=0, )
    air_lines_or_light_cord = models.IntegerField(_('Air Lines/Light Cord'), choices=VRT_CHOICES, default=0, )
    check_for_hazards = models.IntegerField(_('Check for Hazards'), choices=VRT_CHOICES, default=0, )
    back_under_slowly = models.IntegerField(_('Back Under Slowly'), choices=VRT_CHOICES, default=0, )
    test_tug = models.IntegerField(_('Test Tug'), choices=VRT_CHOICES, default=0, )
    secures_equip_properly = models.IntegerField(_('Secures Equip Properly'), choices=VRT_CHOICES, default=0, )
    verfiy_couple_secure = models.IntegerField(_('Verify Couple Secure'), choices=VRT_CHOICES, default=0, )

    raise_landing_gear = models.IntegerField(_('Raise Landing Gear'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Coupling"


# 3. VRT Uncoupling
class VRTUncoupling(models.Model):
    vrt = models.OneToOneField('safe_driver.SafeDriveVRT', on_delete=models.CASCADE, null=False)

    secure_equip_properly = models.IntegerField(_('Secure Equip Properly'), choices=VRT_CHOICES, default=0, )
    chock_wheels = models.IntegerField(_('Chock Wheels'), choices=VRT_CHOICES, default=0, )
    lower_landing_gear = models.IntegerField(_('Lower Landing Gear'), choices=VRT_CHOICES, default=0, )
    air_lanes_or_light_cord = models.IntegerField(_('Air Lines/Light Cord'), choices=VRT_CHOICES, default=0, )
    unlock_fifth_gear = models.IntegerField(_('Unlock 5th Wheel'), choices=VRT_CHOICES, default=0, )
    lower_trailer_gently = models.IntegerField(_('Lower trailer Gently'), choices=VRT_CHOICES, default=0, )

    test = models.IntegerField(_('Verify Firm to Ground'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Uncoupling"


# 4. VRT Engine Operations
class VRTEngineOperations(models.Model):
    vrt = models.OneToOneField('safe_driver.SafeDriveVRT', on_delete=models.CASCADE, null=False)

    lugging = models.IntegerField(_('Lugging'), choices=VRT_CHOICES, default=0, )
    over_revving = models.IntegerField(_('Over Revving'), choices=VRT_CHOICES, default=0, )
    check_gauges = models.IntegerField(_('Checks Gauges'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Engine Operations"


# 5. VRT Start Engine
class VRTStartEngine(models.Model):
    vrt = models.OneToOneField('safe_driver.SafeDriveVRT', on_delete=models.CASCADE, null=False)

    park_brake_applied = models.IntegerField(_('Park Brake Applied'), choices=VRT_CHOICES, default=0, )
    transmission_in_neutral = models.IntegerField(_('Transmission in Neutral'), choices=VRT_CHOICES, default=0, )
    clutch_depressed = models.IntegerField(_('Clutch Depressed'), choices=VRT_CHOICES, default=0, )
    starter_used_properly = models.IntegerField(_('Starter Used Properly'), choices=VRT_CHOICES, default=0, )
    reads_gauges = models.IntegerField(_('Reads Gauges'), choices=VRT_CHOICES, default=0, )
    seat_belt = models.IntegerField(_('Seat Belt'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Start Engine"


# 6. VRT Use Clutch
class VRTUseClutch(models.Model):
    vrt = models.OneToOneField('safe_driver.SafeDriveVRT', on_delete=models.CASCADE, null=False)
    disengages_completely = models.IntegerField(_('Disengages Completely'), choices=VRT_CHOICES, default=0, )
    engages_smoothly = models.IntegerField(_('Engages Smoothly'), choices=VRT_CHOICES, default=0, )
    double_clutches_properly = models.IntegerField(_('Double Clutches Properly'), choices=VRT_CHOICES, default=0, )
    rides_clutch = models.IntegerField(_('Rides Clutch'), choices=VRT_CHOICES, default=0, )

    coast = models.IntegerField(_('Coast'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Use Clutch"


# 7. VRT Use of Transmission
class VRTUseOfTransmission(models.Model):
    vrt = models.OneToOneField('safe_driver.SafeDriveVRT', on_delete=models.CASCADE, null=False)

    starts_in_low_gear = models.IntegerField(_('Starts in Low Gear'), choices=VRT_CHOICES, default=0, )
    proper_sequence = models.IntegerField(_('Proper Sequence'), choices=VRT_CHOICES, default=0, )
    shifts_without_classing = models.IntegerField(_('Shifts without classing'), default=0, )
    timing_up = models.IntegerField(_('Timing Up'), choices=VRT_CHOICES, default=0, )
    timing_down = models.IntegerField(_('Timing Down'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Use of Transmission"


# 8. VRT Use of Brakes
class VRTUseOfBrakes(models.Model):
    vrt = models.OneToOneField('safe_driver.SafeDriveVRT', on_delete=models.CASCADE, null=False)

    smoothly_applies = models.IntegerField(_('Smoothly Applies'), choices=VRT_CHOICES, default=0, )
    stops_smoothly = models.IntegerField(_('Stops Smoothly'), choices=VRT_CHOICES, default=0, )

    fans_brakes = models.IntegerField(_('Fans Brakes'), choices=VRT_CHOICES, default=0, )
    engine_assist_brake = models.IntegerField(_('Engine Assist Brake'), choices=VRT_CHOICES, default=0, )
    foot_brake_only = models.IntegerField(_('Foot Brake Only'), choices=VRT_CHOICES, default=0, )

    hv_when_stopped_traffic = models.IntegerField(_('H/V when Stopped Traffic'),
                                                  choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Use of Brakes"


# 9. VRT Backing
class VRTBacking(models.Model):
    vrt = models.OneToOneField('safe_driver.SafeDriveVRT', on_delete=models.CASCADE, null=False)

    checks_rear = models.IntegerField(_('Checks Rear'), choices=VRT_CHOICES, default=0, )
    communicates = models.IntegerField(_('Communicates'), choices=VRT_CHOICES, default=0, )
    backs_slowly = models.IntegerField(_('Backs Slowly'), choices=VRT_CHOICES, default=0, )
    checks_mirror = models.IntegerField(_('Checks Mirror'), choices=VRT_CHOICES, default=0, )
    uses_other_aids = models.IntegerField(_('Uses Other Aids'), choices=VRT_CHOICES, default=0, )
    looks_out_window = models.IntegerField(_('Looks Out Window'), choices=VRT_CHOICES, default=0, )
    steers_correctly = models.IntegerField(_('Steers Correctly'), choices=VRT_CHOICES, default=0, )

    does_not_hit_dock = models.IntegerField(_('Doesn’t Hit Dock'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Backing"
        verbose_name_plural = "VRT - Backings"


# 10. VRT Parking
class VRTParking(models.Model):
    vrt = models.OneToOneField('safe_driver.SafeDriveVRT', on_delete=models.CASCADE, null=False)

    does_not_hit_dock = models.IntegerField(_('Doesn’t Hit Dock'), choices=VRT_CHOICES, default=0, )
    curbs_wheel = models.IntegerField(_('Curbs Wheel'), choices=VRT_CHOICES, default=0, )
    chocks_wheel = models.IntegerField(_('Chocks Wheel'), choices=VRT_CHOICES, default=0, )
    parking_brake_applied = models.IntegerField(_('Parking Brake Applied'), choices=VRT_CHOICES, default=0, )
    transmission_neutral = models.IntegerField(_('Transmission Neutral'), choices=VRT_CHOICES, default=0, )

    engine_off_pull_key = models.IntegerField(_('Engine Off - Pull Key'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Parking"


# 11. VRT Driving Habits
class VRTDrivingHabits(models.Model):
    vrt = models.OneToOneField('safe_driver.SafeDriveVRT', on_delete=models.CASCADE, null=False)

    trafic_signals = models.IntegerField(_('Traffic Signals'), choices=VRT_CHOICES, default=0, )
    warning_signals = models.IntegerField(_('Warning Signals'), choices=VRT_CHOICES, default=0, )
    use_of_horn = models.IntegerField(_('Use of Horn'), choices=VRT_CHOICES, default=0, )
    steering = models.IntegerField(_('Steering'), choices=VRT_CHOICES, default=0, )
    intersections = models.IntegerField(_('Intersections'), choices=VRT_CHOICES, default=0, )
    use_of_lanes = models.IntegerField(_('Use of Lanes'), choices=VRT_CHOICES, default=0, )
    right_of_way = models.IntegerField(_('Right of Way'), choices=VRT_CHOICES, default=0, )
    following = models.IntegerField(_('Following'), choices=VRT_CHOICES, default=0, )
    right_of_turns = models.IntegerField(_('Right Turns'), choices=VRT_CHOICES, default=0, )
    left_turns = models.IntegerField(_('Left Turns'), choices=VRT_CHOICES, default=0, )
    speed_control = models.IntegerField(_('Speed Control'), choices=VRT_CHOICES, default=0, )
    use_of_mirrors = models.IntegerField(_('Use of Mirrors'), choices=VRT_CHOICES, default=0, )
    passing = models.IntegerField(_('Passing'), choices=VRT_CHOICES, default=0, )
    alertness = models.IntegerField(_('Alertness'), choices=VRT_CHOICES, default=0, )
    area_knowledge = models.IntegerField(_('Area Knowledge'), choices=VRT_CHOICES, default=0, )

    defensive_driving = models.IntegerField(_('Defensive Driving'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Driving Habits"


# 12. VRT Post Trip
class VRTPostTrip(models.Model):
    vrt = models.OneToOneField('safe_driver.SafeDriveVRT', on_delete=models.CASCADE, null=False)

    lights = models.IntegerField(_('Lights'), choices=VRT_CHOICES, default=0, )
    reflectors = models.IntegerField(_('Reflectors'), choices=VRT_CHOICES, default=0, )
    body_damage = models.IntegerField(_('Body Damage'), choices=VRT_CHOICES, default=0, )
    tires = models.IntegerField(_('Tires'), choices=VRT_CHOICES, default=0, )
    hub_heat = models.IntegerField(_('Hub Heat'), choices=VRT_CHOICES, default=0, )

    leaks = models.IntegerField(_('Leaks'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Post Trip"



