from django import forms
from .models import Cargo,Departamento

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre_cargo', 'estado', 'departamento']