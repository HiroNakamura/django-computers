from django.contrib import admin
from .models import Departamento
from .models import Equipo
from .models import Usuario

class AdminDepartamento(admin.ModelAdmin):
  list_display = []
  class Meta:
    model = Departamento

class AdminEquipo(admin.ModelAdmin):
  list_display = []
  class Meta:
    model = Equipo
    
class AdminUsuario(admin.ModelAdmin):
  list_display = []
  class Meta:
    model = Usuario
    
    
admin.site.register(Departamento,AdminDepartamento)
admin.site.register(Equipo,AdminEquipo)
admin.site.register(Usuario,AdminUsuario)
