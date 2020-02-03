from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico, DocIdentificacao
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco
from recursos.api.serializers import RecursoSerializer
from recursos.models import Recurso

class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'

class PontoTuristicoSerializer(ModelSerializer):
    recursos = RecursoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()
    doc_identificacao = DocIdentificacaoSerializer()

  #  aprovacao = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'recursos',
                  'comentarios', 'avaliacoes', 'endereco', 'foto',
                  'descricao_completa', 'aprovacao', 'doc_identificacao']

        read_only_fields = ['comentarios', 'avaliacoes']

    def cria_recursos(self, recursos, ponto):
        for recurso in recursos:
            rc = Recurso.objects.create(**recurso)
            ponto.recursos.add(rc)

    def create(self, validated_data):

        recursos = validated_data['recursos']
        del validated_data['recursos']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_recursos(recursos, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.doc_identificacao = doci

        ponto.save()

        return ponto


    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)

 #   def get_aprovacao(self, obj):
 #       return '%s - %s' % (obj.id, obj.aprovado)