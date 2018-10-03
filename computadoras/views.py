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
    titulo = "Bienvenido al sistema"
    if request.user.is_authenticated:
        admin = str(request.user)
        admin = admin.upper()
        titulo = "Bienvenido al sistema %s" %(admin)
    context = {'comps':comps,'cantidad':cantidad,'arrendadas':arrendadas,'propias':propias,"titulo":titulo}
    return render(request, 'computadoras/home.html',context)

#http://localhost:8000/departamentos
def dept_list(request):
    deptos = Departamento.objects.all()
    cantidad = len(deptos)
    titulo = "Departamentos"
    context={'deptos':deptos,'cantidad':cantidad}
    return render(request, 'computadoras/dept_list.html', context)

def usuarios_list(request):
    users = Usuario.objects.all()
    cantidad = len(users)
    titulo = "Bienvenido al sistema"
    if request.user.is_authenticated:
        admin = str(request.user)
        admin = admin.upper()
        titulo = "Bienvenido al sistema %s" %(admin)
    context = {'users':users,'cantidad':cantidad,'titulo':titulo}
    return render(request, 'computadoras/usuarios_list.html', context)


def usuario_detalle(request, pk):
    user = get_object_or_404(Usuario, pk=pk)
    #comp = Equipo.objects.get(pk=pk)
    print "Usuario: ", user.usuario
    context = {'user': user}
    return render(request, 'computadoras/usuario/usuario_detalle.html', context)

def usuario_nuevo(request):
    form = UsuarioForm(request.POST or None)
    titulo = "Ingresar nuevo usuario"
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'computadoras/usuarios_list.html', {'form': form,'titulo':titulo})
            #return HttpResponseRedirect("computadoras/nueva/")
    return render(request, 'computadoras/form_usuario.html', {'form': form,'titulo':titulo})

def usuario_update(request, pk):
    instance = Usuario.objects.get(pk=pk)
    form = UsuarioForm(request.POST or None, instance=instance)
    titulo = "Actualizar usuario existente"
    if form.is_valid():
          form.save()
          return render(request, 'computadoras/usuarios_list.html', {'form': form,'titulo':titulo})
    return render(request, 'computadoras/form_usuario.html', {'form': form,'titulo':titulo})


def comp_detalle(request, pk):
    comp = get_object_or_404(Equipo, pk=pk)
    #comp = Equipo.objects.get(pk=pk)
    print "Computadora: ", comp.bien
    context = {'comp': comp}
    return render(request, 'computadoras/comp_detalle.html', context)


def comp_nueva(request):
    form = EquipoForm(request.POST or None)
    titulo= "Ingresar nueva computadora"
    context = {'form':form,'titulo':titulo}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'computadoras/form_comp.html', context)
            #return HttpResponseRedirect("computadoras/nueva/")
    return render(request, 'computadoras/form_comp.html', context)

def comp_update(request, pk):
    instance = Equipo.objects.get(pk=pk)
    form = EquipoForm(request.POST or None, instance=instance)
    titulo = "Actualizar computadora existente"
    context = {'form':form,'titulo':titulo}
    if form.is_valid():
          form.save()
          return render(request, 'computadoras/form_comp.html', context)
    return render(request, 'computadoras/form_comp.html', context)



def buscar_comp(request):
    titulo = "Buscar computadora"
    context= {
        'titulo':titulo,
    }
    return render(request, 'computadoras/buscar_comp.html',context)


def comp_delete(request,pk):
    comp = Equipo.objects.get(pk=pk)
    context = {
        'comp':comp,
        'titulo': 'Registro a borrar'
    }
    return render(request,'computadoras/comp_delete.html',context)


def comp_delete_confirm(request,pk):
    comp = Equipo.objects.get(pk=pk)
    print "Id: ",comp.pk 
    print "Bien: ",comp.bien
    print "Arrendado:",comp.arrendado
    comp.delete()
    titulo = "Registro eliminado"
    return render(request,'computadoras/comp_delete_confirm.html',{'titulo':titulo})



def usuario_delete(request,pk):
    usuario = Usuario.objects.get(pk=pk)
    context = {
        'user':usuario,
        'titulo': 'Registro a borrar'
    }
    return render(request,'computadoras/usuario/usuario_delete.html',context)


def usuario_delete_confirm(request,pk):
    usuario = Usuario.objects.get(pk=pk)
    print "Id: ",usuario.pk 
    print "Nombre: ",usuario.nombre, " ", usuario.apellidos
    print "Cargo:",usuario.cargo
    usuario.delete()
    titulo = "Registro eliminado"
    return render(request,'computadoras/usuario/usuario_delete_confirm.html',{'titulo':titulo})
