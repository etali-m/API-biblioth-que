from django.contrib import admin
from .models import Auteur, Livre

# Register your models here.
class AuteurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'date_naissance')
    list_display_links = ('id', 'nom') #Lien pour pouvoir accéder au détails d'une annonce
    list_filter = ('nom',)  #appliquer les filtres sur une colonne
    list_per_page = 25 #définir la pagination sur la page d'admiistration


admin.site.register(Auteur, AuteurAdmin)