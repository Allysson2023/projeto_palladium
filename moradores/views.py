from django.shortcuts import render
from contact.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def indexMoradores(request):
    moradores = Visitante.objects.filter().order_by('-id')

    paginator = Paginator(moradores, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'moradores/index.html',
        {'page_obj':page_obj}
    )

def visitante_id(request, id_visitante):
    visitanteIndex = get_object_or_404(Visitante, pk=id_visitante)
    site_title = f'  { visitanteIndex.nome } - '
    context = {
        'visitantes': visitanteIndex,
        'site_title': site_title,
    }
    return render(
        request,
        'moradores/id_visitante.html',
        context,
    )

def busca_visitante(request):
    busca_id = request.GET.get('q', '').strip()
    if busca_id  == '':
        messages.info(request, 'Escreva no campo de Busca oque você deseja procura...')
        return redirect('moradores:indexMoradores')

    moradores = Visitante.objects.filter(nome__icontains = busca_id )\
        .order_by('-id')
    
    paginator = Paginator(moradores, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search -',
        'search_value':busca_id,
    }

    return render(
        request,
        'moradores/index.html',
        context,
    )

def eventos(request):
    eventos = Eventos.objects.filter().order_by('-id')

    paginator = Paginator(eventos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'moradores/eventos.html',
        {'page_obj':page_obj}
    )

def eventos_id(request, id_eventos):
    evento_id = get_object_or_404(Eventos, pk=id_eventos)

    context = {
        'id_eventos': evento_id,
        'site_title': 'Contato do Evento do Condominio -',
    }
    
    return render(
        request,
        'moradores/id_eventos.html',
        context,
    )

def eventos_busca(request):
    busca_evento = request.GET.get('q', '').strip()
    if busca_evento == '':
        messages.info(request, 'Escreva no campo de Busca oque você deseja procura...')
        return redirect('moradores:eventos')
    
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
        'moradores/eventos.html',
        context,
    )

def entregas(request):
    entregasindex = Registros_de_Entrega.objects.filter().order_by('-id')

    paginator = Paginator(entregasindex, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'moradores/entregas.html',
        {'page_obj':page_obj}
    )