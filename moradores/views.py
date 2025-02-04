from django.shortcuts import render
from contact.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
def indexMoradores(request):
    moradores = Visitante.objects.filter().order_by('-id')

    paginator = Paginator(moradores, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(
        request,
        'moradores/index.html',
        {'moradores':page_obj}
    )
# def index(request):
#     visitantes = Visitante.objects.filter().order_by('-id')

#     paginator = Paginator(visitantes, 10)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     context = {
#         'page_obj': page_obj,
#         'site_title': 'Entrada de Visitantes -',
#     }

#     return render(
#         request,
#         'contact/visitantes/index.html',
#         context,
#     )

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
        return redirect('moradores:indexMoradores')

    moradores = Visitante.objects.filter(nome__icontains = busca_id )\
        .order_by('-id')

    context = {
        'moradores': moradores,
        'site_title': 'Search -',
        'search_value':busca_id,
    }

    return render(
        request,
        'moradores/index.html',
        context,
    )