from django import forms
from ProfileApp.models import *

screen_choice = [('Nomal','Nomal'),('LCD','LCD')]
size_choice = [('6 Inch','6 Inch'),('7 Inch','7 Inch'),('8 Inch','8 Inch'),('9 Inch','9 Inch'),('10 Inch','10 Inch')]
pressure_choice = [('1024','1024'),('2048','2048'),('4096','4096'),('8192','8192')]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('id','brand','model','screen','size','pressure','weight','price','amount')
        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control'}),
            'brand': forms.TextInput(attrs={'class':'form-control'}),
            'model': forms.TextInput(attrs={'class':'form-control'}),
            'screen': forms.RadioSelect(attrs={'class':'form-inline'}, choices=screen_choice),
            'size': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=size_choice),
            'pressure': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=pressure_choice),
            'weight': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control'})
        }
        labels = {
            'id':'ID',
            'brand': 'Brand',
            'model': 'Model',
            'screen': 'Screen',
            'size': 'Size',
            'pressure': 'Pressure',
            'weight': 'Weight',
            'price': 'Price',
            'amount': 'Amount'
        }