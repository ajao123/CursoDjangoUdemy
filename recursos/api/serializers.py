from rest_framework.serializers import ModelSerializer
from recursos.models import Recurso

class RecursoSerializer(ModelSerializer):
    class Meta:
        model = Recurso
        fields = ['id', 'nome', 'descricao', 'horario_func', 'idade_minima', 'foto']