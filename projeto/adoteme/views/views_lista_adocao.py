from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from ..models import ListaAdocao, Animal


@login_required
def adicionar_animal_lista(request, animal_id):
    animal = get_object_or_404(Animal, animal_id=animal_id)

    if ListaAdocao.objects.filter(adotante=request.user, animal=animal).exists():
        messages.add_message(request, messages.INFO, _('Animal já está na sua lista de adoção!\n'))
        return redirect(reverse('lista_adocao'))

    animal_lista = ListaAdocao(
        adotante = request.user,
        animal = animal,
    )
    animal_lista.save()

    messages.add_message(request, messages.INFO, _('Animal adicionado à sua lista de adoção!\n'))
    return redirect(reverse('lista_adocao'))


@login_required
def deletar_animal_lista(request, animal_id):
    animal_lista = ListaAdocao.objects.filter(adotante=request.user, animal__animal_id=animal_id).first()
    if not animal_lista:
        return HttpResponseNotFound()

    animal_lista.delete()
    messages.add_message(request, messages.INFO, _('Animal deletado da lista de adoção com sucesso!\n'))

    return redirect(reverse('lista_adocao'))


@login_required
def visualizar_lista_adocao(request):
    animais_lista = ListaAdocao.objects.filter(adotante=request.user)

    context = {
        'animais_lista': animais_lista
    }
    return render(request, 'lista_adocao/visualizar_lista_adocao.html', context=context)


@login_required
def lista_adocao_animal(request, animal_id):
    animal = get_object_or_404(Animal, animal_id=animal_id)
    unidade_id = animal.unidade.unidade_id

    animal_lista = ListaAdocao.objects.filter(animal=animal).all()

    context = {
        'animal': animal,
        'animal_lista': animal_lista
    }

    return render(request, 'animais/lista_adocao_animal.html', context=context)