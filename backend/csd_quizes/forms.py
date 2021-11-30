from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelect
from django.core.exceptions import ValidationError
from .models import Exam, Question, QuestionAnswer, QuestionChoice


class QuestionAnswerForm(forms.ModelForm):

    def clean(self):
        data = self.cleaned_data
        answers = []
        question = None
        if 'answers' in data:
            answers = data.get('answers')

        if 'question' in data:
            question = data.get('question')

        if question:
            if question.question_type == 'single' and len(answers) > 1:
                raise ValidationError({'answers': 'You can only select one answer'})

            if len(answers) > 0:
                correct_choices = question.correct_choices.all()
                print(correct_choices)
                if not correct_choices.filter(id__in=answers):
                    raise ValidationError({'answers': 'Select Valid answers for the selected questions'})

    class Meta:
        model = QuestionAnswer
        fields = '__all__'


class QuestionCreateForm(forms.ModelForm):
    # exam = forms.ModelChoiceField(
    #     queryset=Exam.objects.all(),
    #     widget=AutocompleteSelect(Question._meta.get_field('exam').remote_field, admin.AdminSite))

    class Meta:
        model = Question
        fields = ('exam', 'title', 'question_type', 'position', )


class QuestionChangeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            qs = QuestionChoice.objects.filter(question=self.instance)
            self.fields['correct_choices'].queryset = qs

    class Meta:
        model = Question
        fields = ('exam', 'title', 'question_type', 'correct_choices', 'position', )
