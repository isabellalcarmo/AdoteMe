from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from ..models import Estado, Unidade, Usuario, Animal, ListaAdocao

from adoteme.forms.forms_unidade import UnidadeForm


def lista_unidades(request, estado_id):
    unidades = Unidade.objects.filter(estado=estado_id).all()
    estado_atual = Estado.objects.filter(estado_id=estado_id).first()

    context = {
        'unidades': unidades,
        'estado_id': estado_id,
        'estado_atual': estado_atual
    }

    return render(request, "unidades/lista_unidades.html", context)


@login_required
@permission_required('adoteme.add_unidade')
def criar_unidade(request, estado_id):
    estado_atual = Estado.objects.filter(estado_id=estado_id).first()
    usuario_atual = request.user

    if request.method == 'POST':
        form = UnidadeForm(request.POST, auto_id=True)
        if form.is_valid():
            unidade = Unidade(
                estado = estado_atual,
                responsavel = usuario_atual,
                nome_unidade = form.cleaned_data['nome_unidade'],
                telefone_unidade = form.cleaned_data['telefone_unidade'],
                descricao_unidade = form.cleaned_data['descricao_unidade']
            )
        try:
            unidade.save()
            messages.add_message(request, messages.INFO, _('Unidade criada com sucesso!\n'))
            return redirect(reverse('lista_unidades', args=[estado_id]))
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, _("Não foi possível criar a Unidade"))

    else:
        form = UnidadeForm()

    context = {
        'form': form,
        'estado_id': estado_id
    }

    return render(request, "unidades/criar_unidade.html", context)


@login_required
@permission_required('adoteme.delete_unidade')
def deletar_unidade(request, unidade_id):
    unidade = get_object_or_404(Unidade, unidade_id=unidade_id)
    estado_id = unidade.estado.estado_id
    unidade.delete()
    messages.add_message(request, messages.INFO, _('Unidade deletada com sucesso!\n'))

    return redirect(reverse('lista_unidades', args=[estado_id]))


@login_required
@permission_required('adoteme.change_unidade')
def editar_unidade(request, unidade_id):
    unidade = get_object_or_404(Unidade, unidade_id=unidade_id)

    if request.method == 'POST':
        form = UnidadeForm(request.POST, instance=unidade)
        if form.is_valid():
            unidade = form.save()
            unidade.save()
            messages.add_message(request, messages.INFO, _('Unidade editada com sucesso!\n'))

            return redirect(reverse('lista_unidades',args=[unidade.estado.estado_id]))

    form = UnidadeForm(instance=unidade)

    context = {
        'form': form,
        'unidade_id': unidade_id,
        'estado_id': unidade.estado.estado_id
    }
    return render(request, 'unidades/editar_unidade.html', context)


def visualizar_unidade(request, unidade_id):
    unidade = get_object_or_404(Unidade, unidade_id=unidade_id)
    animais = Animal.objects.filter(unidade=unidade_id, adotado=False).all()
    animais_lista_adotados = ListaAdocao.objects.filter(adotante=request.user, adotante_adotou=True, animal__unidade__unidade_id=unidade_id).all()

    if animais_lista_adotados.count() == 0:
        animais_lista_adotados == False

    context = {
        'unidade': unidade,
        'animais': animais,
        'animais_lista_adotados': animais_lista_adotados,
    }

    return render(request, "unidades/visualizar_unidade.html", context)


@login_required
@permission_required('adoteme.change_unidade')
def minhas_unidades(request, responsavel_id):
    unidades = Unidade.objects.filter(responsavel=responsavel_id).all()
    responsavel_unidades = Usuario.objects.filter(id=responsavel_id).first()

    context = {
        'unidades': unidades,
        'responsavel_unidades': responsavel_unidades
    }

    return render(request, "unidades/minhas_unidades.html", context)