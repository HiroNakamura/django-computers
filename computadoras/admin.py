from django.contrib import admin
from .models import Departamento
from .models import Equipo
from .models import Usuario

class AdminDepartamento(admin.ModelAdmin):
  list_display = ["area","responsable"]
  #list_display_links = ["responsable"]
  list_filter = ["area"]
  list_editable = ["responsable"]
  search_fields = ["area","responsable"]
  class Meta:
    model = Departamento

class AdminEquipo(admin.ModelAdmin):
  list_display = ["bien","arrendado","asignado","ip","departamento"]
  #list_display_links = ["bien"]
  list_filter = ["bien","arrendado","asignado","ip"]
  list_editable = ["asignado","ip","departamento"]
  search_fields = ["bien","arrendado","asignado","ip","actualizada"]
  class Meta:
    model = Equipo
    
class AdminUsuario(admin.ModelAdmin):
  list_display = ["usuario","nombre","apellidos","cargo"]
  #list_display_links = ["cargo"]
  list_filter = ["usuario","nombre","apellidos","cargo"]
  list_editable = ["usuario","nombre","apellidos","cargo"]
  search_fields = ["usuario","nombre","apellidos","cargo","computadora"]
  class Meta:
    model = Usuario
    
    
admin.site.register(Departamento,AdminDepartamento)
admin.site.register(Equipo,AdminEquipo)
admin.site.register(Usuario,AdminUsuario)
