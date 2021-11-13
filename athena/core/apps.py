from django.apps import AppConfig
from django.db.models import Field

from athena.core.db.filters import PostgresILike


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'athena.core'

    def ready(self):
        Field.register_lookup(PostgresILike)
