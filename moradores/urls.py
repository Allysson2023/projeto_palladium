from django.urls import path, include
from moradores import views

app_name = 'moradores'

urlpatterns = [
    path('', views.indexMoradores, name='indexMoradores' ),
    

]