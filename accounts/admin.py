from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'is_active', 'is_verified')
    list_display_links = ('id', 'first_name') #Lien pour pouvoir accéder au détails d'une annonce
    list_editable = ('is_active',)
    list_filter = ('first_name',)  #appliquer les filtres sur une colonne
    list_per_page = 25 #définir la pagination sur la page d'admiistration

admin.site.register(User, UserAdmin)
