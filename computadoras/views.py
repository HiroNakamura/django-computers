from django.shortcuts import render
from .models import Departamento
from .models import Computadora
from django.views.defaults import page_not_found
from django.conf import settings
from .forms import ComputadoraForm

 
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


def comp_detalle(request, pk):
    comp = get_object_or_404(Computadora, pk=pk)
    return render(request, 'computadoras/comp_detalle.html', {'comp': comp})

def comp_list(request):
    comps = Computadora.objects.all()
    return render(request, 'computadoras/comp_list.html', {'comps':comps})

def comp_nueva(request):
    try:
        form = ComputadoraForm(request.POST)
        comp = form.save(commit=False)
        user = User.objects.get(username='fer')
        comp.save()
        print "Computadora almacenada"
    except ValueError as error:
        print "Ha ocurrido un error en el formulario: ",error
    return render(request, 'computadoras/comp_edit', {'form': form})    