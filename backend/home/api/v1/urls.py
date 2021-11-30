from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.views import base64_to_image, db_url
from home.api.v1.viewsets import (
    HomePageViewSet,
    CustomTextViewSet,
)
from users.api.v1.urls import router as user_router

router = DefaultRouter()
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)

# router += user_router

urlpatterns = [
    path("", include(router.urls)),
    path("test/base64/", base64_to_image),
    # path('db/', db_url, )

]
