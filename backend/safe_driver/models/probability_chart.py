from django.db import models
from django.utils.translation import ugettext_lazy as _

FACTOR_CHOICES = (
    ('animal', 'Animal'),
    ('backing', 'Backing'),
    ('cyclist', 'Cyclist'),
    ('entering_exiting', 'Entering/Exiting'),
    ('hazardous_materials', 'Hazardous Materials'),
    ('head_on_collision', 'Head-on Collision'),
    ('hit_in_rear', 'Hit in Rear'),
    ('hit_other_in_rear', 'Hit Other in Rear'),
    ('hit_parked_vehicle', 'Hit Parked Vehicle'),
    ('hit_stationary_object', 'Hit Stationary Object'),
    ('hit_while_parked', 'Hit While Parked'),
    ('intersection', 'Intersection'),
    ('jacknife', 'Jacknife'),
    ('moving_object', 'Moving Object'),
    ('parking_lot', 'Parking Lot'),
    ('rollaway', 'Rollaway'),
    ('sideswipe', 'Sideswipe'),
)

FACTOR_CHOICES_PRETRIPS = (
    ('inside_cab', 'Inside Cab'),
    ('coals', 'COALS'),
    ('engine_compartment', 'Engine Compartment'),
    ('vehicle_front', 'Vehicle Front'),
    ('both_sides_vehicle', 'Both Sides Vehicle'),
    ('vehicle_or_tractor_rear', 'Vehcile/Tractor Rear'),
    ('front_of_trailer_box', 'Front of Trailer Box - Header Board'),
    ('driver_side_trailer_or_box', 'Driver Side Trailer Or Box'),
    ('rear_trailer_and_box', 'Rear Trailer & Box'),
    ('passenger_side_trailer_or_box', 'Passenger Side Trailer Or Box'),
    ('dolly', 'Dolly'),
    ('post_trip', 'Post-Trip'),
)

SWP_FACTOR_CHOICES = (
    ('animal_bite', 'Animal Bite'),
    ('amputation', 'Amputation'),
    ('blunt_force_trauma', 'Blunt Force Trauma'),
    ('burn', 'Burn'),
    ('cut', 'Cut'),
    ('dehydration', 'Denydration'),
    ('fracture', 'Fracture'),
    ('frost_bite', 'Frost Bite'),
    ('heat_stress', 'Heat Stress'),
    ('sprain', 'Sprain'),
    ('spider_bite_sting', 'Spider Bite/Sting'),
    ('strain', 'Strain'),
    ('stress', 'Stess'),
    ('toxic_exposure', 'Toxic Exposure'),
)


class AccidentProbabilityValueBTWClassA(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=False, blank=False)
    model_name = models.CharField(_('Model Name'), max_length=250, default=None, null=True, blank=True)
    key = models.CharField(_('Key'), choices=FACTOR_CHOICES, max_length=32, default=None,
                           null=False, blank=False,
                           help_text='Type key name underscore and without any space')

    field_name = models.CharField(_('Field Name'), max_length=250, default=None, null=False,
                                  help_text='Type field name underscore and without any space matched with db field')

    value = models.DecimalField(_('Value'), default=None, decimal_places=2, max_digits=4, null=False, blank=False,
                                help_text='Postive Value')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.key

    class Meta:
        ordering = ('key', 'field_name')
        verbose_name = 'Accident Probability Value BTW Class A'
        verbose_name_plural = 'Accident Probability Value BTW Class A'
        constraints = [
            models.UniqueConstraint(fields=['db_table', 'key', 'field_name'],
                                    name='unique_model_key_field_btw_class_a'),
        ]


class AccidentProbabilityValueBTWClassB(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=False, blank=False)
    model_name = models.CharField(_('Model Name'), max_length=250, default=None, null=True, blank=True)
    key = models.CharField(_('Key'), choices=FACTOR_CHOICES, max_length=32, default=None,
                           null=False, blank=False,
                           help_text='Type key name underscore and without any space')

    field_name = models.CharField(_('Field'), max_length=250, default=None, null=False,
                                  help_text='Type field name underscore and without any space matched with db field')
    value = models.DecimalField(_('Value'), default=None, decimal_places=2, max_digits=4, null=False, blank=False,
                                help_text='Postive Value')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.key

    class Meta:
        ordering = ('key', 'field_name')
        verbose_name = 'Accident Probability Value BTW Class B'
        verbose_name_plural = 'Accident Probability Value BTW Class B'
        constraints = [
            models.UniqueConstraint(fields=['db_table', 'key', 'field_name'],
                                    name='unique_model_key_field_btw_class_b'),
        ]


