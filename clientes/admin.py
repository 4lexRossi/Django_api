from django.contrib import admin
from clientes.models import Cliente

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

admin.site.register(Cliente, Clientes)
