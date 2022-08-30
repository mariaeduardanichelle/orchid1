from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from core.models import Origen, Classe, Personagen
from core.serializers import OrigenSerializer, ClasseSerializer, PersonagenSerializer, PersonagenDetailSerializer

class OrigenViewSet(ModelViewSet):
    queryset = Origen.objects.all()
    serializer_class = OrigenSerializer

class ClasseViewSet(ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

class PersonagenViewSet(ModelViewSet):
    queryset = Personagen.objects.all()
    serializer_class = PersonagenSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PersonagenDetailSerializer
        return PersonagenSerializer
