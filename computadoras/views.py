from django.shortcuts import render , get_object_or_404
from .models import Departamento
from .models import Computadora
from django.views.defaults import page_not_found
from django.conf import settings
from .forms import ComputadoraForm
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


def base_comp(request):
    return render(request, 'computadoras/base_comp.html', {})


#http://localhost:8000/pk/
def comp_detalle(request, pk):
    comp = get_object_or_404(Computadora, pk=pk)
    print "Comp pk:"+comp
    return render(request, 'computadoras/comp_detalle.html', {'comp': comp})


#http://localhost:8000/computadoras
def comp_list(request):
    comps = Computadora.objects.all()
    return render(request, 'computadoras/comp_list.html', {'comps':comps})

#http://localhost:8000/computadoras/nueva/
def comp_nueva(request):
    form = ComputadoraForm(request.POST)
    try:
        #form = ComputadoraForm(request.POST)
        print "formulario: ",form
        comp = form.save(commit=False)
        comp.save()
        print "Post guardado"
    except ValueError as error:
        print "Error al crear nuevo post: ",error
    return render(request, 'computadoras/comp_nueva.html', {'form': form})


#http://localhost:8000/computadoras/pk/edit
def comp_edit(request, pk):
    comp = get_object_or_404(Computadora, pk=pk)
    form = PostForm(request.POST, instance=comp)
    valido = "Formulario valido" if form.is_valid() else "Formulario no valido"
    if request.method == "POST":
        print "form: ",form
        print valido
        if form.is_valid():
            print "Formulario valido"
            comp = form.save(commit=False)
            #post.author = request.user
            comp.save()
            comps = Computadora.objects.all()
            return render(request, 'computadoras/comp_list.html', {'comps': comps})
        else:
            print "form no valido"
            form = ComputadoraForm(instance=comp)
    else:
        print "form: ",form
        print valido
        return render(request, 'computadoras/comp_edit.html', {'form': form})
