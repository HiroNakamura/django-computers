from django.shortcuts import render
from .models import Departamento
from .models import Computadora

def dept_list(request):
    deptos = Departamento.objects.all()
    return render(request, 'computadoras/dept_list.html', {'deptos':deptos})

def comp_list(request):
    comps = Computadora.objects.all()
    return render(request, 'computadoras/comp_list.html', {'comps':comps})