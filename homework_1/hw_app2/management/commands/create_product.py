from django.core.management.base import BaseCommand
from hw_app2.models import Product

class Command(BaseCommand):
    help = "Create new product."

    def handle(self, *args, **kwargs):
        product = Product(name='iPhone 12', description='Latest iPhone model', price=999.99, quantity=100)
        # product = Product(name='Xaomi 10', description='Latest Xaomi model', price=889.99, quantity=80)
        product.save()
        self.stdout.write(f'{product}')
