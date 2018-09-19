from django.shortcuts import render
from .models import Departamento
from .models import Computadora
from django.views.defaults import page_not_found
from django.conf import settings

 
def pag_error_404(request):
    context={}
    context={"project_name":settings.PROJECT_NAME}
    return render(request,'computadoras/404.html',context)
    #return page_not_found(request, '404.html',{})


def home(request):
    return render(request, 'computadoras/home.html',{})

def dept_list(request):
    deptos = Departamento.objects.all()
    return render(request, 'computadoras/dept_list.html', {'deptos':deptos})

def comp_list(request):
    comps = Computadora.objects.all()
    return render(request, 'computadoras/comp_list.html', {'comps':comps})