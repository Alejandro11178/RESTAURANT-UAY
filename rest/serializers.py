from rest_framework import serializers  
from core.models import Plato  

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato  # Modelo a ser serializado
        fields = '__all__'  
class PlatoDestacadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato  # Modelo a ser serializado
        fields = '__all__'  
