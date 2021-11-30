from django.contrib import admin
from .models import *

from .forms import *


# Register your models here.
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'created', 'updated']
    search_fields = ['title', 'id']


@admin.register(StudentTestExam)
class StudentTestExamAdmin(admin.ModelAdmin):
    list_display = ['test', 'exam', 'created']
    search_fields = ['test', 'exam']
    autocomplete_fields = ('test', 'exam')


class QuestionChoiceInline(admin.TabularInline):
    model = QuestionChoice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['get_qs_short_title', 'question_type', 'exam', 'position', 'created', 'updated']
    search_fields = ['title', 'question_type', ]
    autocomplete_fields = ['exam', ]
    inlines = [QuestionChoiceInline]
    form = QuestionCreateForm

    def get_qs_short_title(self, instance):
        if len(instance.title) > 50:
            return '%s ...' % instance.title[:50]
        return '%s' % instance.title

    get_qs_short_title.short_description = 'Title'
    get_qs_short_title.ordering = 'title'

    def get_form(self, request, obj=None, change=True, **kwargs):
        # if obj is None:
        #     self.exclude('choices', 'correct_choices')
        if obj:
            return QuestionChangeForm
        return QuestionCreateForm
        # return super(QuestionAdmin, self).get_form(request, obj, kwargs)


@admin.register(QuestionChoice)
class QuestionChoiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'question', 'get_question_exam', 'position', 'created', 'updated']
    search_fields = ['title']

    # prepopulated_fields = {
    #     'question': ('title', )
    # }
    # autocomplete_fields = ('question',)
    def get_question_exam(self, instance):
        return '%s' % instance.question.exam

    get_question_exam.short_description = 'Exam'


@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ['test_exam', 'question', 'get_question_type', 'get_question_exam', 'check_answer',
                    'created', 'updated']
    readonly_fields = ['get_question_exam', 'get_question_type', 'check_answer']
    autocomplete_fields = ('question', 'answers')
    form = QuestionAnswerForm

    def get_question_type(self, instance):
        return '%s' % instance.question.get_question_type_display()

    get_question_type.short_description = 'Type'

    def get_question_exam(self, instance):
        return '%s' % instance.question.exam.title

    get_question_exam.short_description = 'Exam'
