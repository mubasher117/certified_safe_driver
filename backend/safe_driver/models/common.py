import os

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _

from safe_driver.image_functions import signature_image_folder

import datetime

time_now = datetime.datetime.now()

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
    company_id = models.CharField(_("Company ID"), max_length=32, default=None, null=True, blank=True)
    city = models.CharField(_("City"), max_length=32, default=None, null=True, blank=True)
    state = models.CharField(_("State"), max_length=32, default=None, null=True, blank=True)
    phone = models.CharField(_("Phone"), max_length=32, default=None, null=True, blank=True)
    address = models.CharField(_("Address"), max_length=150, default=None, null=True, blank=True)
    zip_code = models.CharField(_("ZIP Code"), max_length=20, default=None, null=True, blank=True)

    instructors = models.ManyToManyField('users.User', blank=True)
    # instructor = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)

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

        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['name', 'instructor', ],
        #         condition=models.Q(instructor__isnull=False),
        #         name='instructor_unique_company_name'
        #     )
        # ]


class StudentTest(models.Model):
    TEST_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    )

    student = models.ForeignKey('users.User', on_delete=models.CASCADE, null=False, related_name='student_tests')
    instructor = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True,
                                   related_name='student_test_instructor')
    name = models.CharField(_('Name'), default="", null=True, blank=True, max_length=250)
    status = models.CharField(_('Test Status'), choices=TEST_STATUS_CHOICES, max_length=20, default='pending', )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        if self.name:
            return '%s' % self.name
        return 'Test - %s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "Student Test"
        verbose_name_plural = "Student Tests"


class Equipment(models.Model):
    # student = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='equip_student', null=False)
    test = models.ForeignKey('safe_driver.StudentTest', on_delete=models.CASCADE, null=False,
                             related_name='equip_student_test')

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
    # dolly_3 = models.CharField(max_length=32, default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s Equip - %s' % (self.test.student.full_name, self.pk)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"


class SafeDriveNote(models.Model):
    student = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='note_student',
                                null=False)
    test = models.ForeignKey('safe_driver.StudentTest', on_delete=models.CASCADE, null=True, blank=True)

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


def student_test_note_image_path(instance, filename):
    file_path = 'student_notes/note_{}/{}/{}/{}'.format(instance.test.id, time_now.year,
                                                        time_now.month, time_now.day)
    return os.path.join(file_path, filename)


# Student Test Notes
class StudentTestNote(models.Model):
    test = models.ForeignKey('safe_driver.StudentTest', on_delete=models.CASCADE, null=False,
                             related_name='note_test')

    note = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=student_test_note_image_path, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s Note - %s' % (self.test.student.full_name, self.pk)

    class Meta:
        ordering = ('test__student__first_name', 'test__student__last_name', '-created',)
        verbose_name = "Test Note"
        verbose_name_plural = "Test Notes"


class SafeDriveProd(models.Model):
    # student = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='prod_student',
    #                                null=False)
    test = models.OneToOneField('safe_driver.StudentTest', on_delete=models.CASCADE, null=False,
                                related_name='prod_student_test')

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

    miles = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=None, blank=True,
                                verbose_name='Miles')

    odometer = models.CharField(max_length=150, null=True, blank=True, default=None,
                                verbose_name='Odometer')

    route_number = models.CharField(_('Route Number'), max_length=50, default=None, null=True, blank=True)
    employee = models.CharField(_('Employee'), max_length=50, default=None, null=True, blank=True)
    driver_signature = models.ImageField(upload_to=signature_image_folder, default=None, null=True, blank=True)
    evaluator_signature = models.ImageField(upload_to=signature_image_folder, default=None, null=True, blank=True)
    company_rep_signature = models.ImageField(upload_to=signature_image_folder, default=None, null=True, blank=True)
    company_rep_name = models.CharField(max_length=150, null=True, blank=True, default=None,
                                        verbose_name='Company Rep. Name')

    observer_first_name = models.CharField(max_length=150, null=True, blank=True, default=None,
                                           verbose_name='Observer First Name')

    observer_last_name = models.CharField(max_length=150, null=True, blank=True, default=None,
                                          verbose_name='Observer Last Name')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def total_number(self):
        # sum_number = self.prod_item.aggregate(total=Sum('leave_building'))
        # total = self.start_work + self.leave_building + self.travel_path + self.speed + self.idle_time + \
        #         self.plan_ahead + self.turn_around + self.on_schedule + self.customer_contact + \
        #         self.not_ready_situations + self.brisk_pace + \
        #         self.finish_work
        #
        # return total
        sum_number = 0
        if self.prod_item.all():
            sum_number = sum([item.total_number for item in self.prod_item.all()])
        # print(sum_number)
        return sum_number

    class Meta:
        ordering = ('-created',)
        verbose_name = "Prod"
        verbose_name_plural = "Prods"


class ProdItem(models.Model):
    prod = models.ForeignKey('safe_driver.SafeDriveProd', on_delete=models.CASCADE, null=False,
                             related_name='prod_item')

    location = models.CharField(max_length=150, null=True, blank=True, default=None, verbose_name='Location')
    trailer = models.CharField(max_length=150, null=True, blank=True, default=None, verbose_name='Trailer')
    start_work = models.IntegerField(choices=NUMBER_CHOICES, default=0, verbose_name="Start Work")
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

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def total_number(self):
        total = self.start_work + self.leave_building + self.travel_path + self.speed + self.idle_time + \
                self.plan_ahead + self.turn_around + self.on_schedule + self.customer_contact + \
                self.not_ready_situations + self.brisk_pace + \
                self.finish_work

        return total

    class Meta:
        ordering = ('-created',)
        verbose_name = "Prod Item"
        verbose_name_plural = "Prod Items"


class SafeDriveEye(models.Model):
    test = models.OneToOneField('safe_driver.StudentTest', on_delete=models.CASCADE, null=False,
                                related_name='eye_student_test')

    start_time = models.TimeField(default=None, null=True, blank=True)
    stop_time = models.TimeField(default=None, null=True, blank=True)

    eye_movement = models.CharField(_('Eye Movement'), max_length=250, default=None, null=True, blank=True)

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
    eye_actions = JSONField(null=True, default=dict, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s Eye - %s' % (self.test.student.full_name, self.pk)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Eye"
