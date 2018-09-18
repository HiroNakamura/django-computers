from django.contrib import admin
from .models import Departamento
from .models import Computadora
from .models import Question
from .models import Choice


admin.site.register(Departamento)
admin.site.register(Computadora)
admin.site.register(Question)
admin.site.register(Choice)
