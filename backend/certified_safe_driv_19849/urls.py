"""certified_safe_driv_19849 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path("", include("home.urls")),
    path("accounts/", include("allauth.urls")),
    path("safe-drive/", include("safe_driver.urls")),
    # path("api/v1/", include("users.api.v1.urls")),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("truck-driving-school/", include("truck_driving_school.urls", namespace="truck_driving_school")),
    # path("rest-auth/", include("rest_auth.urls")),
    # # Override email confirm to use allauth's HTML view instead of rest_auth's API view
    path("account/registration/account-confirm-email/<str:key>/", confirm_email),
    # path("rest-auth/registration/", include("rest_auth.registration.urls")),
    path("api/v1/", include('certified_safe_driv_19849.api.v1.urls', namespace="api_v1"))
]


admin.site.site_header = "Certified Safe Driver"
admin.site.site_title = "Certified Safe Driver Admin Portal"
admin.site.index_title = "Certified Safe Driver Admin"

# swagger
api_info = openapi.Info(
    title="Certified Safe Driver API",
    default_version="v1",
    description="API documentation for Certified Safe Driver App",
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns += [
    path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
