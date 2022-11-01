from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from ..models import Unidade, Animal

from adoteme.forms.forms_animal import AnimalForm, AnimalForm_edit


def lista_animais(request, unidade_id):
    unidade = Unidade.objects.filter(unidade_id=unidade_id).all()
    animais = Animal.objects.filter(unidade=unidade).all()

    context = {
        'unidade': unidade,
        'animais': animais,
    }

    return render(request, "animais/lista_animais.html", context)


@login_required
@permission_required('adoteme.add_animal')
def criar_animal(request, unidade_id):
    unidade_atual = Unidade.objects.filter(unidade_id=unidade_id).values('estado')
    # estado_id = unidade_atual[0]['estado']

    if request.method == 'POST':
        form = AnimalForm(request.POST, auto_id=True)
        if form.is_valid():
            animal = Animal(
                nome_animal = form.cleaned_data['nome_animal'],
                descricao_animal = form.cleaned_data['descricao_animal'],
                tipo_animal = form.cleaned_data['tipo_animal'],
                # raca = form.cleaned_data['raca'],
                unidade = unidade_id,
            )
        try:
            animal.save()
            messages.add_message(request, messages.INFO, _('Animal criado com sucesso!\n'))
            return redirect(reverse('visualizar_unidade', args=[unidade_id]))
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, _("Não foi possível criar o Animal"))

    else:
        form = AnimalForm()

    context = {
        'form': form,
        'unidade_id': unidade_id,
    }

    return render(request, "animais/criar_animal.html", context)


@login_required
@permission_required('adoteme.delete_animal')
def deletar_animal(request, animal_id):
    animal = get_object_or_404(Animal, unidade_id=animal_id)
    animal.delete()
    messages.add_message(request, messages.INFO, _('Animal deletada com sucesso!\n'))

    return redirect(reverse('lista_animais'))


@login_required
@permission_required('adoteme.change_animal')
def editar_animal(request, animal_id):
    animal = get_object_or_404(Animal, animal_id=animal_id)

    if request.method == 'POST':
        form = AnimalForm_edit(request.POST, instance=animal)
        if form.is_valid():
            animal = form.save()
            animal.save()
            messages.add_message(request, messages.INFO, _('Animal editada com sucesso!\n'))

            return redirect(reverse('visualizar_unidade',args=[animal.unidade.unidade_id]))

    form = AnimalForm_edit(instance=animal)

    context = {
        'form': form,
        'animal_id': animal_id,
        'unidade_id': animal.unidade.unidade_id
    }
    return render(request, 'animais/editar_animal.html', context)


# def visualizar_unidade(request, unidade_id):
#     unidade = get_object_or_404(Unidade, unidade_id=unidade_id)
#     animais = Animal.objects.filter(unidade=unidade_id)

#     context = {
#         'unidade': unidade,
#         'animais': animais,
#     }

#     return render(request, "unidades/visualizar_unidade.html", context)


# @login_required
# @permission_required('adoteme.change_animal')
# def meus_animais(request, responsavel_id):
#     unidades = Unidade.objects.filter(responsavel=responsavel_id).all()
#     responsavel_unidades = Usuario.objects.filter(id=responsavel_id).first()

#     context = {
#         'unidades': unidades,
#         'responsavel_unidades': responsavel_unidades
#     }

#     return render(request, "unidades/minhas_unidades.html", context)