class AccidentProbabilityValueBTWClassC(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=False, blank=False)
    model_name = models.CharField(_('Model Name'), max_length=250, default=None, null=True, blank=True)
    key = models.CharField(_('Key'), choices=FACTOR_CHOICES, max_length=32, default=None,
                           null=False, blank=False,
                           help_text='Type key name underscore and without any space')

    field_name = models.CharField(_('Field'), max_length=250, default=None, null=False,
                                  help_text='Type field name underscore and without any space matched with db field')
    value = models.DecimalField(_('Value'), default=None, decimal_places=2, max_digits=4, null=False, blank=False,
                                help_text='Postive Value')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.key

    class Meta:
        ordering = ('key', 'field_name')
        verbose_name = 'Accident Probability Value BTW Class C'
        verbose_name_plural = 'Accident Probability Value BTW Class C'
        constraints = [
            models.UniqueConstraint(fields=['db_table', 'key', 'field_name'],
                                    name='unique_model_key_field_btw_class_c'),
        ]


# for class p
class AccidentProbabilityValueBTWClassP(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=False, blank=False)
    model_name = models.CharField(_('Model Name'), max_length=250, default=None, null=True, blank=True)
    key = models.CharField(_('Key'), choices=FACTOR_CHOICES, max_length=32, default=None,
                           null=False, blank=False,
                           help_text='Type key name underscore and without any space')

    field_name = models.CharField(_('Field'), max_length=250, default=None, null=False,
                                  help_text='Type field name underscore and without any space matched with db field')
    value = models.DecimalField(_('Value'), default=None, decimal_places=2, max_digits=4, null=False, blank=False,
                                help_text='Postive Value')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.key

    class Meta:
        ordering = ('key', 'field_name')
        verbose_name = 'Accident Probability Value BTW Class P'
        verbose_name_plural = 'Accident Probability Value BTW Class P'
        constraints = [
            models.UniqueConstraint(fields=['db_table', 'key', 'field_name'], name='unique_model_key_field_btw_class_p'),
        ]


class AccidentProbabilityValueBTWBus(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=False, blank=False)
    model_name = models.CharField(_('Model Name'), max_length=250, default=None, null=True, blank=True)
    key = models.CharField(_('Key'), choices=FACTOR_CHOICES, max_length=32, default=None,
                           null=False, blank=False,
                           help_text='Type key name underscore and without any space')

    field_name = models.CharField(_('Field'), max_length=250, default=None, null=False,
                                  help_text='Type field name underscore and without any space matched with db field')
    value = models.DecimalField(_('Value'), default=None, decimal_places=2, max_digits=4, null=False, blank=False,
                                help_text='Postive Value')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.key

    class Meta:
        ordering = ('key', 'field_name')
        verbose_name = 'Accident Probability Value BTW BUS'
        verbose_name_plural = 'Accident Probability Value BTW BUS'
        constraints = [
            models.UniqueConstraint(fields=['db_table', 'key', 'field_name'], name='unique_model_key_field_btw_bus'),
        ]


# for pretrips
class AccidentProbabilityValuePreTripClassA(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=False, blank=False)
    model_name = models.CharField(_('Model Name'), max_length=250, default=None, null=True, blank=True)
    key = models.CharField(_('Key'), choices=FACTOR_CHOICES_PRETRIPS, max_length=32, default=None,
                           null=False, blank=False,
                           help_text='Type key name underscore and without any space')

    field_name = models.CharField(_('Field Name'), max_length=250, default=None, null=False,
                                  help_text='Type field name underscore and without any space matched with db field')

    value = models.DecimalField(_('Value'), default=None, decimal_places=2, max_digits=4, null=False, blank=False,
                                help_text='Postive Value')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.key

    class Meta:
        ordering = ('key', 'field_name')
        verbose_name = 'Accident Probability Value PreTrip Class A'
        verbose_name_plural = 'Accident Probability Value PreTrip Class A'

        constraints = [
            models.UniqueConstraint(fields=['db_table', 'key', 'field_name'],
                                    name='unique_model_key_field_pretrip_class_a'),
        ]


class AccidentProbabilityValuePreTripClassB(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=False, blank=False)
    model_name = models.CharField(_('Model Name'), max_length=250, default=None, null=True, blank=True)
    key = models.CharField(_('Key'), choices=FACTOR_CHOICES_PRETRIPS, max_length=32, default=None,
                           null=False, blank=False,
                           help_text='Type key name underscore and without any space')

    field_name = models.CharField(_('Field'), max_length=32, default=None, null=False,
                                  help_text='Type field name underscore and without any space matched with db field')
    value = models.DecimalField(_('Value'), default=None, decimal_places=2, max_digits=4, null=False, blank=False,
                                help_text='Postive Value')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.key

    class Meta:
        ordering = ('key', 'field_name')
        verbose_name = 'Accident Probability Value PreTrip Class B'
        verbose_name_plural = 'Accident Probability Value PreTrip Class B'
        constraints = [
            models.UniqueConstraint(fields=['db_table', 'key', 'field_name'],
                                    name='unique_model_key_field_pretrip_class_b'),
        ]


