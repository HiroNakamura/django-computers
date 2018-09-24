from django.contrib import admin
from .models import Departamento
from .models import Equipo
from .models import Usuario

admin.site.register(Departamento)
admin.site.register(Equipo)
admin.site.register(Usuario)