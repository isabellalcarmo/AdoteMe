from django import forms

from ..models import ListaAdocao


class ListaAdocaoForm(forms.ModelForm):
    motivo_adocao = forms.CharField(label='Sobre o Animal', required=True,  widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}))
    justificativa_viagem = forms.CharField(label='Sobre o Animal', required=True,  widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}))
    posse_animal = forms.CharField(label='Sobre o Animal', required=True,  widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}))

    class Meta:
        model = ListaAdocao
        exclude = ['lista_id', 'animal', 'adotante', 'adotante_adotou']
