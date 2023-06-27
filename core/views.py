from django.shortcuts import render
from .models import Plato

# Create your views here.

def menu(request):
    platos = Plato.objects.all()
    return render(request, 'core/menu.html',{'menu': platos})