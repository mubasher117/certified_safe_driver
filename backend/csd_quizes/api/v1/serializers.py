from rest_framework import serializers
from csd_quizes.models import *


class ExamSerializer(serializers.ModelSerializer):
    total_questions = serializers.IntegerField(read_only=True)

    class Meta:
        model = Exam
        fields = '__all__'


class StudentTestExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTestExam
        fields = '__all__'


class QuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionChoice
        fields = '__all__'


class QuestionOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    choices = QuestionChoiceSerializer(many=True, source='choice_question')

    # def to_representation(self, instance):
    #     res = super(QuestionSerializer, self).to_representation(instance)
    #     if instance.choice_question:
    #         res['choices'] = QuestionChoiceSerializer(instance.choice_question, many=True).data
    #     return res

    class Meta:
        model = Question
        fields = '__all__'


class QuestionListWithoutCorrectSerializer(serializers.ModelSerializer):
    choices = QuestionChoiceSerializer(many=True, source='choice_question')

    class Meta:
        model = Question
        exclude = ('correct_choices',)


class QuestionListWithCorrectSerializer(serializers.ModelSerializer):
    choices = QuestionChoiceSerializer(many=True, source='choice_question')
    correct_choices = QuestionChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'
        # exclude = ('correct_choices',)
