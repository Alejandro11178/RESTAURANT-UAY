from django.shortcuts import render  
from rest_framework import viewsets  
from .serializers import PlatoSerializer 
from core.models import Plato  


#Serializador : es una clase que se utiliza para convertir los objetos de Django en formatos 
# de datos que se puedan enviar a través de la API, como JSON, XML o incluso representaciones HTML. 

# Create your views here.
class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()  # Conjunto de datos que se utilizará para la vista
    serializer_class = PlatoSerializer  # Clase de serializador para convertir objetos Plato en formato JSON

  
class PlatoDestacadoViewSet(viewsets.ModelViewSet):
   queryset = Plato.objects.filter(destacado=True)
   serializer_class = PlatoSerializer