from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from recursos.api.serializers import RecursoSerializer
from recursos.models import Recurso

class RecursoViewSet(ModelViewSet):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer
    filter_backends = {DjangoFilterBackend, SearchFilter}
    filter_fields = ('nome', 'descricao')
    search_fields = ('nome', 'descricao')

