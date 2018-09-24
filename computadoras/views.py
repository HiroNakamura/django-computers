from django.shortcuts import render , get_object_or_404,redirect 
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
    comps = Equipo.objects.all()
    return render(request, 'computadoras/home.html',{'comps':comps})

#http://localhost:8000/departamentos
def dept_list(request):
    deptos = Departamento.objects.all()
    return render(request, 'computadoras/dept_list.html', {'deptos':deptos})


def comp_detalle(request, pk):
    comp = get_object_or_404(Equipo, pk=pk)
    #comp = Equipo.objects.get(pk=pk)
    print "Computadora: ", comp.bien
    return render(request, 'computadoras/comp_detalle.html', {'comp': comp})


def comp_nueva(request):
    form = EquipoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'computadoras/form_comp.html', {'form': form})
            #return HttpResponseRedirect("computadoras/nueva/")
    return render(request, 'computadoras/form_comp.html', {'form': form})