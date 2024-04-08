# Создаём класс Command как дочерний для BaseCommand. Переменная help выведет справку по работе команды.
# А метод handle отработает при вызове команды в консоли.
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    help = "Print 'Hello world!' to output."
    def handle(self, *args, **kwargs):
        self.stdout.write('Hello world!')

# Вместо привычного print необходимо использовать self.stdout.write для печати информации в стандартный поток вывода -
# консоль.
# Файл my_command.py можно запускать из терминала командой
# python manage.py my_comand
