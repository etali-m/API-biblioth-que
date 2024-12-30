from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from accounts.permissions import *

# Create your views here.
from .models import *
from .serializers import AuteurListSerializer, AuteurDetailsSerializer, LivreSerializer

#Mixin pour obtenir le serializer de details pour chaque classe.
class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()

#viewset pour les endpoints sur les auteurs
class AuteurViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = AuteurListSerializer
    detail_serializer_class = AuteurDetailsSerializer

    def get_queryset(self):
        queryset = Auteur.objects.all()
        #on recupère les paramètre url si il existe
        nom = self.request.GET.get('nom')
        if nom is not None:
            queryset = queryset.filter(nom__icontains=nom)
        return queryset
    
class AdminAuteurViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = AuteurListSerializer
    detail_serializer_class = AuteurDetailsSerializer

    permission_classes = [IsAdminAuthenticated]

    def get_queryset(self):
        queryset = Auteur.objects.all()

        return queryset

#Viewset pour les endpoints sur les livres
class LivreViewset(ModelViewSet):
    serializer_class = LivreSerializer

    def get_queryset(self):
        queryset = Livre.objects.all()
        #On recupère un paramètre d'url s'il existe 
        date_pub = self.request.GET.get('date_pub')
        auteur = self.request.GET.get('auteur')
        titre = self.request.GET.get('titre')

        if titre is not None:
            queryset = queryset.filter(titre__icontains=titre)

        if date_pub is not None:
            queryset = queryset.filter(date_publication__lte=date_pub)

        if auteur is not None:
            queryset = queryset.filter(auteur__nom__icontains=auteur)

        return queryset
