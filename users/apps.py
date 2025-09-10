from django.apps import AppConfig
from django.db.models.signals import post_migrate

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from django.contrib.auth.models import Group

        def create_user_groups(sender, **kwargs):
            Group.objects.get_or_create(name='Seller')
            Group.objects.get_or_create(name='Buyer')

        post_migrate.connect(create_user_groups, sender=self)