class AccidentProbabilityValuePreTripClassC(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=False, blank=False)
    model_name = models.CharField(_('Model Name'), max_length=250, default=None, null=True, blank=True)
    key = models.CharField(_('Key'), choices=FACTOR_CHOICES_PRETRIPS, max_length=32, default=None,
                           null=False, blank=False,
                           help_text='Type key name underscore and without any space')

    field_name = models.CharField(_('Field'), max_length=250, default=None, null=False,
                                  help_text='Type field name underscore and without any space matched with db field')
    value = models.DecimalField(_('Value'), default=None, decimal_places=2, max_digits=4, null=False, blank=False,
                                help_text='Postive Value')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.key

    class Meta:
        ordering = ('key', 'field_name')
        verbose_name = 'Accident Probability Value PreTrip Class C'
        verbose_name_plural = 'Accident Probability Value PreTrip Class C'
        constraints = [
            models.UniqueConstraint(fields=['db_table', 'key', 'field_name'],
                                    name='unique_model_key_field_pretrip_class_c'),
        ]


class AccidentProbabilityValuePreTripBus(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=False, blank=False)
    model_name = models.CharField(_('Model Name'), max_length=250, default=None, null=True, blank=True)
    key = models.CharField(_('Key'), choices=FACTOR_CHOICES_PRETRIPS, max_length=32, default=None,
                           null=False, blank=False,
                           help_text='Type key name underscore and without any space')

    field_name = models.CharField(_('Field'), max_length=250, default=None, null=False,
                                  help_text='Type field name underscore and without any space matched with db field')
    value = models.DecimalField(_('Value'), default=None, decimal_places=2, max_digits=4, null=False, blank=False,
                                help_text='Postive Value')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.key

    class Meta:
        ordering = ('key', 'field_name')
        verbose_name = 'Accident Probability Value PreTrip BUS'
        verbose_name_plural = 'Accident Probability Value PreTrip BUS'
        constraints = [
            models.UniqueConstraint(fields=['db_table', 'key', 'field_name'],
                                    name='unique_model_key_field_pretrip_bus'),
        ]


# for class p
class AccidentProbabilityValuePreTripClassP(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=False, blank=False)
    model_name = models.CharField(_('Model Name'), max_length=250, default=None, null=True, blank=True)
    key = models.CharField(_('Key'), choices=FACTOR_CHOICES_PRETRIPS, max_length=32, default=None,
                           null=False, blank=False,
                           help_text='Type key name underscore and without any space')

    field_name = models.CharField(_('Field'), max_length=250, default=None, null=False,
                                  help_text='Type field name underscore and without any space matched with db field')
    value = models.DecimalField(_('Value'), default=None, decimal_places=2, max_digits=4, null=False, blank=False,
                                help_text='Postive Value')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.key

    class Meta:
        ordering = ('key', 'field_name')
        verbose_name = 'Accident Probability Value PreTrip Class P'
        verbose_name_plural = 'Accident Probability Value PreTrip Class P'
        constraints = [
            models.UniqueConstraint(fields=['db_table', 'key', 'field_name'],
                                    name='unique_model_key_field_pretrip_class_p'),
        ]


# vrt


# swp
class InjuryProbabilityValueSWP(models.Model):
    db_table = models.CharField(_('Database Table'), max_length=250, default=None, null=False, blank=False, )
    key = models.CharField(_('Key'), choices=SWP_FACTOR_CHOICES, max_length=250, default=None,
                           null=False, blank=False,
                           help_text='Type key name underscore and without any space')

    field_name = models.CharField(_('Field'), max_length=250, default=None, null=False,
                                  help_text='Type field name underscore and without any space matched with db field')
    value = models.DecimalField(_('Value'), default=None, decimal_places=2, max_digits=4, null=False, blank=False,
                                help_text='Postive Value')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.get_key_display()

    class Meta:
        ordering = ('key', 'field_name')
        verbose_name = 'Injury Probability Value SWP'
        verbose_name_plural = 'Injury Probability Value SWP'
        # unique_together = ('key', 'field_name')
        constraints = [
            models.UniqueConstraint(fields=['db_table', 'key', 'field_name'], name='unique_value_fields_contraints')
        ]
