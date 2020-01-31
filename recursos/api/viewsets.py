from rest_framework.viewsets import ModelViewSet
from recursos.api.serializers import RecursoSerializer
from recursos.models import Recurso

class RecursoViewSet(ModelViewSet):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer