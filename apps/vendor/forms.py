from django.db.models import fields
from django.forms import ModelForm, widgets
from django import forms
from apps.product.models import Product
from apps.order.models import Order, OrderItem

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'price', 'image', 'title', 'description']


        widgets = {
        'category': forms.Select(attrs={'class': 'select control label'}),
        'price': forms.NumberInput(attrs={'class': 'label input'}),
        'title': forms.TextInput(attrs={'class': 'label input'}),
        'image': forms.ClearableFileInput(attrs={'class': 'field label control'}),

        'description': forms.Textarea(attrs={'class': 'label textarea'}),
        
        
    }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'city', 'zipcode',  'phone']

        widgets = {
        'first_name': forms.TextInput(attrs={'class': 'label input'}),
        'last_name': forms.TextInput(attrs={'class': 'label input'}),
        'email': forms.TextInput(attrs={'class': 'label input'}),
        'address': forms.TextInput(attrs={'class': 'label input'}),
        'zipcode': forms.TextInput(attrs={'class': 'label input'}),
        'city': forms.TextInput(attrs={'class': 'label input'}),
        'phone': forms.TextInput(attrs={'class': 'label input'}),

    }