from django.contrib import admin
from src.core.models import *


class AssuntoSaberMaisModelAdmin( admin.ModelAdmin ):
    save_on_top = True
    list_display = ['nome', 'ordem', 'ativo']
    date_hierarchy = 'criado_em'
    search_fields = ('nome',)
    list_filter = ('criado_em',)
    list_display_links = ('nome',)

class UsuarioGuiaModelAdmin( admin.ModelAdmin ):
    save_on_top = True
    list_display = ['nome', 'email', 'cidade', 'ja_fez_compras', 'ativo']
    date_hierarchy = 'criado_em'
    search_fields = ('nome',)
    list_filter = ('criado_em',)
    list_display_links = ('nome',)


admin.site.register(AssuntoSaberMais, AssuntoSaberMaisModelAdmin)
admin.site.register(UsuarioGuia, UsuarioGuiaModelAdmin)