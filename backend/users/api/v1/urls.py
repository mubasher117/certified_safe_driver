from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from home.api.v1.urls import router
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from users.api.v1 import views, viewsets

router = DefaultRouter()
# router.register("signup", viewsets.SignupViewSet, basename="signup")
# router.register("login", viewsets.LoginViewSet, basename="login")
# router.register("user-groups", UserGroupViewSet, basename="user-groups")

urlpatterns = [
    path("", include(router.urls)),
    path('admin/login/token/', views.AdminTokenObtainPairView.as_view(), name='admin_token_obtain_pair'),
    path('admin/login/token/refresh/', TokenRefreshView.as_view(), name='admin_token_refresh'),
    path('admin/login/token/verify/', TokenVerifyView.as_view(), name='admin_token_verify'),
    path('student/login/token/', views.StudentTokenObtainPairView.as_view(), name='student_token_obtain_pair'),
    path('student/login/token/refresh/', TokenRefreshView.as_view(), name='student_token_refresh'),
    path('student/login/token/verify/', TokenVerifyView.as_view(), name='student_token_verify'),
    path('user-groups/', views.UserGroupList.as_view()),
    path('user-permissions/', views.PermissionList.as_view()),
    path('account/profile/', views.LoggdeUserDetail.as_view(), name='logged_user_profile'),
    path('account/change-password/', views.ChangeUserPassword.as_view(), name='change_account_password'),
    path('user/add/', views.AddNewAdminUser.as_view(), name="add_admin_user"),
    path('user/instructor/register/', views.InstructorRegister.as_view(), name="add_instructor"),
    path('users/', views.AdminUserList.as_view(), name="admin_user_list"),
    path('users/<int:pk>/', views.AdminUserDetail.as_view(), name="admin_user_detail"),

]
