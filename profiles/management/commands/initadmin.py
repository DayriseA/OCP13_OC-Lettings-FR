import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create a superuser if no users exist"

    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.exists():
            self.stdout.write("Not first run. Superuser creation skipped.")
        else:
            password = os.environ.get("INIT_SUPERUSER_PASS")
            if password:
                User.objects.create_superuser(username="ocladmin", password=password)
                self.stdout.write(
                    "Superuser 'ocladmin' created successfully.\n"
                    "Think about removing the INIT_SUPERUSER_PASS environment variable"
                )
            else:
                self.stdout.write("INIT_SUPERUSER_PASS missing. Superuser not created.")
