from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from ..models import ListaAdocao, Animal, Unidade

from adoteme.forms.forms_lista_adocao import ListaAdocaoForm


@login_required
def adicionar_animal_lista(request, animal_id):
    animal = get_object_or_404(Animal, animal_id=animal_id)
    usuario_atual = request.user

    if ListaAdocao.objects.filter(adotante=request.user, animal=animal).exists():
        messages.add_message(request, messages.INFO, _('Animal já está na sua lista de adoção!\n'))
        return redirect(reverse('lista_adocao'))
    else:
        if request.method == 'POST':
            form = ListaAdocaoForm(request.POST, auto_id=True)
            if form.is_valid():
                lista_adocao = ListaAdocao(
                    animal = animal,
                    adotante = usuario_atual,
                    adotante_adotou = False,
                    motivo_adocao = form.cleaned_data['motivo_adocao'],
                    justificativa_viagem = form.cleaned_data['justificativa_viagem'],
                    posse_animal = form.cleaned_data['posse_animal']
            )
            try:
                lista_adocao.save()
                messages.add_message(request, messages.INFO, _('Animal adicionado à sua lista de adoção!\n'))
                return redirect(reverse('lista_adocao'))
            except Exception as e:
                print(e)
                messages.add_message(request, messages.ERROR, _("Não foi possível adicionar o animal à sua lista de adoção.\n"))
        else:
            form = ListaAdocaoForm()

    context = {
        'form': form,
        'animal_id': animal_id
    }

    return render(request, 'lista_adocao/adicionar_animal_lista_adocao.html', context=context)


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
    animais_lista_nao_adotados = ListaAdocao.objects.filter(adotante=request.user, adotante_adotou=False)
    animais_lista_adotados = ListaAdocao.objects.filter(adotante=request.user, adotante_adotou=True)

    context = {
        'animais_lista_nao_adotados': animais_lista_nao_adotados,
        'animais_lista_adotados': animais_lista_adotados
    }
    return render(request, 'lista_adocao/visualizar_lista_adocao.html', context=context)


@login_required
def visualizar_lista_adotados(request, unidade_id):
    animais_lista_adotados = ListaAdocao.objects.filter(adotante_adotou=True, animal__unidade__unidade_id=unidade_id).all()

    context = {
        'animais_lista_adotados': animais_lista_adotados,
        'unidade_id': unidade_id,
        'nome_unidade': animais_lista_adotados[0].animal.unidade.nome_unidade
    }
    return render(request, 'lista_adocao/visualizar_lista_adotados.html', context=context)


@login_required
def lista_adocao_animal(request, animal_id):
    animal = get_object_or_404(Animal, animal_id=animal_id)

    animal_lista = ListaAdocao.objects.filter(animal=animal).all()

    context = {
        'animal': animal,
        'animal_lista': animal_lista
    }

    return render(request, 'animais/lista_adocao_animal.html', context=context)


@login_required
def aprovar_adocao_animal(request, animal_id, usuario_id):
    animal = get_object_or_404(Animal, animal_id=animal_id)

    animal_lista = ListaAdocao.objects.filter(animal=animal, adotante__id=usuario_id).first()

    animal_lista.adotante_adotou = True
    animal.adotado = True

    animal.save()
    animal_lista.save()

    messages.add_message(request, messages.INFO, _('O animal foi adotado com sucesso!\n'))

    return redirect(reverse('visualizar_unidade',args=[animal.unidade.unidade_id]))