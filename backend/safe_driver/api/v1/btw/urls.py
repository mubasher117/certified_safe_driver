from django.urls import path

from .views import *

urlpatterns = [
    path('', BTWClassList.as_view(), name='btw_class_list'),
    path('class_a/', BTWClassADetailView.as_view(), name='student_btw_class_a_detail'),
    path('class_a/accident_probability_graph/', BTWClassAFactors.as_view(), name='student_btw_class_a_factors'),
    # path('class_a/instructions/', btw_class_a_instructions, name='student_btw_class_a_instructions'),
    path('class_b/', BTWClassBDetailView.as_view(), name='student_btw_class_b_detail'),
    path('class_b/accident_probability_graph/', BTWClassBFactors.as_view(), name='student_btw_class_b_factors'),
    path('class_c/', BTWClassCDetailView.as_view(), name='student_btw_class_c_detail'),
    path('class_c/accident_probability_graph/', BTWClassCFactors.as_view(), name='student_btw_class_c_factors'),
    path('class_p/', BTWClassPDetailView.as_view(), name='student_btw_class_p_detail'),
    path('class_p/accident_probability_graph/', BTWClassPFactors.as_view(), name='student_btw_class_p_factors'),
    path('bus/', BTWBusDetailView.as_view(), name='student_btw_bus_detail'),
    path('bus/accident_probability_graph/', BTWBusFactors.as_view(), name='student_btw_bus_factors'),
]
