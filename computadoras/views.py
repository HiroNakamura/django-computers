from django.shortcuts import render , get_object_or_404,redirect 
from .models import Departamento
from .models import Equipo
from .models import Usuario
from django.views.defaults import page_not_found
from django.conf import settings
from .forms import EquipoForm
from .forms import UsuarioForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.db import connection




def pag_error_404(request):
    #context={}
    context={"project_name":settings.PROJECT_NAME}
    #return render(request,'computadoras/404.html',context)
    return page_not_found(request, 'computadoras/static/404.html',context)

#http://localhost:8000
def home(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT count(*) FROM computadoras_equipo WHERE computadoras_equipo.bien LIKE '%MXL4332%' ''') 
    arrendadas = cursor.fetchone()
    cursor.execute('''SELECT count(*) FROM computadoras_equipo WHERE computadoras_equipo.bien NOT LIKE '%MXL4332%' ''') 
    propias = cursor.fetchone()
    comps = Equipo.objects.all()
    cantidad = len(comps)
    return render(request, 'computadoras/home.html',{'comps':comps,'cantidad':cantidad,'arrendadas':arrendadas,'propias':propias})

#http://localhost:8000/departamentos
def dept_list(request):
    deptos = Departamento.objects.all()
    return render(request, 'computadoras/dept_list.html', {'deptos':deptos})

def usuarios_list(request):
    users = Usuario.objects.all()
    cantidad = len(users)
    return render(request, 'computadoras/usuarios_list.html', {'users':users,'cantidad':cantidad})


def usuario_detalle(request, pk):
    user = get_object_or_404(Usuario, pk=pk)
    #comp = Equipo.objects.get(pk=pk)
    print "Usuario: ", user.usuario
    return render(request, 'computadoras/usuario/usuario_detalle.html', {'user': user})

def usuario_nuevo(request):
    form = UsuarioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'computadoras/usuarios_list.html', {'form': form})
            #return HttpResponseRedirect("computadoras/nueva/")
    return render(request, 'computadoras/form_usuario.html', {'form': form})


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