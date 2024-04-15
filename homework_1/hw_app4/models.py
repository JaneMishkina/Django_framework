from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

    def str(self):
        return (f'Clientname: {self.name}, email: {self.email}, phone_number: {self.phone_number}, '
                f'address: {self.address}, registration_date: {self.registration_date}')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    added_date = models.DateField(auto_now_add=True)
    # photo = models.ImageField(upload_to='product_photos/')

    def str(self):
        return (f'Product: {self.name}, description: {self.description}, price: {self.price}, '
                f'quantity: {self.quantity}, added_date: {self.added_date}')


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()

    def str(self):
        return (f'Order: {self.client}, products: {self.products}, total_amount: {self.total_amount}, '
                f'order_date: {self.order_date}')