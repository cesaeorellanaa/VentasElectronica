from django.shortcuts import render
from .models import Cliente
from .forms import FormCliente



# Create your views here.



def index(request) :
    return render(request, 'VentasElectronica/index.html')

def checkout(request) : 
    return render(request, 'VentasElectronica/checkout.html')

def product(request) :
    return render(request, 'VentasElectronica/product.html')





def login(request) :
    return render(request, 'VentasElectronica/login.html')


def Solicitud(request) :
    if request.method == 'POST' :
        form = FormCliente(request.POST)
        if form.is_valid() :
            cliente = form.save()
            return render(request, 
                'VentasElectronica/send.html',
                {'cliente' : cliente})
    else :
        form = FormCliente()
        return render(request, 'VentasElectronica/checkout.html',
            {'form' : form})


def Formulario(request) :
    form = FormCliente()
    return render(request, 'VentasElectronica/Formulario.html',  {'form' : form})



def Listado(request) :
    # recuperamos a todas las Clientes de la BD
    listaCliente = Cliente.objects.all()
    return render(request, 'VentasElectronica/Listado.html',
        { 'listaCliente' : listaCliente,
        'cuantos' : len(listaCliente)
        })