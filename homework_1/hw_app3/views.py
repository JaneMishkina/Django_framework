
from django.utils import timezone
from .models import Client, Product, Order
from django.shortcuts import render, get_object_or_404
import logging
from datetime import timedelta


logger = logging.getLogger(__name__)

def index(request):
    logger.info(f'Посещение страницы {__name__}: index')
    return render(request, 'hw_app3/index.html')


def about(request):
    logger.info(f'Посещение страницы {__name__}: about')
    return render(request, 'hw_app3/about.html')

def client_orders_view(request, client_id):
    client = Client.objects.get(id=client_id)
    orders_last_7_days = Order.objects.filter(client=client, order_date__gt=timezone.now() - timedelta(days=7))
    orders_last_30_days = Order.objects.filter(client=client, order_date__gt=timezone.now() - timedelta(days=30))
    orders_last_365_days = Order.objects.filter(client=client, order_date__gt=timezone.now() - timedelta(days=365))

    products_last_7_days = set()
    products_last_30_days = set()
    products_last_365_days = set()

    for order in orders_last_7_days:
        for product in order.products.all():
            products_last_7_days.add(product)

    for order in orders_last_30_days:
        for product in order.products.all():
            products_last_30_days.add(product)

    for order in orders_last_365_days:
        for product in order.products.all():
            products_last_365_days.add(product)

    return render(request, 'hw_app3/client_orders_view.html', {
        'products_last_7_days': products_last_7_days,
        'products_last_30_days': products_last_30_days,
        'products_last_365_days': products_last_365_days
    })

