from django.urls import path
from .test_quiz_views import *

urlpatterns = [
    path('exams/', StudentTestExams.as_view()),
    path('exams/<int:exam_id>/', StudentTestExamDetail.as_view()),
    path('exams/<int:exam_id>/submit-answers/', TestExamSubmitAnswers.as_view()),
    path('exams/<int:exam_id>/get-answers/', TestExamAnswerList.as_view()),

    # defensive_driving
    path('quizes/defensive_driving/', StudentTestDefensiveDrivingExamDetail.as_view()),
    path('quizes/defensive_driving/submit-answers/', DefensiveDrivingExamSubmitAnswers.as_view()),
    path('quizes/defensive_driving/get-answers/', DefensiveDrivingExamAnswerList.as_view()),

    # distracted
    path('quizes/distracted/', StudentTestDistractedExamDetail.as_view()),
    path('quizes/distracted/submit-answers/', DistractedExamSubmitAnswers.as_view()),
    path('quizes/distracted/get-answers/', DistractedExamAnswerList.as_view()),
]
