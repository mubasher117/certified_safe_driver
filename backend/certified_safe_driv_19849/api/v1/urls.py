from django.urls import path, include

app_name = 'api_v1'
urlpatterns = [
    path("rest-auth/", include("rest_auth.urls")),
    # Override email confirm to use allauth's HTML view instead of rest_auth's API view
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
    path("", include("home.api.v1.urls")),
    path("", include("users.api.v1.urls")),
    path("quizes/", include("csd_quizes.api.v1.urls")),
    path("", include("safe_driver.api.v1.urls", namespace="api_v1:safe_driver")),
    path("truck-driving-school/", include("truck_driving_school.api.v1.api_urls", namespace="api_v1:truck_driving_school")),
]
