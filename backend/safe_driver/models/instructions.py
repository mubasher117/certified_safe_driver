from django.db import models
from django.utils.translation import ugettext_lazy as _


class InstructionBTWBus(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=True, blank=False)
    instruction = models.TextField()

    field_name = models.CharField(_('Field Name'), max_length=250, default=None, null=False,
                                  help_text='Type/select field name underscore and without any space matched with db '
                                            'field')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.field_name

    class Meta:
        ordering = ('field_name',)
        verbose_name = 'Instruction for BTW BUS'
        verbose_name_plural = 'Instructions for BTW BUS'
        constraints = [
            models.UniqueConstraint(
                fields=['db_table', 'field_name'], condition=models.Q(db_table__isnull=False),
                name='instruction_btw_bus_db_field_unique'
            )
        ]


class InstructionBTWClassA(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=True, blank=False)
    instruction = models.TextField()

    field_name = models.CharField(_('Field Name'), max_length=250, default=None, null=False,
                                  help_text='Type/select field name underscore and without any space matched with db '
                                            'field')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.field_name

    class Meta:
        ordering = ('field_name',)
        verbose_name = 'Instruction for BTW Class A'
        verbose_name_plural = 'Instructions for BTW Class A'
        constraints = [
            models.UniqueConstraint(
                fields=['db_table', 'field_name'], condition=models.Q(db_table__isnull=False),
                name='instruction_btw_class_a_db_field_unique'
            )
        ]


class InstructionBTWClassB(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=True, blank=False)
    instruction = models.TextField()

    field_name = models.CharField(_('Field Name'), max_length=250, default=None, null=False,
                                  help_text='Type/select field name underscore and without any space matched with db '
                                            'field')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.field_name

    class Meta:
        ordering = ('field_name',)
        verbose_name = 'Instruction for BTW Class B'
        verbose_name_plural = 'Instructions for BTW Class B'
        constraints = [
            models.UniqueConstraint(
                fields=['db_table', 'field_name'], condition=models.Q(db_table__isnull=False),
                name='instruction_btw_class_b_db_field_unique'
            )
        ]


class InstructionBTWClassC(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=True, blank=False)
    instruction = models.TextField()

    field_name = models.CharField(_('Field Name'), max_length=250, default=None, null=False,
                                  help_text='Type/select field name underscore and without any space matched with db '
                                            'field')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.field_name

    class Meta:
        ordering = ('field_name',)
        verbose_name = 'Instruction for BTW Class C'
        verbose_name_plural = 'Instructions for BTW Class C'
        constraints = [
            models.UniqueConstraint(
                fields=['db_table', 'field_name'], condition=models.Q(db_table__isnull=False),
                name='instruction_btw_class_c_db_field_unique'
            )
        ]


# Instructions for BTW Class C
class InstructionBTWClassP(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=True, blank=False)
    instruction = models.TextField()

    field_name = models.CharField(_('Field Name'), max_length=250, default=None, null=False,
                                  help_text='Type/select field name underscore and without any space matched with db '
                                            'field')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.field_name

    class Meta:
        ordering = ('field_name',)
        verbose_name = 'Instruction for BTW Class P'
        verbose_name_plural = 'Instructions for BTW Class P'
        constraints = [
            models.UniqueConstraint(
                fields=['db_table', 'field_name'], condition=models.Q(db_table__isnull=False),
                name='instruction_btw_class_p_db_field_unique'
            )
        ]


# pretrips
class InstructionPreTripBus(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=True, blank=False)
    instruction = models.TextField()

    field_name = models.CharField(_('Field Name'), max_length=250, default=None, null=False,
                                  help_text='Type/select field name underscore and without any space matched with db '
                                            'field')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.field_name

    class Meta:
        ordering = ('field_name',)
        verbose_name = 'Instruction for PreTrip BUS'
        verbose_name_plural = 'Instructions for PreTrip Bus'
        constraints = [
            models.UniqueConstraint(
                fields=['db_table', 'field_name'], condition=models.Q(db_table__isnull=False),
                name='instruction_pretrip_bus_db_field_unique'
            )
        ]


