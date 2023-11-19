from django.apps import AppConfig


class Polls1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls1'

from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'polls1'

    def ready(self):
        import polls1.signals