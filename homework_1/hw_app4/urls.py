
from django.urls import path
from . import views
from .views import upload_image

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('client/<int:client_id>/orders/', views.client_orders_view, name='client_orders_view'),
    path('upload/', upload_image, name='upload_image'),
]