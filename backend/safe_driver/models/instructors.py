from django.db import models
from django.utils.translation import ugettext_lazy as _

CLASS_CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)


class InstructorProfile(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, null=False, default=None,
                                related_name='instructor_profile')

    customer_number = models.CharField(_('Customer Number'), max_length=50, default=None, null=True, blank=True)
    contact_name = models.CharField(_('Contact Name'), max_length=32, default=None, null=True, blank=True)

    driver_id = models.CharField(_("Driver ID"), default=None, blank=True, null=True,
                                 max_length=32)
    driver_license_number = models.CharField(_("Driver License Num"), default=None, blank=True, null=True,
                                             max_length=120)
    driver_license_state = models.CharField(_("Driver License State"), default=None, blank=True, null=True,
                                            max_length=250)
    driver_license_expire_date = models.DateField(_("Dirver License Expiration Date"), default=None, null=True,
                                                  blank=True)
    driver_license_class = models.CharField(_('Driver License Class'), default=None, max_length=1,
                                            choices=CLASS_CHOICES,
                                            null=True, blank=True)

    endorsement = models.CharField(_('Endorsement'), max_length=120, null=True, blank=True)

    company = models.ForeignKey('safe_driver.Company', on_delete=models.CASCADE, blank=True, null=True,
                                related_name='instructor_company')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.pk

    def __str__(self):
        return "%s" % self.user.username

    class Meta:
        ordering = ('user__username',)
        verbose_name = 'Instructor Profile'
        verbose_name_plural = 'Instructor Profiles'
