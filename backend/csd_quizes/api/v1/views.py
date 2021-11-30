from rest_framework.generics import *
from .serializers import *


class ExamList(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()


class QuestionListByExam(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = QuestionListWithCorrectSerializer
    queryset = Question.objects.all()
    pagination_class = None

    def get_queryset(self):
        return Question.objects.filter(exam_id=self.kwargs['exam_id'])


class DefensiveDrivingQuestionList(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = QuestionListWithCorrectSerializer
    queryset = Question.objects.all()
    pagination_class = None

    def get_queryset(self):
        return Question.objects.filter(exam__exam_type='defensive_driving').order_by('position')


class DistractedQuestionList(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = QuestionListWithCorrectSerializer
    queryset = Question.objects.all()
    pagination_class = None

    def get_queryset(self):
        return Question.objects.filter(exam__exam_type='distracted')
