from django import forms
from .models import Equipo
from .models import Departamento


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('area','responsable')

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ('bien','arrendado','asignado','ip' ,'dns' ,'red'  ,'operativo' ,'tipo' ,'maquina' , 'dominio' ,'modelo' ,'administrador' ,'ubicacion' ,'actualizada' ,'departamento',)
     