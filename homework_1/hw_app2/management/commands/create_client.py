
from django.core.management.base import BaseCommand
from hw_app2.models import Client


class Command(BaseCommand):
    help = "Create new client."

    def handle(self, *args, **kwargs):
        client = Client(name='John', email='john@example.com', phone_number='79115214545', address='Moscow')
        client = Client(name='Mary', email='mary@example.com', phone_number='79115245785', address='Tula')
        client.save()
        self.stdout.write(f'{client}')
