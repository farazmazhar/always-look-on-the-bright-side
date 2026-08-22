# Django requires an apps.py with the app's config class so it can find
# this package in INSTALLED_APPS.
from django.apps import AppConfig


class DemoAppConfig(AppConfig):
    name = "demo_app"
    default_auto_field = "django.db.models.AutoField"
