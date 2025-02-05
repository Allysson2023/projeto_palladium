from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Visitante, Registro_de_Visitante,\
Registros_de_Entrega, Moradore, Carro, Ocorrencia, Eventos
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from contact.views.user_forms import *
#  Pagina do Index do Visitantes

@porteiro_required
def index(request):
    visitantes = Visitante.objects.filter().order_by('-id')

    paginator = Paginator(visitantes, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Entrada de Visitantes -',
    }

    return render(
        request,
        'contact/visitantes/index.html',
        context,
    )

@porteiro_required
def eventos(request):
    agenda = Eventos.objects.filter().order_by('-id')
    
    paginator = Paginator(agenda, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Agendamento de Eventos -',
    }
    return render(
        request,
        'contact/eventos/index_eventos.html',
        context,
    )



# Index de Registro de Visitante
@porteiro_required
def registro_visitantes_index(request):
    registro_visitantes = Registro_de_Visitante.objects.filter().order_by('-id')

    paginator = Paginator(registro_visitantes, 10)
    page_number = request.GET.get("page")
    registro_visitantes = paginator.get_page(page_number)
    

    context = {
        'registro_visitantes': registro_visitantes,
        'site_title': 'Registro de Visitantes -',
    }

    return render(
        request,
        'contact/registro_visitantes/registros_Visitantes.html',
        context,
    )


#  Pagina do Index do Registro de Entregas
@porteiro_required
def registro_entregas_index(request):
    registro_entregas = Registros_de_Entrega.objects.filter().order_by('-id')

    paginator = Paginator(registro_entregas, 10)
    page_number = request.GET.get("page")
    registro_entregas = paginator.get_page(page_number)

    context = {
        'registro_entregas': registro_entregas,
        'site_title': 'Registros de Entregas -',
    }

    return render(
        request,
        'contact/entregas/entregas_index.html',
        context,
    )

# Moradore Index
@porteiro_required
def moradores_index(request):
    moradores = Moradore.objects.filter().order_by('-id')
    
    paginator = Paginator(moradores, 10)
    page_number = request.GET.get("page")
    moradores = paginator.get_page(page_number)

    context = {
        'moradores': moradores,
        'site_title': 'Moradores Condominio -',
    }

    return render(
        request,
        'contact/moradores/moradores.html',
        context,
    )

@porteiro_required
def carros_index(request):
    carros = Carro.objects.filter().order_by('-id')

    paginator = Paginator(carros, 10)
    page_number = request.GET.get("page")
    carros = paginator.get_page(page_number)

    context = {
        'carros':carros,
        'site_title': 'Carros Condominio -',
    }
    return render(
        request,
        'contact/veiculos/veiculos.html',
        context,
    )

@porteiro_required
def ocorrencias_index(request):
    ocorrencias = Ocorrencia.objects.filter().order_by('-id')
    paginator = Paginator(ocorrencias, 12)
    page_number = request.GET.get("page")
    ocorrencias = paginator.get_page(page_number)
    
    context = {
        'ocorrencias':ocorrencias,
        'site_title':'Ocorrencia do Platão -',
    }
    return render(
        request,
        'contact/ocorrencias/ocorrencias.html',
        context,
    )


# Busca listas do Visitantes
@porteiro_required
def search(request):
    search_value = request.GET.get('q', '').strip()
    if search_value == '':
        return redirect('contact:index')

    visitantes = Visitante.objects.filter(nome__icontains = search_value)\
        .order_by('-id')
    paginator = Paginator(visitantes, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search -',
        'search_value':search_value,
    }

    return render(
        request,
        'contact/visitantes/index.html',
        context,
    )

@porteiro_required
def eventos_busca(request):
    busca_evento = request.GET.get('q', '').strip()
    if busca_evento == '':
        return redirect('contact:eventos')
    
    agenda = Eventos.objects.filter(nome_responsavel__icontains = busca_evento ).order_by('-id')
    
    paginator = Paginator(agenda, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Agendamentos -',
        'busca_eventos': busca_evento,
    }
    return render(
        request,
        'contact/eventos/index_eventos.html',
        context,
    )

# Busca  listas Registro do Visitantes
@porteiro_required
def registro_visitantes_index_busca(request):
    
    busca_registro_visitantes = request.GET.get('q', '').strip()
    if busca_registro_visitantes == '':
        return redirect('contact:registro_visitantes_index')
    
    registro_visitantes = Registro_de_Visitante.objects.\
        filter(nome__icontains= busca_registro_visitantes).order_by('-id')
    
    paginator = Paginator(registro_visitantes, 10)
    page_number = request.GET.get("page")
    registro_visitantes = paginator.get_page(page_number)

    context = {
        'registro_visitantes': registro_visitantes,
        'site_title': ' Buscando Registro de Visitantes -',
        'busca_registro_visitantes': busca_registro_visitantes,
    }

    return render(
        request,
        'contact/registro_visitantes/registros_Visitantes.html',
        context,
    )

@porteiro_required
def registro_entregas_index_busca(request):
    busca_registro_entregas = request.GET.get('q', '').strip()

    if busca_registro_entregas == '':
        return redirect('contact:registro_entregas_index')
    
    registro_entregas = Registros_de_Entrega.objects.\
        filter(destino__icontains=busca_registro_entregas)\
        .order_by('-id')
    
    paginator = Paginator(registro_entregas, 10)
    page_number = request.GET.get("page")
    registro_entregas = paginator.get_page(page_number)

    context = {
        'registro_entregas': registro_entregas,
        'site_title': 'Registros de Entregas -',
        'busca_registro_entregas':busca_registro_entregas,
    }

    return render(
        request,
        'contact/entregas/entregas_index.html',
        context,
    )


