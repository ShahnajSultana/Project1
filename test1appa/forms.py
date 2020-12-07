from .models import Product
from django import forms

class ProductForm (forms.ModelForm):
    
    class Meta:
        model = Product
        #fields = '__all__'
        fields=['name','price']

        widgets = {
            
            'name':forms.TextInput(attrs={'class':'form-control bg-light'}),
            'price':forms.TextInput(attrs={'class':'from-control bg-light'})
        }
