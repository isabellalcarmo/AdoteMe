from django import forms

from ..models import Animal


class AnimalForm(forms.ModelForm):
    nome_animal = forms.CharField(label='Nome do Animal', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_animal = forms.CharField(label='Tipo do Animal', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    raca_animal = forms.CharField(label='Raça do Animal', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao_animal = forms.CharField(label='Sobre o Animal', required=False,  widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}))

    class Meta:
        model = Animal
        exclude = ['animal_id', 'unidade']

class AnimalForm_edit(forms.ModelForm):
    nome_animal = forms.CharField(label='Nome do Animal', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_animal = forms.CharField(label='Tipo do Animal', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    raca_animal = forms.CharField(label='Raça do Animal', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao_animal = forms.CharField(label='Sobre o Animal', required=False,  widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}))

    class Meta:
        model = Animal
        exclude = ['animal_id', 'unidade']
