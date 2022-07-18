
from pyexpat import model
from django import forms
from .models import Emp,Account

class EmpForm1(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'


class EmpForm2(forms.ModelForm):
    class Meta:
        model=Emp
        fields=['name', 'contact','description']

class AccForm(forms.ModelForm):
    class Meta:
        model=Account
        fields='__all__'