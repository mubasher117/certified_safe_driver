import os
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from safe_driver.models import StudentTest


# Create your models here.
class DefensiveDriverKnowledgeQuiz(models.Model):
    test = models.OneToOneField('safe_driver.StudentTest', on_delete=models.CASCADE, verbose_name=_('Student Test'))
    ahead_vehicle_eyes = models.BooleanField(_('How far ahead of your vehicle should your eyes be?'),
                                             default=False)

    ahead_aiming_vehicle = models.BooleanField(_('How far ahead should you be aiming your vehicle?'), default=False)
    avoid_staring_moving_eyes = models.BooleanField(_('You should avoid staring by moving your eyes every 2 seconds, '
                                                      'your eyes should never be away from the front for more than '
                                                      '2 seconds?'), default=False)
    types_of_distractions = models.BooleanField(_('What are the 3 types of distractions?'), default=False)
    intersection_slow_down = models.BooleanField(_('When approaching an intersection where the light is red, '
                                                   'do you slow down enough and attempt not to stop.'), default=False)
    intersection_check_left = models.BooleanField(_('Prior to entering an intersection you check left, right and back '
                                                    'to the left?'), default=False)
    identify_priority_items = models.BooleanField(_('What are the priority items that you should identify in the front '
                                                    'of your vehicle?'), default=False)
    stale_green_light_change = models.BooleanField(_('A stale green light is a light that you did not observe turn '
                                                     'green and you do not know when it will change?'), default=False)
    decision_point_changing_green_light = models.BooleanField(_('A decision point is the point prior to the '
                                                                'intersection, and if your vehicle reaches it without '
                                                                'the light changing from green, you will proceed '
                                                                'through the intersection without hesitation or '
                                                                'acceleration?'), default=False)
    intersection_count_three_seconds = models.BooleanField(_('Why should you count 3 seconds when starting up at an '
                                                             'intersection?'), default=False)
    following_distance_formula = models.BooleanField(_('What is the formula for Following Distance?'), default=False)
    following_distance_gives = models.BooleanField(_('Proper following distance gives you?'), default=False)
    parked_vehicle_life_signs = models.BooleanField(_('When approaching a parked vehicle, you should look for '
                                                      'signs of life?'), default=False)
    check_mirror = models.BooleanField(_('How often should you check a mirror?'), default=False)
    check_mirror_during_turn = models.BooleanField(_('You should check your mirrors 3 times during a turn (beginning, '
                                                     'middle and end).'), default=False)
    communication_tools = models.BooleanField(_('What tools do you use to communicate?'), default=False)
    advance_signal = models.BooleanField(_('You should signal a minimum of 100 feet in advance?'), default=False)
    advance_signal_100_feet = models.BooleanField(_('When backing, you should back in not out?'), default=False)
    backing_first_choice = models.BooleanField(_('What is your first choice when backing?'), default=False)
    look_while_backing_doubt = models.BooleanField(_('While backing, when in doubt - stop and get out and look?'),
                                                   default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Defensive Driver Knowledge Quiz'
        verbose_name_plural = 'Defensive Driver Knowledge Quiz'


# class TrainingLocation(models.Model):
#     name = models.CharField(_('Location Name'), max_length=100, unique=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return '%s' % self.name
#
#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'Training Location'
#         verbose_name_plural = 'Training Locations'


def csv_template_file_upload_path(instance, filename):
    return os.path.join('companies', 'company_%s' % instance.company.id, 'csv_templates', filename)


class TrainingRecordCSVTemplate(models.Model):
    company = models.OneToOneField('safe_driver.Company', on_delete=models.CASCADE, related_name='training_record_csv')

    csv_file = models.FileField(upload_to=csv_template_file_upload_path, null=False,
                                validators=[FileExtensionValidator(allowed_extensions=['csv'])],
                                help_text=_('File format .csv only'))

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.company.name

    class Meta:
        ordering = ('-company__name',)
        verbose_name = _('Training Record CSV Template')
        verbose_name_plural = _('Training Record CSV Templates')


TRAINING_LOCATION_CHOICES = (
    ('classroom', 'Classroom'),
    ('yard', 'Yard'),
    ('btw', 'BTW'),
    ('on_road', 'On Road',),
)


class DriverTrainigRecord(models.Model):
    test = models.ForeignKey('safe_driver.StudentTest', on_delete=models.CASCADE,
                             related_name='driver_training_record_test')
    day = models.PositiveIntegerField(_('Day'), default=1)
    title = models.CharField(_('Title'), max_length=250)

    location = models.CharField(choices=TRAINING_LOCATION_CHOICES, max_length=20, default=None, null=True, blank=True)

    planned = models.DecimalField(_('Planned'), default=0.00, decimal_places=2, max_digits=10)
    actual = models.DecimalField(_('Actual'), default=0.00, decimal_places=2, max_digits=10)
    initials = models.CharField(_('Initials'), max_length=250, default=None, null=True, blank=True)

    position = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Day %s: %s' % (self.day, self.title)

    @property
    def location_name(self):
        if self.location:
            return '%s' % self.get_location_display()

        return None

    class Meta:
        ordering = ('day', 'position')
        verbose_name = 'Driver Training Record'
        verbose_name_plural = 'Driver Training Records'


class TrainingRecordDayComment(models.Model):
    test = models.ForeignKey('safe_driver.StudentTest', on_delete=models.CASCADE,
                             related_name='driver_training_record_day_comments')
    day = models.PositiveIntegerField(_('Day'), default=1)
    body = models.TextField(_('Body'))

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s: Day %s' % (self.test.__str__(), self.day)

    class Meta:
        ordering = ('day',)
        verbose_name = 'Driver Training Record Day Comment'
        verbose_name_plural = 'Driver Training Record Day Comments'

        constraints = [
            models.UniqueConstraint(
                fields=['test', 'day'], name='training_record_comment_unique_by_day',
            )
        ]


class TrainingRecordComment(models.Model):
    training_record = models.OneToOneField('truck_driving_school.DriverTrainigRecord', related_name='comment',
                                           on_delete=models.CASCADE)
    body = models.TextField(_('Body'))

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Day %s: %s' % (self.training_record.day, self.training_record.title)

    class Meta:
        ordering = ('training_record__day', 'training_record__title')
        verbose_name = 'Training Record Comment'
        verbose_name_plural = 'Training Record Comments'


def school_hours_signature_path(instance, filename):
    return os.path.join('tests', 'test_%s' % instance.test_id, 'truck_driving_school', 'signatures', filename)


# Driver Training School Hours
class SchoolHours(models.Model):
    test = models.OneToOneField('safe_driver.StudentTest', on_delete=models.CASCADE,
                                related_name='driver_training_school_hours')

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    remarks = models.TextField(blank=True)
    completed_statisfactorily_on = models.CharField(default=None, max_length=250, null=True, blank=True)

    driver_trainer_signature = models.ImageField(upload_to=school_hours_signature_path, default=None, null=True,
                                                 blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.test

    @property
    def total_days(self):
        if self.end_date and self.start_date and (self.end_date > self.start_date):
            delta = self.end_date - self.start_date
            return delta.days
        return 0

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Driver Training School Hours')
        verbose_name_plural = _('Driver Training School Hours')


DEPARTMENT_CHOICES = (
    ('hr', 'HR'),
    ('trainer', 'Trainer'),
    ('company', 'Company'),
)


class DQFRequirementItem(models.Model):
    title = models.CharField(_('title'), max_length=250, null=False)
    department = models.CharField(_('Department'), choices=DEPARTMENT_CHOICES, max_length=10)

    position = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.title

    @property
    def department_display_name(self):
        return '%s' % self.get_department_display()

    class Meta:
        ordering = ('position',)
        verbose_name = _('DQF Requirement Item')
        verbose_name_plural = _('DQF Requirement Items')


# Driver Training School Control | DQF Requirements
class SchoolControlDQFRequirement(models.Model):
    test = models.ForeignKey('safe_driver.StudentTest', on_delete=models.CASCADE,
                             related_name='school_control_dqf_requirement')

    item = models.ForeignKey('truck_driving_school.DQFRequirementItem', on_delete=models.CASCADE)

    initials = models.CharField(_('Intials'), max_length=150, default=None, null=True, blank=True)
    date = models.DateField(default=None, null=True, blank=True, )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('item__position',)
        verbose_name = _('School Control DQF Requirement')
        verbose_name_plural = _('School Control DQF Requirements')


class TraineeBookItem(models.Model):
    title = models.CharField(_('title'), max_length=250, null=False)
    department = models.CharField(_('Department'), choices=DEPARTMENT_CHOICES, max_length=10)

    position = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.title

    @property
    def department_display_name(self):
        return '%s' % self.get_department_display()

    class Meta:
        ordering = ('position',)
        verbose_name = _('Trainee Book Item')
        verbose_name_plural = _('Trainee Book Items')


# Driver Training School Control | Trainee Book
class TraineeBook(models.Model):
    test = models.ForeignKey('safe_driver.StudentTest', on_delete=models.CASCADE,
                             related_name='school_control_trainee_books')

    item = models.ForeignKey('truck_driving_school.TraineeBookItem', on_delete=models.CASCADE)

    initials = models.CharField(_('Intials'), max_length=150, default=None, null=True, blank=True)
    date = models.DateField(default=None, null=True, blank=True, )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {}'.format(self.test.name, self.item.title)

    class Meta:
        ordering = ('item__position',)
        verbose_name = _('Trainee Book')
        verbose_name_plural = _('Trainee Books')
