# Создание модели
# Отношения между моделями в Django позволяют описывать связи между объектами разных моделей.
# Для этого используются поля моделей, такие как ForeignKey, ManyToManyField и OneToOneField.

from django.db import models
# Здесь мы создаем класс "User", который наследуется от "models.Model".
# Каждое поле имеет свой тип данных: "CharField" для строк, "EmailField" для
# электронных адресов и "IntegerField" для целых чисел.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'

# Здесь мы создаем модели для хранения информации о продуктах и заказах.
# В модели "Product" мы определяем поля для хранения названия продукта, цены, описания и изображения.
# В модели "Order" мы определяем поля для хранения информации о заказчике, списке продуктов, дате заказа и общей
# стоимости заказа.
# Обратите внимание на использование ForeignKey и ManyToManyField для определения отношений между таблицами.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
# Для использования в моделях Django поля ImageField необходимо установить дополнительный модуль Pillow.
# pip install Pillow

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'
# Создание пользовательских методов
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return f'Title is {self.title}'
    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'
# Здесь мы создаем метод "get_summary", который возвращает первые 12 слов контента поста и добавляет многоточие в конце.

# Не забываем про миграции после изменения файла models.py
# >python manage.py makemigrations