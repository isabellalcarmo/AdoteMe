from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from ..models import Unidade, Animal

from adoteme.forms.forms_animal import AnimalForm


@login_required
@permission_required('adoteme.add_animal')
def criar_animal(request, unidade_id):
    unidade_atual = Unidade.objects.filter(unidade_id=unidade_id).first()
    usuario_atual = request.user

    if request.method == 'POST':
        form = AnimalForm(request.POST, auto_id=True)
        if form.is_valid():
            animal = Animal(
                unidade = unidade_atual,
                nome_animal = form.cleaned_data['nome_animal'],
                descricao_animal = form.cleaned_data['descricao_animal'],
                tipo_animal = form.cleaned_data['tipo_animal'],
                raca_animal = form.cleaned_data['raca_animal']
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
    animal = get_object_or_404(Animal, animal_id=animal_id)
    unidade_id = animal.unidade.unidade_id
    animal.delete()
    messages.add_message(request, messages.INFO, _('Animal deletado com sucesso!\n'))

    return redirect(reverse('visualizar_unidade', args=[animal.unidade.unidade_id]))


@login_required
@permission_required('adoteme.change_animal')
def editar_animal(request, animal_id):
    animal = get_object_or_404(Animal, animal_id=animal_id)

    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            animal = form.save()
            animal.save()
            messages.add_message(request, messages.INFO, _('Animal editado com sucesso!\n'))

            return redirect(reverse('visualizar_unidade',args=[animal.unidade.unidade_id]))

    form = AnimalForm(instance=animal)

    context = {
        'form': form,
        'animal_id': animal_id,
        'unidade_id': animal.unidade.unidade_id
    }
    return render(request, 'animais/editar_animal.html', context)
