from django.urls import path
from .views import home, admin_panel

urlpatterns = [
    path("", home, name="home"),
    path("webadmin", admin_panel, name="webadmin/"),
]
