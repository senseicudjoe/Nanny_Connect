from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _ #You need to import this and add the commented line of code below for the signals to work. 
class ClientappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientApp'

    def ready(self):
        import clientApp.signals  # noqa The Django documentation advices to put the signals inside your app config file
