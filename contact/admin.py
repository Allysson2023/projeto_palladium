from django.contrib import admin
from contact import models

@admin.register(models.Apartamento)
class ApartamentoAdmin(admin.ModelAdmin):
    list_display ='id', 'numero_apartamento', 'anda',
    ordering = '-id',
    list_per_page = 10
    list_display_links = 'numero_apartamento',

@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = 'id','nome',
    ordering = '-id',
    list_display_links = 'nome',

@admin.register(models.Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = 'id','nome_proprietario', 'placa', 'obs',
    ordering = '-id',
    search_fields = 'nome_proprietario', 'placa',
    list_per_page = 10
    list_display_links = 'nome_proprietario',

@admin.register(models.Moradore)
class MoradoreAdmin(admin.ModelAdmin):
    list_display = 'id','nome', 'cpf', 'telefone',
    ordering = '-id',
    search_fields = 'nome',
    list_per_page = 10
    list_display_links = 'nome',

@admin.register(models.Registro_de_Visitante)
class Registro_de_VisitanteAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'cpf', 'telefone',
    ordering = '-id',
    search_fields = 'nome',
    list_per_page = 10
    list_display_links = 'nome',

@admin.register(models.Registros_de_Entrega)
class Registros_de_EntregaAdmin(admin.ModelAdmin):
    list_display = 'id','tipos_de_entrega', 'destino', 'apartamento', 'data_registro',
    ordering = '-id',
    search_fields = 'destino',
    list_per_page = 10
    list_display_links = 'destino',

@admin.register(models.Visitante)
class VisitanteAdmin(admin.ModelAdmin):
    list_display = 'id','nome','id_registro', 'apartamento', 'data_entrada', 'saida',
    ordering = '-id',
    search_fields = 'nome',
    list_per_page = 10
    list_display_links = 'nome',

@admin.register(models.Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display ='id', 'nome_completo', 'data',
    ordering = '-id',
    search_fields = 'nome_completo','data',
    list_per_page = 10
    list_display_links = 'nome_completo',

@admin.register(models.Eventos)
class EventosAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome_responsavel', 'local_evento', 'apartamento', 'data_horas_evento',
    ordering = '-id',
    search_fields = 'local_evento', 'data_horas_evento',
    list_display_links = 'nome_responsavel',