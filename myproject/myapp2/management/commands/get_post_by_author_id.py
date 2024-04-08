# Использование QuerySet для получения данных из базы данных
# Для получения данных из базы данных мы можем использовать QuerySet,
# который позволяет выполнить различные операции над набором объектов модели.

from django.core.management.base import BaseCommand
from myapp2.models import Author, Post
class Command(BaseCommand):
    help = "Get all posts by author id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')

        posts = Post.objects.filter(author__pk=pk)
        intro = f'All posts\n'
        text = '\n'.join(post.get_summary() for post in posts)
        self.stdout.write(f'{intro}{text}')
# Если нам не нужно имя автора в строке intro, можем изменить запрос к базе данных.
# Фильтруем посты по автору непосредственно из модели пост: