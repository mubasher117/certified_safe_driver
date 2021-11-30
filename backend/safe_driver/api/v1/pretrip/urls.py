from django.urls import path, include

from .views import *

urlpatterns = [
    path('class_a/', PreTripClassADetailView.as_view(), name='student_pretrip_class_a_detail'),
    # path('class_a/test/', TestPretripClassView.as_view(), ),
    path('class_a/accident_probability_graph/', PreTripClassAProbabilityGraph.as_view(),
         name='student_pretrip_class_a_probability_graph'),
    path('class_b/', PreTripClassBDetailView.as_view(), name='student_pretrip_class_b_detail'),
    path('class_b/accident_probability_graph/', PreTripClassBProbabilityGraph.as_view(),
         name='student_pretrip_class_b_probability_graph'),
    path('class_c/', PreTripClassCDetailView.as_view(), name='student_pretrip_class_c_detail'),
    path('class_c/accident_probability_graph/', PreTripClassCProbabilityGraph.as_view(),
         name='student_pretrip_class_c_probability_graph'),
    path('class_p/', PreTripClassPDetailView.as_view(), name='student_pretrip_class_p_detail'),
    path('class_p/with_instructions/', PreTripClassPDetailViewWithInsructions.as_view(),),
    path('class_p/accident_probability_graph/', PreTripClassPProbabilityGraph.as_view(),
         name='student_pretrip_class_p_probability_graph'),
    path('bus/', PreTripBusDetailView.as_view(), name='student_pretrip_bus_detail'),
    path('bus/accident_probability_graph/', PreTripBusProbabilityGraph.as_view(),
         name='student_pretrip_bus_probability_graph'),
]
