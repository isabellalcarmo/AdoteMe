from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from ..models import Unidade


class UnidadeForm(forms.ModelForm):
    nome_unidade = forms.CharField(label='Nome da Unidade', widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(label='Sobre a Unidade', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}))
    numero_barraca = forms.CharField(label='Número da Barraca', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone_unidade = forms.CharField(label='Telefone da Unidade', widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_telefone_unidade(self):
        tel = self.cleaned_data['telefone_unidade']
        validator = RegexValidator(r"^(\(\+?55\)|\+?55)?(\(0?[0-9]{2}\)|0?[0-9]{2})?\s?[0-9]{4,5}\-?[0-9]{4}$")
        try:
            validator(tel)
        except Exception as e:
            print(e)
            raise ValidationError(_('Número de telefone inválido.'))

        return tel

    class Meta:
        model = Unidade
        exclude = ['unidade_id', 'estado', 'responsavel']