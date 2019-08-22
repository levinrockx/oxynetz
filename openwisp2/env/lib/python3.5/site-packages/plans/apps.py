from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from . import conf as app_settings


class PlansConfig(AppConfig):
    name = 'plans'
    verbose_name = _(app_settings.APP_VERBOSE_NAME)
