# Получение объектов модели из базы данных, read
# Для получения объектов модели из базы данных можно использовать методы "all()" и "get()" класса модели.
from django.core.management.base import BaseCommand
from myapp2.models import User
class Command(BaseCommand):
    help = "Get all users."
    def handle(self, *args, **kwargs):
        users = User.objects.all()
        self.stdout.write(f'{users}')