class InstructionPreTripClassA(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=True, blank=False)
    instruction = models.TextField()

    field_name = models.CharField(_('Field Name'), max_length=250, default=None, null=False,
                                  help_text='Type/select field name underscore and without any space matched with db '
                                            'field')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.field_name

    class Meta:
        ordering = ('field_name',)
        verbose_name = 'Instruction for PreTrip Class A'
        verbose_name_plural = 'Instructions for PreTrip Class A'
        constraints = [
            models.UniqueConstraint(
                fields=['db_table', 'field_name'], condition=models.Q(db_table__isnull=False),
                name='instruction_pretrip_class_a_db_field_unique'
            )
        ]


class InstructionPreTripClassB(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=True, blank=False)
    instruction = models.TextField()

    field_name = models.CharField(_('Field Name'), max_length=250, default=None, null=False,
                                  help_text='Type/select field name underscore and without any space matched with db '
                                            'field')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.field_name

    class Meta:
        ordering = ('field_name',)
        verbose_name = 'Instruction for PreTrip Class B'
        verbose_name_plural = 'Instructions for PreTrip Class B'
        constraints = [
            models.UniqueConstraint(
                fields=['db_table', 'field_name'], condition=models.Q(db_table__isnull=False),
                name='instruction_pretrip_class_b_db_field_unique'
            )
        ]


class InstructionPreTripClassC(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=True, blank=False)
    instruction = models.TextField()

    field_name = models.CharField(_('Field Name'), max_length=250, default=None, null=False,
                                  help_text='Type/select field name underscore and without any space matched with db '
                                            'field')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.field_name

    class Meta:
        ordering = ('field_name',)
        verbose_name = 'Instruction for PreTrip Class C'
        verbose_name_plural = 'Instructions for PreTrip Class C'
        constraints = [
            models.UniqueConstraint(
                fields=['db_table', 'field_name'], condition=models.Q(db_table__isnull=False),
                name='instruction_pretrip_class_c_db_field_unique'
            )
        ]


# class P
class InstructionPreTripClassP(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=True, blank=False)

    field_name = models.CharField(_('Field Name'), max_length=250, default=None, null=False,
                                  help_text='Type/select field name underscore and without any space matched with db '
                                            'field')
    instruction = models.TextField()

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.field_name

    class Meta:
        ordering = ('field_name',)
        verbose_name = 'Instruction for PreTrip Class P'
        verbose_name_plural = 'Instructions for PreTrip Class P'

        constraints = [
            models.UniqueConstraint(
                fields=['db_table', 'field_name'], condition=models.Q(db_table__isnull=False),
                name='instruction_pretrip_class_p_db_field_unique'
            )
        ]


# vrt
class InstructionVRT(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=True, blank=False)
    instruction = models.TextField()

    field_name = models.CharField(_('Field Name'), max_length=250, default=None, null=False,
                                  help_text='Type/select field name underscore and without any space matched with db '
                                            'field')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.field_name

    class Meta:
        ordering = ('field_name',)
        verbose_name = 'Instruction for VRT'
        verbose_name_plural = 'Instructions for VRT'
        constraints = [
            models.UniqueConstraint(
                fields=['db_table', 'field_name'], condition=models.Q(db_table__isnull=False),
                name='instruction_pretrip_vrt_db_field_unique'
            )
        ]


# SWP
class InstructionSWP(models.Model):
    db_table = models.CharField(_('DB Table'), max_length=250, default=None, null=True, blank=False)
    instruction = models.TextField()

    field_name = models.CharField(_('Field Name'), max_length=250, default=None, null=False,
                                  help_text='Type/select field name underscore and without any space matched with db '
                                            'field')

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.field_name

    class Meta:
        ordering = ('field_name',)
        verbose_name = 'Instruction for SWP'
        verbose_name_plural = 'Instructions for SWP'

        constraints = [
            models.UniqueConstraint(
                fields=['db_table', 'field_name'], condition=models.Q(db_table__isnull=False),
                name='instruction_swp_db_field_unique'
            )
        ]
