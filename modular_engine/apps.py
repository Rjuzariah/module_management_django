from django.apps import AppConfig
from django.db.migrations.recorder import MigrationRecorder
from django.db import connection


class ModularEngineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modular_engine'
