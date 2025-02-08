from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegistrorUpadateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from functools import wraps


# Decorador para restringir acesso apenas a porteiros
def porteiro_required(view_func):
    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.groups.filter(name="porteiro").exists():  # Verifica se o usuário está no grupo 'porteiro'
            messages.error(request, 'Acesso negado! Apenas porteiros podem acessar esta área.')
            return redirect('contact:login_views')  # Redireciona para login se não for porteiro
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view


@porteiro_required
def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado com sucesso!')
            return redirect('contact:index')


    return render(
        request,
        'contact/user/register.html',
        {
            'form':form
        }
    )

@porteiro_required
def user_update(request):
    form = RegistrorUpadateForm(instance=request.user)

    if request.method != 'POST':
        return render(
        request,
        'contact/user/register.html',
            {
               'form':form
            }
        )
    
    form = RegistrorUpadateForm(data=request.POST , instance=request.user)

    if not form.is_valid():
        return render(
        request,
        'contact/user/register.html',
            {
               'form':form
            }
        )
    form.save()
    messages.success(request, 'Seu perfil foi atualizado com sucesso!')
    return redirect('contact:user_update')

def login_views(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)

            if user.groups.filter(name="porteiro").exists():  # Verifica se o usuário pertence ao grupo 'porteiro'
                messages.success(request, 'Bem-vindo ao sistema da portaria!')
                return redirect('contact:index')  # Redirecione para a página inicial da portaria

            messages.error(request, 'Acesso negado! Apenas porteiros podem acessar esta área.')
            auth.logout(request)
            return redirect('contact:login_views')  # Se não for porteiro, faz logout e redireciona

        messages.error(request, 'Login inválido')

    return render(
        request,
        'contact/user/login.html',
        {
            'form': form
        }
    )

@porteiro_required
def logaut_views(request):
    auth.logout(request)
    messages.info(request, 'Você saiu do Sistema!')
    return redirect('contact:login_views')