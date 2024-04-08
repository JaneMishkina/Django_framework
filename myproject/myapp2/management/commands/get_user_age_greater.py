# Фильтрация объектов модели

from django.core.management.base import BaseCommand
from myapp2.models import User
class Command(BaseCommand):
    help = "Get user with age greater <age>."
    def add_arguments(self, parser):
        parser.add_argument('age', type=int, help='User age')
    def handle(self, *args, **kwargs):
        age = kwargs['age']
        user = User.objects.filter(age__gt=age)
        self.stdout.write(f'{user}')
# Здесь мы используем оператор "__gt" для сравнения значения поля "age" с заданным значением.
# Помните про двойное подчеркивание перед оператором.
# Например для поиска имён начинающихся с S будет использоваться запись вида:
# name__startswith='S'