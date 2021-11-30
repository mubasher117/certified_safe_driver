from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from safe_driver.models import StudentTest


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    # name = models.CharField(_("Name of User"), blank=True, null=True, max_length=255)
    middle_name = models.CharField(_("Middle Name"), blank=True, null=True, max_length=32)
    surname = models.CharField(_("Surname"), blank=True, null=True, max_length=32)

    is_student = models.BooleanField(default=True)
    is_instructor = models.BooleanField(default=False,
                                        help_text='Designates whether the instructor can log into this admin site.')

    home_phone_number = models.CharField(_("Home Phone Number"), default=None, blank=True, null=True, max_length=20)
    work_phone_number = models.CharField(_("Work Phone Number"), default=None, blank=True, null=True, max_length=20)
    mobile_number = models.CharField(_("Mobile Number"), default=None, blank=True, null=True, max_length=20)
    phone = models.CharField(_("Phone"), default=None, blank=True, null=True, max_length=20)

    send_gps_location = models.BooleanField(_('Send GPS Location'), default=False)

    date_of_birth = models.DateField(_("Date of Birth"), default=None, null=True, blank=True)

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    sex = models.CharField(_('Sex'), default=None, null=True, blank=True, max_length=6)

    @property
    def full_name(self):
        if self.first_name and self.first_name != "":
            return self.get_full_name().strip()
        return '%s' % self.username

    @property
    def total_tests(self):
        total = self.student_tests.count()
        # return StudentTest.objects.filter(student=self).count()
        return total

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
