from django.urls import path, include
from rest_framework.routers import DefaultRouter
from csd_quizes.api.v1 import views, viewsets

router = DefaultRouter()
router.register('exams', viewsets.ExamViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path('exams/<int:exam_id>/questions/', views.QuestionListByExam.as_view()),
    path('defensive_driving_questions/', views.DefensiveDrivingQuestionList.as_view()),
    path('distracted_questions/', views.DistractedQuestionList.as_view()),
]