# Busca Lista de carros
@porteiro_required
def carros_index_busca(request):
    busca_carro = request.GET.get('q', '').strip()
    
    if busca_carro == '':
        return redirect('contact:carros_index')
    
    carros = Carro.objects\
        .filter(
            Q(nome_proprietario__icontains=busca_carro) |
            Q(placa__icontains=busca_carro) |
            Q(cor__icontains=busca_carro) |
            Q(modelo__icontains=busca_carro) 
        )\
        .order_by('-id')
    
    paginator = Paginator(carros, 10)
    page_number = request.GET.get("page")
    carros = paginator.get_page(page_number)

    context = {
        'carros':carros,
        'site_title': 'Carros Condominio -',
        'busca_carro':busca_carro,
    }
    return render(
        request,
        'contact/veiculos/veiculos.html',
        context,
    )

# Busca Ocorrencias
@porteiro_required
def ocorrencias_index_busca(request):
    busca_ocorrencia = request.GET.get('q', '').strip()
    if busca_ocorrencia == '':
        return redirect('contact:ocorrencias_index')

    ocorrencias = Ocorrencia.objects\
        .filter(
            Q(data__icontains=busca_ocorrencia)| 
            Q(nome_completo__icontains=busca_ocorrencia) 
        ).order_by('-id')
    paginator = Paginator(ocorrencias, 12)
    page_number = request.GET.get("page")
    ocorrencias = paginator.get_page(page_number)
    
    context = {
        'ocorrencias':ocorrencias,
        'site_title':'Ocorrencia do Platão -',
        'busca_ocorrencia':busca_ocorrencia,
    }
    return render(
        request,
        'contact/ocorrencias/ocorrencias.html',
        context,
    )



# Busca Lista Moradores
@porteiro_required
def moradores_index_busca(request):
    busca_moradores = request.GET.get('q', '').strip()
    if busca_moradores == '':
        return redirect('contact:moradores_index')
    moradores = Moradore.objects.filter(nome__icontains=busca_moradores)\
        .order_by('-id')
    
    paginator = Paginator(moradores, 10)
    page_number = request.GET.get("page")
    moradores = paginator.get_page(page_number)

    context = {
        'moradores': moradores,
        'site_title': 'Moradores Condominio -',
        'busca_moradores':busca_moradores,
    }

    return render(
        request,
        'contact/moradores/moradores.html',
        context,
    )

# Busca id do Visitantes
@porteiro_required
def visitanteIndex(request, visitante_id):
    visitanteIndex = get_object_or_404(Visitante, pk=visitante_id)

    site_title = f'  { visitanteIndex.nome } - '
    
    context = {
        'visitantes': visitanteIndex,
        'site_title': site_title,
    }

    return render(

        
        request,
        'contact/visitantes/index_visitante.html',
        context,
    )

# Busca id do Registro do Visitantes
@porteiro_required
def registro_visitantes_index_contato(request, registro_id):
    single_registro_visitantes = get_object_or_404(Registro_de_Visitante,\
                                                   pk=registro_id)

    context = {
        'registro_visitante': single_registro_visitantes,
        'site_title': 'Registro de Visitantes -',
    }

    return render(
        request,
        'contact/registro_visitantes/registros_visitantes_id.html',
        context,
    )



#  Busca ID do Registro de Entregas
@porteiro_required
def registro_entregas_index_contato(request, entregas_id):
    busca_registro_entregas = get_object_or_404(Registros_de_Entrega, \
                                                pk=entregas_id)

    context = {
        'registro_entregas': busca_registro_entregas,
        'site_title': 'Contato do Registros de Entregas -',
    }

    return render(
        request,
        'contact/entregas/registros_entregas_id.html',
        context,
    )

# Busca Id do Moradores
@porteiro_required
def moradores_index_id(request, moradores_id):
    id_moradores =get_object_or_404(Moradore, pk=moradores_id)

    context = {
        'moradore': id_moradores,
        'site_title': ' Contato do Moradores Condominio -',
    }

    return render(
        request,
        'contact/moradores/id_moradores.html',
        context,
    )

# Busca Id do Carro
@porteiro_required
def carros_index_id(request, carro_id):
    id_carros = get_object_or_404(Carro, pk=carro_id)
    context = {
        'carro':id_carros,
        'site_title': 'Contato do Veiculo Condominio -',
    }
    return render(
        request,
        'contact/veiculos/id_veiculos.html',
        context,
    )

@porteiro_required
def eventos_id(request, eventos_id):
    id_eventos = get_object_or_404(Eventos, pk=eventos_id)
    context = {
        'id_eventos': id_eventos,
        'site_title': 'Contato do Evento do Condominio -',
    }
    
    return render(
        request,
        'contact/eventos/id_eventos.html',
        context,
    )


# id das ocorrencia
@porteiro_required
def ocorrencias_index_id(request, id_ocorrencia):
    id_ocorrencias = get_object_or_404(Ocorrencia, pk=id_ocorrencia)
    
    context = {
        'ocorrencia':id_ocorrencias,
        'site_title':'Status da Ocorrencia do Platão -',
    }
    return render(
        request,
        'contact/ocorrencias/ocorrencias_id.html',
        context,
    )