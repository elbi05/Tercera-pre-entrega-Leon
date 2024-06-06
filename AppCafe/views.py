from django.shortcuts import render
from AppCafe.models import *
from AppCafe.forms import *
from django.http import HttpResponse

# Create your views here.
def inicio(req):
    return render(req, "AppCafe/inicio.html")

def cliente(req):
    return render(req,"AppCafe/cliente.html")

def mesero(req):
    return render(req,"AppCafe/mesero.html")

def cuenta(req):
    return render(req,"AppCafe/cuenta.html")

def buscar(req):
    return render(req,"AppCafe/buscar.html")

def cliente(req):
    if req.method=='POST':
        miFormulario=ClienteFormulario(req.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            cliente=Cliente(nombre=informacion['nombre'],mesa=informacion['mesa'],email=informacion['email'])
            cliente.save()
            return render(req,"AppCafe/inicio.html")
    else:
        miFormulario=ClienteFormulario()
    return render(req, "AppCafe/cliente.html",{"miFormulario":miFormulario})

def mesero(req):
    if req.method=='POST':
        miFormulario=MeseroFormulario(req.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            mesero=Mesero(nombre=informacion['nombre'],mesa=informacion['mesa'])
            mesero.save()
            return render(req,"AppCafe/inicio.html")
    else:
        miFormulario=MeseroFormulario()
    return render(req,"AppCafe/mesero.html",{"miFormulario":miFormulario})

def cuenta(req):
    if req.method=='POST':
        miFormulario=CuentaFormulario(req.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            cuenta=Cuenta(total=informacion['total'],mesa=informacion['mesa'])
            cuenta.save()
            return render(req, "AppCafe/inicio.html")
    else:
        miFormulario=CuentaFormulario()
    return render(req,"AppCafe/cuenta.html",{"miFormulario":miFormulario})

def busquedaMesa(req):
    return render(req,"AppCafe/busquedaMesa.html")

def buscar(req):
    if req.GET["mesa"]:
        mesa=req.GET["mesa"]
        cuenta=Cuenta.objects.filter(mesa__icontains=mesa)
        cliente=Cliente.objects.filter(mesa__icontains=mesa)
        mesero=Mesero.objects.filter(mesa__icontains=mesa)
        return render(req,"AppCafe/resultadosBusqueda.html",{"cuenta":cuenta,"mesa":mesa,"cliente":cliente,"mesero":mesero})
    else:
        respuesta="No enviaste datos"
    #return HttpResponse(respuesta)
    return render(req,"AppCafe/inicio.html",{"respuesta":respuesta})

