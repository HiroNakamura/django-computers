from django.shortcuts import render , get_object_or_404
from .models import Departamento
from .models import Equipo
from django.views.defaults import page_not_found
from django.conf import settings
from .forms import EquipoForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, HttpResponseRedirect

def pag_error_404(request):
    context={}
    context={"project_name":settings.PROJECT_NAME}
    return render(request,'computadoras/404.html',context)
    #return page_not_found(request, '404.html',{})

#http://localhost:8000
def home(request):
    return render(request, 'computadoras/home.html',{})

#http://localhost:8000/departamentos
def dept_list(request):
    deptos = Departamento.objects.all()
    return render(request, 'computadoras/dept_list.html', {'deptos':deptos})


#http://localhost:8000/computadoras
def comp_list(request):
    comps = Equipo.objects.all()
    return render(request, 'computadoras/comp_list.html', {'comps':comps})

