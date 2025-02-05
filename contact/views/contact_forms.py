from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import VisitantesForm, Registro_visitantesForm, Registros_de_EntregaForm, OcorrenciaForm, EventosForm
from django.urls import reverse
from contact.models import Visitante,Registro_de_Visitante, Registros_de_Entrega, Ocorrencia, Eventos
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from contact.views.user_forms import *

@porteiro_required
def create_visitantes(request):
    form_action = reverse('contact:create_visitantes')

    if request.method == 'POST':
        form_visitantes = VisitantesForm(request.POST)

        context = {
            'form': form_visitantes,
            'form_action': form_action,
        }

        if form_visitantes.is_valid():
            form_visitantes.save()
            messages.success(request, 'Visitante Registrado com Sucesso!')
            return redirect('contact:index')

        return render(
            request,
            'contact/visitantes/create.html',
            context,
        )

    context = {
        'form': VisitantesForm(),
        'form_action': form_action,
    }
    return render(
        request,
        'contact/visitantes/create.html',
        context,
    )

@porteiro_required
def create_eventos(request):
    form_action = reverse('contact:create_eventos')
    if request.method == 'POST':
        form_eventos = EventosForm(request.POST)

        context = {
            'form': form_action,
            'form_eventos': form_eventos
        }

        if form_eventos.is_valid():
            form_eventos.save()
            messages.success(request, 'Agendado com sucesso!')
            return redirect('contact:eventos')
        return render(
            request,
            'contact/eventos/create_eventos.html',
            context,
        )
    context = {
            'form': EventosForm(),
            'form_eventos': form_action,
    }
    return render(
        request,
        'contact/eventos/create_eventos.html',
        context,
    )

@porteiro_required
def visitanteIndexUpdate(request, visitante_id):
    visitante = get_object_or_404(Visitante, pk=visitante_id)

    form_action = reverse('contact:visitanteIndexUpdate', args=(visitante_id,))

    if request.method == 'POST':
        form_visitantes = VisitantesForm(request.POST, instance=visitante)

        context = {
            'form': form_visitantes,
            'form_action': form_action,
        }

        if form_visitantes.is_valid():
            id_visitante = form_visitantes.save()
            messages.success(request, 'Visitante Atualizado com sucesso!')
            return redirect('contact:visitanteIndex', visitante_id=id_visitante.pk)

        return render(
            request,
            'contact/visitantes/create.html',
            context,
        )

    context = {
        'form': VisitantesForm(instance=visitante),
        'form_action': form_action,
    }
    return render(
        request,
        'contact/visitantes/create.html',
        context,
    )

# Formulario de registro de visitantes
@porteiro_required
def create_registro_de_visitantes(request):
    form_action_registro_visitantes = reverse('contact:create_registro_de_visitantes')

    if request.method == 'POST':
        form_registro_visitantes = Registro_visitantesForm(request.POST, request.FILES)

        context = {
            'form': form_registro_visitantes,
            'form_action_registro_visitantes': form_action_registro_visitantes,
        }

        if form_registro_visitantes.is_valid():
            form_registro_visitantes.save()
            messages.success(request, 'Registro Cadastrado com sucesso!')
            messages.info(request, 'Agora cadastre no Visitante e coloque o ID do registro que você acabou de Registra')
            return redirect('contact:registro_visitantes_index')
            # return redirect('contact:visitanteIndexUpdate', visitante_id=visitante.pk)

        return render(
            request,
            'contact/registro_visitantes/create_registro_visitantes.html',
            context,
        )

    context = {
        'form': Registro_visitantesForm(),
        'form_action_registro_visitantes': form_action_registro_visitantes,
    }
    return render(
        request,
        'contact/registro_visitantes/create_registro_visitantes.html',
        context,
    )

# Formulario de update do registro de visitantes
@porteiro_required
def update_registro_de_visitantes(request, registro_id):
    registro = get_object_or_404(Registro_de_Visitante, pk=registro_id)

    form_action_registro_visitantes = reverse('contact:update_registro_de_visitantes', args=(registro_id,))

    if request.method == 'POST':
        form_registro_visitantes = Registro_visitantesForm(request.POST, request.FILES, instance=registro )
        context = {
            'form': form_registro_visitantes,
            'form_action_registro_visitantes': form_action_registro_visitantes,
        }
        if form_registro_visitantes.is_valid():
            id_resitro_visitante = form_registro_visitantes.save()
            messages.success(request, 'Atualizado com sucesso!')
            return redirect('contact:registro_visitantes_index_contato',registro_id = id_resitro_visitante.pk)
        return render(
            request,
            'contact/registro_visitantes/create_registro_visitantes.html',
            context,
        )
    context = {
        'form': Registro_visitantesForm(instance=registro),
        'form_action_registro_visitantes': form_action_registro_visitantes,
    }
    return render(
        request,
        'contact/registro_visitantes/create_registro_visitantes.html',
        context,
    )

