from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SafeDriverConfig(AppConfig):
    name = 'safe_driver'
    verbose_name = _("Safe Driver")

    def ready(self):
        try:
            import safe_driver.signals  # noqa F401
        except ImportError:
            pass
