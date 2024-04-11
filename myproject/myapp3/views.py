from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Author, Post


# Представления на основе функций

# Функциональное представление — это функция Python, которая принимает объект
# запроса и возвращает объект ответа. Она может быть определена как обычная
# функция или декоратор. Пример функционального представления:

def hello(request):
    return HttpResponse("Hello World from function!")

# Представления на основе классов

# Классовое представление – это класс Python, который наследуется от базового
# класса View и реализует один или несколько методов для обработки запросов.
# Пример классового представления:
class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")


def year_post(request, year):
    text = ""
    ...  # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ...  # формируем статьи за год и месяц
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")


def post_detail(request, year, month, slug):
    ...  # Формируем статьи за год и месяц по идентификатору.
    # Пока обойдёмся без запросов к базе данных
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумался над тем, "
                   "какой способ создания списков в Python работает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})

# Передача контекста в шаблон
def my_view(request):

    context = {"name": "John"}
    return render(request, "myapp3/my_template.html", context)

# В этом примере мы создали функцию my_view, которая использует шаблон my_template.html из приложения myapp3.
# Функция передает шаблону параметр name со значением "John". Функция render заменяет переменные в шаблоне на
# значения из контекста и возвращает готовую HTML-страницу.

# Рассмотрим ещё одну вариацию представления.
class TemplIf(TemplateView):
    template_name = "myapp3/templ_if.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context
# В данном примере мы создаем класс TemplIf, который наследуется от TemplateView и указывает на использование шаблона
# myapp3/templ_if.html. В методе get_context_data мы добавляем две переменные в словарь context - message и number.
# В шаблоне мы используем эти переменные в условных операторах. Если переменная message не пуста, будет выведено
# сообщение. В зависимости от значения переменной number будет выбрано соответствующее окончание предложения.

def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp3/templ_for.html', context)

# В данном примере мы создаем функцию view_for, которая передает список my_list и словарь my_dict в контекст шаблона
# и вызывает рендеринг шаблона myapp3/templ_for.html.
# В шаблоне мы можем использовать тег for для вывода элементов списка

def index(request):
    return render(request, 'myapp3/index.html')


def about(request):
    return render(request, 'myapp3/about.html')

# Создадим “вьюшку” для получения 5 последних статей автора:
def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp3/author_posts.html', {'author': author, 'posts': posts})
# Новая функция get_object_or_404 работает аналогично get, т.е. делает select запрос к базе данных. Но если запрос не
# вернёт строку из таблицы БД, представление отрисует страницу с ошибкой 404.
# Метод order_by('-id'): после фильтрации статей по автору, мы сортируем их на основе id по убыванию.  Об этом говорит
# знак минус перед именем. Далее питоновский срез формирует список из пяти статей с максимальными идентификаторами.
# Словарь с контекстом в виде автора и списка статей пробрасываются в шаблон myapp3/author_posts.html.

# Второе представление должно возвращать шаблон с полным текстом статьи:
def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_full.html', {'post': post})
# Сделав select запрос к таблице с постами мы передаём в шаблон myapp3/post_full.html контекст в виде одной статьи.