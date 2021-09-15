from django.forms import widgets
from .models import LaptopModel
from django import forms



class LaptopForm(forms.ModelForm):
    class Meta:
        model=LaptopModel
        fields='__all__'

        labels={
            'laptopname':'Laptop Name',
            'laptopCompany':'Laptop Company',
            'laptopram':'Laptop RAM (Gb)',
            'laptoprom':'Laptop ROM (Gb)',
            'laptopprice':'Laptop Price (Rs)',
            'laptopprocessor':'Laptop Processor',
        }

        widgets={
            'laptopname':forms.TextInput(attrs={'placeholder':'Enter Laptop Name....'}),
            'laptopCompany':forms.TextInput(attrs={'placeholder':'Enter Laptop Company....'}),
            'laptopram':forms.TextInput(attrs={'placeholder':'Enter Laptop RAM....'}),
            'laptoprom':forms.TextInput(attrs={'placeholder':'Enter Laptop ROM....'}),
            'laptopprice':forms.TextInput(attrs={'placeholder':'Enter Laptop Price....'}),
            'laptopprocessor':forms.TextInput(attrs={'placeholder':'Enter Laptop Processor....'}),

        }