from django import forms
from .models import Product


class ImageForm(forms.Form):
    image = forms.ImageField()


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'name', 'description', 'price', 'quantity'
