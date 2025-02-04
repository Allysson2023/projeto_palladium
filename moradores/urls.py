from django.urls import path, include
from moradores import views

app_name = 'moradores'

urlpatterns = [
    path('', views.indexMoradores, name='indexMoradores' ),
    path('registro_index/<int:id_visitante>/detail/', views.visitante_id, name='visitante_id' ),
    path('busca_visitantes/', views.busca_visitante, name='busca_visitante' ),
    

]