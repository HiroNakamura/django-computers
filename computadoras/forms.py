from django import forms
from .models import Computadora


class ComputadoraForm(forms.ModelForm):
    class Meta:
        model = Computadora
        fields = ('bien','arrendado','asignado','ip' ,'dns' ,'red'  ,'operativo' ,'tipo' ,'maquina' , 'dominio' ,'modelo' ,'administrador' ,'ubicacion' ,'actualizada' ,'departamento',)
     