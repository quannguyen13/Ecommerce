from django.forms import ModelForm
from django import forms
from apps.product.models import Product

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