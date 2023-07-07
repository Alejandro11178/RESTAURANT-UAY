from django.urls import path, include
from rest_framework import routers
from . import views


# Un router en Django es una clase que permite registrar las vistas y rutas asociadas a un modelo en particular. 


router = routers.DefaultRouter()  # Creación de una URL predeterminada de Django REST Framework
router.register('plato', views.PlatoViewSet, basename="plato")  # Registro de la vista del ViewSet en el enrutador con la ruta 'plato'
router.register('destacado', views.PlatoDestacadoViewSet, basename="destacado") # El basename se usa para generar las rutas con el nombre asignado
# El router genera las urls para poder listar, verificar, eliminar y guardar los enlaces.


urlpatterns = [
    path('',include(router.urls)) # Asegura que las rutas generadas por el enrutador estén disponibles en 
                                  # la ruta principal del sitio web, permitiéndote acceder a las vistas y funcionalidades 
                                  #asociadas a esos endpoints a través de la página principal.
]

