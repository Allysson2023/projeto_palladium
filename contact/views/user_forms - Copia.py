from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegistrorUpadateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='contact:login_views')
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
@login_required(login_url='contact:login_views')
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
            messages.success(request, 'Bem Vindo ao Sistema Patrimonial!')
            return redirect('contact:index')

        messages.error(request, 'Login inválido')

    return render(
        request,
        'contact/user/login.html',
        {
            'form':form
        }
    )

@login_required(login_url='contact:login_views')
def logaut_views(request):
    auth.logout(request)
    messages.info(request, 'Você saiu do Sistema!')
    return redirect('contact:login_views')