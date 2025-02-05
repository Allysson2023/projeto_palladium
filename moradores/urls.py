from django.urls import path, include
from moradores import views

app_name = 'moradores'

urlpatterns = [
    path('', views.indexMoradores, name='indexMoradores' ),
    path('registro_index/<int:id_visitante>/detail/', views.visitante_id, name='visitante_id' ),
    path('busca_visitantes/', views.busca_visitante, name='busca_visitante' ),
    
    path('eventos/', views.eventos, name='eventos' ),
    path('id_eventos/<int:id_eventos>/detail/', views.eventos_id, name='eventos_id' ),
    path('busca_eventos/', views.eventos_busca, name='eventos_busca' ),

    path('entregas/', views.entregas, name='entregas' ),
    path('entregas_busca/', views.entregas_busca, name='entregas_busca' ),
    path('id_entregas/<int:id_entregas>/detail/', views.entregas_id, name='entregas_id'),



    path('user/login/', views.login_views_moradores, name='login_views_moradores' ),
    path('user/logaut/', views.logaut_views_moradores, name='logaut_views_moradores' ),

]