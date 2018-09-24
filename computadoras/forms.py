from django import forms
from .models import Equipo
from .models import Departamento
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields =['nombre','apellidos','usuario','password','cargo','computadora',]

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['area','responsable',]

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['bien','arrendado','asignado','ip' ,'dns' ,'red'  ,'operativo' ,'tipo' ,'maquina' , 'dominio' ,'modelo' ,'administrador' ,'ubicacion' ,'actualizada' ,'departamento',]
     