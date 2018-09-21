from django import forms
from .models import Equipo


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ('bien','arrendado','asignado','ip' ,'dns' ,'red'  ,'operativo' ,'tipo' ,'maquina' , 'dominio' ,'modelo' ,'administrador' ,'ubicacion' ,'actualizada' ,'departamento',)
     