@porteiro_required
def entregas(request):
    form_action_registro_entregas = reverse('contact:create_entregas')
    if request.method == 'POST':
        form_registro_entregas = Registros_de_EntregaForm(request.POST, request.FILES)
        context = {
            'form': form_action_registro_entregas,
            'form_registro_entregas': form_registro_entregas,
        }
        if form_registro_entregas.is_valid():
            form_registro_entregas.save()
            messages.success(request, 'Criado o Cadastrado com sucesso!')
            return redirect('contact:registro_entregas_index')
        return render(
                request,
                'contact/entregas/create_entregas.html',
                context,
            )
    context = {
        'form': Registros_de_EntregaForm(),
        'form_action_registro_entregas': form_action_registro_entregas,
    }
    return render(
        request,
        'contact/entregas/create_entregas.html',
        context,
    )

@porteiro_required
def update_entregas(request, entregas_id):
    entrega_update = get_object_or_404(Registros_de_Entrega, pk=entregas_id)

    form_action_registro_entregas = reverse('contact:update_entregas', args=(entregas_id,))

    if request.method == 'POST':
        form_registro_entregas = Registros_de_EntregaForm(request.POST, request.FILES, instance=entrega_update)

        context = {
            'form': form_action_registro_entregas,
            'form_registro_entregas': form_registro_entregas,
        }
        if form_registro_entregas.is_valid():
            id_entrega = form_registro_entregas.save()
            messages.success(request, 'Atualizado com sucesso!')
            return redirect('contact:registro_entregas_index_contato', entregas_id=id_entrega.pk )
        
        return render(
                request,
                'contact/entregas/create_entregas.html',
                context,
            )
    
    context = {
        'form': Registros_de_EntregaForm(instance=entrega_update),
        'form_action_registro_entregas': form_action_registro_entregas,
    }

    return render(
        request,
        'contact/entregas/create_entregas.html',
        context,
    )

@porteiro_required
def ocorrenciaIndex(request):
    form_action_ocorrecia = reverse('contact:ocorrenciaIndex')
    if request.method == 'POST':
        form_ocorrencia = OcorrenciaForm(request.POST)
        contex = {
            'form': form_action_ocorrecia,
            'form_ocorrencia' : form_ocorrencia,
        }
        if form_ocorrencia.is_valid():
            ocorrencia= form_ocorrencia.save(commit=False)
            ocorrencia.owner = request.user
            ocorrencia.save()
            messages.success(request, 'Criado com sucesso!')
            return redirect('contact:ocorrencias_index')
        return render(
            request,
            'contact/ocorrencias/create_livro.html',
            contex
        )
    context = {
        'form': OcorrenciaForm(),
        'form_action_ocorrecia': form_action_ocorrecia,
    }
    return render(
        request,
        'contact/ocorrencias/create_livro.html',
        context
    )

@porteiro_required
def ocorrenciaUpdate(request, id_ocorrencia):
    ocorrencia_update = get_object_or_404(Ocorrencia, pk=id_ocorrencia, owner=request.user)
    form_action_ocorrecia = reverse('contact:ocorrenciaUpdate', args=(id_ocorrencia,))
    if request.method == 'POST':
        form_ocorrencia = OcorrenciaForm(request.POST, instance = ocorrencia_update)
        contex = {
            'form': form_action_ocorrecia,
            'form_ocorrencia' : form_ocorrencia,
        }
        if form_ocorrencia.is_valid():
            ocorrencia = form_ocorrencia.save()
            messages.success(request, 'Atualizado com sucesso!')
            return redirect('contact:ocorrencias_index_id', id_ocorrencia=ocorrencia.pk)
        return render(
            request,
            'contact/ocorrencias/create_livro.html',
            contex
        )
    context = {
        'form': OcorrenciaForm( instance = ocorrencia_update),
        'form_action_ocorrecia': form_action_ocorrecia,
    }
    return render(
        request,
        'contact/ocorrencias/create_livro.html',
        context
    )

@porteiro_required
def update_eventos(request, eventos_id):
    update_eventos = get_object_or_404(Eventos, pk=eventos_id)
    form_action = reverse('contact:update_eventos', args=(eventos_id,))
    if request.method == 'POST':
        form_eventos = EventosForm(request.POST, instance =update_eventos )

        context = {
            'form': form_action,
            'form_eventos': form_eventos
        }

        if form_eventos.is_valid():
            eventos =  form_eventos.save()
            messages.success(request, 'Agendado Atualizado com sucesso!')
            return redirect('contact:eventos_id', eventos_id=eventos.pk)
        return render(
            request,
            'contact/eventos/create_eventos.html',
            context,
        )
    context = {
            'form': EventosForm(instance =update_eventos ),
            'form_eventos': form_action,
    }
    return render(
        request,
        'contact/eventos/create_eventos.html',
        context,
    )


def delete(request, eventos_id):
    update_eventos = get_object_or_404(Eventos, pk=eventos_id)
    
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        update_eventos.delete()
        return redirect('contact:eventos')

    return render(
        request,
        'contact/eventos/id_eventos.html',
        {
            'id_eventos':update_eventos,
            'confirmation':confirmation,
        }
    )