from django import forms
from django.forms import ModelForm
from .models import Customer, Order, ProductOrder, Product


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price')
        labels = {
            'name': '',
            'price': '',
        }

        help_texts = {
            'name': None,
            'price': None,
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Įveskite produkto pavadinimą'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Įveskite produkto kainą už vnt/kg'}),
        }




class AddProductOrderForm(ModelForm):
    class Meta:
        model = ProductOrder
        fields = ('order_id', 'product_id', 'quantity')




