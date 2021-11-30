from django.urls import path
from .views import *

urlpatterns = [
    path('report/student-prod/<int:student_id>/preview/', StudentProdReportPreview.as_view()),
    path('report/student-prod/<int:student_id>/download/', prod_report_download),
    path('students/<int:student_id>/tests/<int:test_id>/btw/<slug:class_name>/accident_probability_grap/',
         accident_probability_graph_btw_class_a),
]
