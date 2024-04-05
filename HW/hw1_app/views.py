
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Здесь вы найдете много интересной информации о разработке веб-приложений.</p>
    """

    # Сохраняем данные в логи
    logging.info('Посещение страницы "главная"')

    return HttpResponse(html)


def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Привет! Я начинающий веб-разработчик, учусь создавать сайты с помощью Django и других технологий.</p>
    <p>На этом сайте я делюсь своим опытом и знаниями, которые набрал за время изучения программирования.</p>
    """

    # Сохраняем данные в логи
    logging.info('Посещение страницы "о себе"')

    return HttpResponse(html)

