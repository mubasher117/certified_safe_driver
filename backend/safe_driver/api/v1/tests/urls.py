from django.urls import path, include

from ..views import (StudentTestPASDetail, StudentEyeDetailByStudentID, StudentEquipList, StudentEquipDetail,
                     StudentVRTDetail,
                     StudentProdDetail, ProdItemListCreate)
from .views import *

urlpatterns = [
    path('', StudentTestListAPIView.as_view(), name='student_test_list'),
    path('<int:test_id>/', StudentTestDetailAPIView.as_view(), name='student_test_detail'),
    path('<int:test_id>/tdc/', include('truck_driving_school.api.v1.urls')),
    path('<int:test_id>/info/', StudentTestInfoDetailAPIView.as_view()),
    path('<int:test_id>/notes/', TestNotes.as_view()),
    path('<int:test_id>/notes/<int:note_id>/', TestNoteDetail.as_view()),
    path('<int:test_id>/pretrips/', include('safe_driver.api.v1.pretrip.urls')),
    path('<int:test_id>/btw/', include('safe_driver.api.v1.btw.urls')),
    path('<int:test_id>/pas/', StudentTestPASDetail.as_view()),
    path('<int:test_id>/swp/', StudentTestSWPDetail.as_view()),
    path('<int:test_id>/swp/injury_probability_graph/', swp_injury_probability_graph),
    path('<int:test_id>/eye/', StudentEyeDetailByStudentID.as_view()),
    path('<int:test_id>/equips/', StudentEquipList.as_view()),
    path('<int:test_id>/equips/<int:equip_id>/', StudentEquipDetail.as_view()),
    path('<int:test_id>/prod/', StudentProdDetail.as_view()),
    path('<int:test_id>/prod/items/', ProdItemListCreate.as_view()),
    path('<int:test_id>/vrt/', StudentVRTDetail.as_view()),
    path('<int:test_id>/', include('csd_quizes.api.v1.test_quiz_urls')),
]
