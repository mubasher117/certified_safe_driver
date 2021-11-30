from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

EXAM_TYPE_CHOICES = (
    ('defensive_driving', 'Defensive Driving Quiz'),
    ('distracted', 'Distracted Quiz'),
)


# Create your models here.
class Exam(models.Model):
    title = models.CharField(_('Title'), max_length=250, null=False)
    description = models.TextField(_('Description'), null=True, blank=True)

    exam_type = models.CharField(_('Exam Type'), choices=EXAM_TYPE_CHOICES, max_length=32, default=None, null=True,
                                 blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.title:
            return '%s' % self.title
        return '%s: %s' % (self.pk, self.get_exam_type_display())

    @property
    def total_questions(self):
        return self.exam_questions.count()

    class Meta:
        ordering = ('title',)
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'

        constraints = [
            models.UniqueConstraint(
                fields=['exam_type'], condition=models.Q(exam_type__isnull=False),
                name='unique_exam_type'
            )
        ]

    def clean(self):
        check_exam = Exam.objects.filter(exam_type__isnull=False, exam_type=self.exam_type)
        if self.pk:
            check_exam = check_exam.exclude(pk=self.pk)

        if check_exam.count() > 0:
            raise ValidationError({
                'exam_type': 'You already have an exam for this exam type.'
            })


QUESTION_TYPE_CHOICES = (
    ('multiple', 'Multiple'),
    ('single', 'Single'),
)


class Question(models.Model):
    exam = models.ForeignKey('csd_quizes.Exam', on_delete=models.CASCADE, related_name='exam_questions')

    title = models.CharField(_('Title'), max_length=250, null=False)
    question_type = models.CharField(_('Question Type'), choices=QUESTION_TYPE_CHOICES, default='single', max_length=20)
    choices = models.ManyToManyField('csd_quizes.QuestionChoice', related_name='question_choices', blank=True)
    correct_choices = models.ManyToManyField('csd_quizes.QuestionChoice', related_name='question_answer_choices',
                                             blank=True)

    position = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Exam: % s - %s' % (self.exam.pk, self.title)

    class Meta:
        ordering = ('position',)
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class QuestionChoice(models.Model):
    question = models.ForeignKey('csd_quizes.Question', on_delete=models.CASCADE, default=None,
                                 related_name='choice_question')
    title = models.CharField(_('Title'), max_length=250, null=False)
    # is_answer = models.BooleanField(default=False)

    position = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('question__position', 'position',)
        verbose_name = 'Question Choice'
        verbose_name_plural = 'Question Choices'


class StudentTestExam(models.Model):
    test = models.ForeignKey('safe_driver.StudentTest', on_delete=models.CASCADE, default=None, null=False,
                             related_name='exam_studenttest')

    exam = models.ForeignKey('csd_quizes.Exam', on_delete=models.CASCADE, default=None, null=False,
                             related_name='studenttest_exam')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def is_passed(self):
        return False

    def __str__(self):
        return '%s' % self.exam.title

    class Meta:
        ordering = ('created',)
        verbose_name = 'Student Test Exam'
        verbose_name_plural = 'Student Test Exams'

        unique_together = ('test', 'exam',)


class QuestionAnswer(models.Model):
    test_exam = models.ForeignKey('csd_quizes.StudentTestExam', on_delete=models.CASCADE, default=None, null=False,
                                  related_name='answer_student_test_exam')
    question = models.ForeignKey('csd_quizes.Question', on_delete=models.CASCADE, related_name='answer_question')
    answers = models.ManyToManyField('csd_quizes.QuestionChoice')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def check_answer(self):
        q1 = self.question.correct_choices.all()
        q2 = self.answers.all()
        if not q1.count() < 1 and not q2.count() < 1:
            return set(q1) == set(q2)
        return False

    def __str__(self):
        return '%s' % self.question.title[:50]

    class Meta:
        ordering = ('question__position', 'answers__position')
        verbose_name = 'Question Answer'
        verbose_name_plural = 'Question Answers'

        constraints = [
            models.UniqueConstraint(
                fields=['test_exam', 'question'], name='answer_test_exam_question_unique_contraint'
            )
        ]
