from django.urls import path, include
from .views import *

urlpatterns = [
    path('defense-quiz/', DefensiveDriverKnowledgeQuizDetail.as_view(), ),
    path('training-records/', DriverTrainigRecordListView.as_view()),
    path('training-records/comments/', TrainingDayCommentList.as_view()),
    path('training-records/<int:pk>/', DriverTrainingRecordDetails.as_view()),
    path('training-records/<int:pk>/comment/', DriverTrainingRecordCommentDetails.as_view()),
    path('training-records-add-day/', DriverTrainingRecordAddNewDay.as_view()),
    path('training-records-delete/', DeleteDriverTrainingRecord.as_view()),
    path('school-hours/', SchoolHoursDetails.as_view()),
    path('dqf-requirements-items/', DQFRequirementListView.as_view()),
    path('dqf-requirements/', SchoolControlDQFRequirementListView.as_view()),
    path('dqf-requirements/<int:pk>/', SchoolControlDQFRequirementDetails.as_view()),

    path('trainee-book-items/', TraineeBookItemListView.as_view()),
    path('trainee-book/', TraineeBookListView.as_view()),
    path('trainee-book/<int:pk>/', TraineeBookDetails.as_view()),
]
