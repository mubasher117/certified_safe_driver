from django.urls import path

from .views import *

urlpatterns = [
    path('btw/class_a/', InstructionsListBTWClassA.as_view()),
    path('btw/class_b/', InstructionsListBTWClassB.as_view()),
    path('btw/class_c/', InstructionsListBTWClassC.as_view()),
    path('btw/class_p/', InstructionsListBTWClassP.as_view()),
    path('btw/bus/', InstructionsListBTWBus.as_view()),

    # pre trips
    path('pretrips/class_a/', InstructionsListPreTripClassA.as_view()),
    path('pretrips/class_b/', InstructionsListPreTripClassB.as_view()),
    path('pretrips/class_c/', InstructionsListPreTripClassC.as_view()),
    path('pretrips/class_p/', InstructionsListPreTripClassP.as_view()),
    path('pretrips/bus/', InstructionsListPreTripBus.as_view()),

    path('swp/', InstructionsListSWP.as_view()),
    path('vrt/', InstructionsListVRT.as_view()),
]
