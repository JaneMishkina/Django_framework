# Создание объектов модели, create
from django.core.management.base import BaseCommand
from myapp2.models import User
class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        user = User(name='John', email='john@example.com', password='secret', age=25)
        user = User(name='Neo', email='neo@example.com', password='secret', age=58)
        user.save()
        self.stdout.write(f'{user}')

# Здесь мы создаем новый объект модели "User" с заданными значениями полей и сохраняем его в базе данных с помощью
# метода "save()". Далее выводим на печать сохранённого пользователя.
# Если заглянуть в базу данных, таблица myapp2_user получит новую запись.