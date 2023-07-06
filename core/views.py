from django.shortcuts import render
from .models import Plato

# Create your views here.

def menu(request):
    platos = Plato.objects.all()
    return render(request, 'core/menu.html', {'menu': platos})

def destacados(request):
    platos_destacados = Plato.objects.filter(destacado=True)
    return render(request, 'core/destacados.html', {'platos_destacados': platos_destacados})