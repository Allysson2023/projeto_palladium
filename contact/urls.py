from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    # Index da pagina
    path('search/', views.search, name='search' ),
    path('', views.index, name='index' ),
    # visitante (CRUD) 
    path('visitantes/<int:visitante_id>/detail/', 
         views.visitanteIndex, name='visitanteIndex' ),
    path('visitantes/create/', views.create_visitantes, 
         name='create_visitantes' ),
    path('visitantes/<int:visitante_id>/update/', 
         views.visitanteIndexUpdate, name='visitanteIndexUpdate' ),

    # Busca do Registro de Visitantes
    path('search/registro_visitantes/', views.registro_visitantes_index_busca, 
         name='registro_visitantes_index_busca' ),
    path('registro_visitantes/', views.registro_visitantes_index, 
         name='registro_visitantes_index' ),
    # REGISTRO VISITANTES CRUD
    path('registro_visitantes/<int:registro_id>/detail/', 
         views.registro_visitantes_index_contato, 
         name='registro_visitantes_index_contato' ),
    path('registro_visitantes/create_registro_visitantes/', 
         views.create_registro_de_visitantes, 
         name='create_registro_de_visitantes' ),
    path('registro_visitantes/<int:registro_id>/update/', 
         views.update_registro_de_visitantes, 
         name='update_registro_de_visitantes' ),

    # URL de Registro de entregas
    path('search/registro_entregas/', views.registro_entregas_index_busca, 
         name='registro_entregas_index_busca' ),
    path('registro_entregas/', views.registro_entregas_index, 
         name='registro_entregas_index' ),
    # CRUDde Registro de entregas
    path('registro_entregas_index_contato/<int:entregas_id>/detail/', 
         views.registro_entregas_index_contato, 
         name='registro_entregas_index_contato' ),
    path('registro_entregas/create_entregas/', views.entregas, 
         name='create_entregas' ),
    path('registro_entregas_index_contato/<int:entregas_id>/update/', 
         views.update_entregas, 
         name='update_entregas' ),

     #URL MORADORES
    path('search/busca_moradores/', views.moradores_index_busca, 
         name='moradores_index_busca' ),
    path('moradores_index_id/<int:moradores_id>', views.moradores_index_id, 
         name='moradores_index_id' ),
    path('moradores/', views.moradores_index, 
         name='moradores_index' ),

     # URL dos carros condominio  carros_index_id
    path('carros_index_busca/', views.carros_index_busca, 
         name='carros_index_busca' ),
    path('contanto_veiculo_id/<int:carro_id>', views.carros_index_id, 
         name='carros_index_id' ),
    path('carros/', views.carros_index, 
         name='carros_index' ),

    # URL Ocorrencia
    path('ocorrencias_busca/', views.ocorrencias_index_busca, 
         name='ocorrencias_index_busca' ),
    path('ocorrencias_index/', views.ocorrencias_index, 
         name='ocorrencias_index' ),
    # CRUD Ocorrencia
    path('ocorrencias_id/create_ocorrencia/', views.ocorrenciaIndex , 
         name='ocorrenciaIndex' ),
    path('ocorrencias_id/<int:id_ocorrencia>/detail/', 
         views.ocorrencias_index_id, 
         name='ocorrencias_index_id' ),
    path('ocorrencias_id/<int:id_ocorrencia>/update/', 
         views.ocorrenciaUpdate, 
         name='ocorrenciaUpdate' ),
     # URL Eventos
    path('index_eventos/', views.eventos, name='eventos' ),
    path('eventos_busca/', views.eventos_busca, name='eventos_busca' ),
     # CRUD Eventos
    path('eventos_busca/<int:eventos_id>/detail/', views.eventos_id, 
         name='eventos_id' ),
    path('eventos_busca/create_eventos/', views.create_eventos, 
         name='create_eventos' ),
    path('eventos_busca/<int:eventos_id>/update_eventos/', 
         views.update_eventos, name='update_eventos' ),
    path('eventos_busca/<int:eventos_id>/delete/', views.delete, 
         name='delete' ),



     # User Register
    path('user/create_user/', views.register, name='register' ),
    path('user/login/', views.login_views, name='login_views' ),
    path('user/logaut/', views.logaut_views, name='logaut_views' ),
    path('user/update/', views.user_update, name='user_update' ),
















]

