# Чтобы получить пользователя по его ID:
from django.core.management.base import BaseCommand
from myapp2.models import User
class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')

# Метод add_arguments позволяет парсить командную строку.
# Мы получаем значение целого типа и сохраняем его по ключу id.
# Теперь обработчик handler может получить к идентификатору доступ через ключ словаря kwargs.
# Для получения пользователя заменили метод get на filter, а далее к результату применяем метод first().
# ● Если в базе несколько записей, вернёт одна, первая из результата запроса
# ● Если запись одна, first вернёт эту единственную запись
# ● Если совпадений не найдено, вместо ошибки вернём None