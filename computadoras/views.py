from django.shortcuts import render
from .models import Departamento

def dept_list(request):
    deptos = Departamento.objects.all()
    return render(request, 'computadoras/dept_list.html', {'deptos':deptos})