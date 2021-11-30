from django.urls import path, include
from rest_framework.routers import DefaultRouter
from safe_driver.api.v1 import views, viewsets
from safe_driver.api.v1.report.views import (StudentReportDetail)

router = DefaultRouter()

router.register('student-groups', viewsets.StudentGroupViewSet, basename='student_groups')
router.register('equips', viewsets.SafeDriveEquipmentViewSet, basename='equips')
router.register('companies', viewsets.CompaniesViewSet, basename='companies')
router.register('student-tests', viewsets.StudentTestViewSet, basename='student_tests')
# router.register('prods', viewsets.SafeDriveProdViewSet, basename='prods')
# router.register('pre-trips', viewsets.SafeDrivePreTripViewSet, basename='pre_trips')
# router.register('eyes', viewsets.SafeDriveEyeViewSet, basename='eyes')
# router.register('btws', viewsets.SafeDriveBTWViewSet, basename='btws')
# router.register('pas-list', viewsets.SafeDrivePASViewSet, basename='pas_list')
# router.register('swp-list', viewsets.SafeDriveSWPViewSet, basename='swp_list')

app_name = "safe_driver"

urlpatterns = [
    path('', include(router.urls)),
    path('charts/', include('safe_driver.api.v1.chart_urls')),
    path('instructions/', include('safe_driver.api.v1.instructions.urls')),
    # instructor
    path('instructors/', views.InstructorList.as_view(), name='instructor_list'),
    path('instructors/<int:user_id>/profile/', views.InstructorProfileDetail.as_view(), name='instructor_profile'),
    # path('companies/', views.CompaniesListView.as_view(), name='company_list'),
    path('students/register/', views.NewStudentRegister.as_view(), name='student_register'),
    path('students/<int:student_id>/', views.StudentDetailAPIView.as_view(), name='student_detail'),
    path('students/<int:student_id>/tests/', include('safe_driver.api.v1.tests.urls'),),

    ##
    # path('students/<int:student_id>/info/', views.StudentInfoDetail.as_view(), name='student_info'),

    # path('students/<int:student_id>/eye/', views.StudentEyeDetailByStudentID.as_view()),
    # path('students/<int:student_id>/notes/', views.StudentNoteListByStudentID.as_view()),
    # path('students/<int:student_id>/notes/<int:pk>/', views.StudentNoteDetail.as_view()),
    # path('students/<int:student_id>/equip/', views.StudentEquipDetail.as_view()),
    # path('students/<int:student_id>/prod/', views.StudentProdDetail.as_view(), name='student_prod'),
    # path('students/<int:student_id>/pre-trip/', views.StudentPreTripDetail.as_view(), name='student_pre_trips'),
    # path('students/<int:student_id>/btw/', views.StudentBTWDetail.as_view(), name='student_btw_detail'),
    # path('students/<int:student_id>/vrt/', views.StudentVRTDetail.as_view(), name='student_vrt_detail'),
    # path('students/<int:student_id>/pas/', views.StudentPASDetail.as_view(), name='student_pas_detail'),
    # path('students/<int:student_id>/swp/', views.StudentSWPDetail.as_view(), name='student_swp_detail'),
    path('students/<int:student_id>/report/', StudentReportDetail.as_view(), name='student_report_detail'),
    path('students/', views.StudentListAPIView.as_view(), name='student_list'),
    # path('student-notes/<int:student_id>/', views.StudentNoteDetail.as_view(), name='student_note_detail'),
    # path('student-prods/<int:student_id>/', views.StudentProdDetail.as_view(), name='student_prod_detail'),
    # path('student/info/create/', views.StudentInfoCreate.as_view()),
    path('download/generate/sample_factor_csv/', views.SampleFactorCSVDownload.as_view(),
         name='download_sample_factor_csv'),
    path('download/generate/instructions_csv/', views.InstructionSampleCSVDownload.as_view(),
         name='download_instruction_sample_csv'),
]
