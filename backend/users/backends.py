from django.conf import settings
from django.contrib.auth import get_user_model, backends
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _


User = get_user_model()


# class EmailAndMobileNumberLoginBackend(backends.AllowAllUsersModelBackend):
class UsernameEmailLoginBackend(backends.ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            user = User.objects.filter(
                Q(email=username) |
                Q(username=username)
            ).first()
        except User.DoesNotExist:
            return None

        # if settings.LOGIN_ALLOW_INACTIVE_USER is True and user.check_password(password):
        #     return user

        # if getattr(user, 'is_active', False) and user.check_password(password):
        if user and user.check_password(password):
            return user

        # if user.check_password(password):
        #     return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None




