from rest_framework import serializers
from .models import Auteur, Livre
from datetime import date


#serializer pour les information de liste sur les livre
class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = ['id', 'titre', 'genre', 'date_publication', 'auteur', 'disponible']

    def validate_titre(self, value):
        if len(value) <=3:
            raise serializers.ValidationError('La taille du titre ne peut pas être inférieur à 3')
        return value


#serializer pour la liste des auteurs auteur
class AuteurListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = ['id', 'nom', 'prenom', 'date_naissance']

    def validate_nom(self, value):
        if len(value) <=3:
            raise serializers.ValidationError('La taille du nom ne peut pas être inférieur à 3')
        return value
    
    def validate_prenom(self, value):
        if len(value) <=3:
            raise serializers.ValidationError('La taille du nom ne peut pas être inférieur à 3')
        return value
    
    def validate_date_naissance(self, value):
        if value >= date(2010,12,31):
            raise serializers.ValidationError('La date de naissance doit être postérieure à 2010.')
        return value


#serializer pour les details sur un auteur
class AuteurDetailsSerializer(serializers.ModelSerializer):
    livres =  serializers.SerializerMethodField()

    class Meta:
        model = Auteur
        fields = ['id', 'nom', 'prenom', 'date_naissance', 'livres']

    def get_livres(self, instance):
        query_set = instance.livres
        serializer = LivreSerializer(query_set, many=True)

        return serializer.data
