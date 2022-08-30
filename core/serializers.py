from rest_framework.serializers import ModelSerializer

from core.models import Origen, Classe, Personagen

class OrigenSerializer(ModelSerializer):
    class Meta:
        model = Origen
        fields = "__all__"

class ClasseSerializer(ModelSerializer):
    class Meta:
        model = Classe
        fields = "__all__"

class PersonagenSerializer(ModelSerializer):
    class Meta:
        model = Personagen
        fields = "__all__"

class PersonagenDetailSerializer(ModelSerializer):
    class Meta:
        model = Personagen
        fields = "__all__"
        depth = 1