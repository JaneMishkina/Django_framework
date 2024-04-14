
from decimal import Decimal
from datetime import timedelta
from random import randint, uniform, choice

from django.utils.timezone import now
from django.core.management.base import BaseCommand

from hw_app4.models import Client, Product, Order

class DBDataError(Exception):
    pass

class Command(BaseCommand):
    help = 'Fill the database with sample data for clients, products, and orders.'

    def add_arguments(self, parser):
        parser.add_argument('clients_qty', type=int, help='Number of clients to create')
        parser.add_argument('products_qty', type=int, help='Number of products to create')
        parser.add_argument('orders_qty', type=int, help='Number of orders to create')

    def handle(self, *args, **options):
        clients_qty = options.get('clients_qty')
        products_qty = options.get('products_qty')
        orders_qty = options.get('orders_qty')

        # Start counters to avoid duplicates
        clients_start_counter = len(Client.objects.all())
        products_start_counter = len(Product.objects.all())
        orders_start_counter = len(Order.objects.all())

        # Create clients
        for i in range(clients_start_counter + 1, clients_start_counter + clients_qty + 1):
            client = Client(
                name=f'Client_{i}',
                email=f'client_{i}@example.com',
                phone_number=f"+7{''.join([str(randint(0, 9)) for _ in range(10)])}",
                address=f'city{i} street {i}',
            )
            client.save()

        # Create products
        for i in range(products_start_counter + 1, products_start_counter + products_qty + 1):
            product = Product(
                name=f'Product_{i}',
                price=round(uniform(1, 1000), 2),
                quantity=randint(1, 100),
                description=f'description_{i}',
            )
            product.save()

        # Create orders
        clients = Client.objects.all()
        if len(clients) == 0:
            raise DBDataError('No clients in the database')
        products = Product.objects.all()
        if len(products) == 0:
            raise DBDataError('No products in the database')

        for i in range(orders_start_counter + 1, orders_start_counter + orders_qty + 1):
            order = Order(
                client=choice(clients),
                total_amount=0,
                order_date=now() - timedelta(days=randint(1, 200)),
            )
            order.save()

            # Add products to the order and calculate total amount
            products_to_order = [choice(products) for _ in range(randint(1, 5))]
            order.products.set(products_to_order)
            total_price = sum([Decimal(product.price) for product in order.products.all()])
            order.total_amount = total_price
            order.save()

        self.stdout.write(f'Database filled with clients: {clients_qty}, products: {products_qty}, orders: {orders_qty}')
