from contact.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from functools import wraps


# Decorador para garantir que apenas moradores acessem
def morador_required(view_func):
    @wraps(view_func)
    @login_required(login_url='moradores:login_views_moradores')  # Exige login
    def _wrapped_view(request, *args, **kwargs):
        if not hasattr(request.user, 'moradore'):  # Se não for morador
            messages.error(request, 'Acesso negado! Somente moradores podem acessar esta área.')  
            return redirect('moradores:login_views_moradores')  # Redireciona para a página inicial ou login dos porteiros

        return view_func(request, *args, **kwargs)

    return _wrapped_view

@morador_required
def indexMoradores(request):
    morador = request.user.moradore
    visitantes = Visitante.objects.filter(apartamento=morador.apartamento).order_by('-id')

    paginator = Paginator(visitantes, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'moradores/index.html', {'page_obj': page_obj})

@morador_required
def visitante_id(request, id_visitante):
    visitanteIndex = get_object_or_404(Visitante, pk=id_visitante)
    site_title = f'  {visitanteIndex.nome} - '

    context = {
        'visitantes': visitanteIndex,
        'site_title': site_title,
    }
    return render(request, 'moradores/id_visitante.html', context)

@morador_required
def busca_visitante(request):
    busca_id = request.GET.get('q', '').strip()
    if busca_id == '':
        messages.info(request, 'Escreva no campo de busca o que deseja procurar...')
        return redirect('moradores:indexMoradores')

    moradores = Visitante.objects.filter(
        nome__icontains=busca_id,
        apartamento=request.user.moradore.apartamento  # Corrigido
    ).order_by('-id')

    paginator = Paginator(moradores, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search -',
        'search_value': busca_id,
    }

    return render(request, 'moradores/index.html', context)

@morador_required
def eventos_id(request, id_eventos):
    evento_id = get_object_or_404(Eventos, pk=id_eventos)

    context = {
        'id_eventos': evento_id,
        'site_title': 'Contato do Evento do Condomínio -',
    }
    
    return render(request, 'moradores/id_eventos.html', context)

@morador_required
def eventos(request):
    morador = request.user.moradore
    eventos = Eventos.objects.filter(apartamento=morador.apartamento).order_by('-id')

    paginator = Paginator(eventos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'moradores/eventos.html', {'page_obj': page_obj})

@morador_required
def eventos_busca(request):
    busca_evento = request.GET.get('q', '').strip()
    if busca_evento == '':
        messages.info(request, 'Escreva no campo de busca o que deseja procurar...')
        return redirect('moradores:eventos')

    agenda = Eventos.objects.filter(
        nome_responsavel__icontains=busca_evento
    ).order_by('-id')

    paginator = Paginator(agenda, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Agendamentos -',
        'busca_eventos': busca_evento,
    }
    return render(request, 'moradores/eventos.html', context)

@morador_required
def entregas(request):
    morador = request.user.moradore
    entregasindex = Registros_de_Entrega.objects.filter(apartamento=morador.apartamento).order_by('-id')

    paginator = Paginator(entregasindex, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}

    return render(request, 'moradores/entregas.html', context)

@morador_required
def entregas_busca(request):
    busca_entrega = request.GET.get('q', '').strip()

    if busca_entrega == '':
        return redirect('moradores:entregas')
    
    entregasindex = Registros_de_Entrega.objects.filter(
        destino__icontains=busca_entrega
    ).order_by('-id')

    paginator = Paginator(entregasindex, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
 
    context = {
        'page_obj': page_obj,
        'busca_entrega': busca_entrega,
    }

    return render(request, 'moradores/entregas.html', context)

@morador_required
def entregas_id(request, id_entregas):
    entregas_id = get_object_or_404(Registros_de_Entrega, pk=id_entregas)

    context = {
        'registro_entregas': entregas_id,
        'site_title': 'Contato das entregas no Condomínio -',
    }
    
    return render(request, 'moradores/id_entregas.html', context)

def login_views_moradores(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Bem-vindo ao Sistema Patrimonial!')
            return redirect('moradores:indexMoradores')

        messages.error(request, 'Login inválido')

    return render(request, 'user/login_moradores.html', {'form': form})

@morador_required
def logaut_views_moradores(request):
    auth.logout(request)
    messages.info(request, 'Você saiu do Sistema!')
    return redirect('moradores:login_views_moradores')