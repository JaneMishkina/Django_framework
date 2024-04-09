from django.core.management.base import BaseCommand
from hw_app2.models import Client, Product, Order

class Command(BaseCommand):
    help = "Create new order."

    def handle(self, *args, **kwargs):
        client = Client.objects.get(name='Mary')  # Получаем клиента Mary (здесь можно использовать любой другой способ получения клиента)
        products = Product.objects.filter(name__icontains='iPhone')  # Получаем продукты с названием содержащим 'iPhone' (здесь можно использовать любой другой метод фильтрации)
        total_amount = sum(product.price for product in products)  # Вычисляем общую стоимость заказа

        order = Order(client=client, total_amount=total_amount)
        order.save()
        order.products.set(products)

        self.stdout.write(f'New order created: {order}')
