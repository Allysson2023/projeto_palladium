from django.shortcuts import render
from contact.models import *

# Create your views here.
def indexMoradores(request):
    moradores = Visitante.objects.filter().order_by('-id')
    return render(
        request,
        'moradores/index.html',
        {'moradores':moradores}
    )