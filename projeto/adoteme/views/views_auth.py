from django.contrib.auth import views
from django.urls import reverse
from django.shortcuts import render
from django.utils.translation import gettext_lazy
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse

from adoteme.models import Usuario

from adoteme.forms.forms_auth import RegisterUserForm


def register_user(request):
    grupo_veterinario = Group.objects.get(name='Veterinário')
    grupo_cliente = Group.objects.get(name='Cliente')

    if request.method == 'POST':
        form = RegisterUserForm(request.POST, auto_id=True)

        if form.is_valid():
            usuario = Usuario.objects.create_user(
                is_active=True,
                is_staff=False,
                is_superuser=False,

                username=form.cleaned_data['usuario'],
                password=form.cleaned_data['senha'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['nome'],
                last_name=form.cleaned_data['sobrenome'],
                cpf = form.cleaned_data['cpf']
            )
            try:
                usuario.save()
                if form.cleaned_data['tipo_usuario'] == 'Veterinário':
                    grupo_veterinario.user_set.add(usuario)
                if form.cleaned_data['tipo_usuario'] == 'Cliente':
                    grupo_cliente.user_set.add(usuario)
                return redirect(reverse('registration_done'))
            except Exception as e:
                print(e)
                pass
    else:
        form = RegisterUserForm()

    context = {
        'form': form
    }

    return render(request, 'registration/register.html', context)


def user_registration_done(request):
    return render(request, 'registration/registration_done.html')


def redirect_login(request):
    return render(request, 'index.html')