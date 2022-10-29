from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from ..models import Estado
from adoteme.forms.forms_estado import EstadoForm


def lista_estados(request):
    estados = Estado.objects.all()

    context = {
        "estados": estados
    }

    return render(request, "estados/lista_estados.html", context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def criar_estado(request):
    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            estado = form.save()
            estado.save()
            form = EstadoForm()
            messages.add_message(request, messages.INFO, _('Estado criado com sucesso!\n'))
            return redirect(reverse('lista_estados'))
    else:
        form = EstadoForm()

    context = {
        'form': form
    }

    return render(request, "estados/criar_estado.html", context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def deletar_estado(request, estado_id):
    estado = get_object_or_404(Estado, estado_id=estado_id)
    estado.delete()
    messages.add_message(request, messages.INFO, _('Estado deletado com sucesso!\n'))

    return redirect(reverse('lista_estados'))