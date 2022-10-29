from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django import forms

from adoteme.models import Usuario

import re


# https://pt.stackoverflow.com/questions/64608/como-validar-e-calcular-o-d%C3%ADgito-de-controle-de-um-cpf
def validate_cpf(cpf):
    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        print("bbbbbbbbbbbbb")
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        print("ccccccccccccccc")
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        print("dddddddddddddd")
        return False

    return True


TIPO_USUARIO = (
    ('Veterinário', 'Veterinário'),
    ('Cliente','Cliente')
)

class RegisterUserForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sobrenome = forms.CharField(label='Sobrenome', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(label='CPF',required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), min_length=11, max_length=11)
    usuario = forms.CharField(label='Nome de Usuário', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[RegexValidator(regex=r'^[A-Za-z\d]+$', message='Seu usuário deve conter apenas letras ou números.')])
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirmar_senha = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    tipo_usuario = forms.ChoiceField(label='Tipo de Usuário', choices=TIPO_USUARIO, widget=forms.Select(attrs={'class': 'form-control'}))

    def clean_cpf(self):

        cpf = self.cleaned_data['cpf']

        if not cpf.isnumeric():
            raise ValidationError(_('Erro de inserção de CPF, insira apenas números'))
        elif not(validate_cpf(cpf)):
            raise ValidationError('CPF inválido')
        elif Usuario.objects.filter(cpf=cpf).count() > 0:
            raise ValidationError(_('Este CPF já está associado a um usuário.'))
        else:
            return cpf

    def clean_usuario(self):
        cleaned_data = super().clean()
        usuario = cleaned_data.get('usuario')

        if len(cleaned_data.get('usuario')) < 5:
            raise ValidationError(_('Seu nome de usuário deve ter pelo menos 5 caracteres.'))

        if Usuario.objects.filter(username=usuario).count() > 0:
            raise ValidationError(_('Este usuário já existe.'))

        return usuario

    def clean_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if Usuario.objects.filter(email=email).count() > 0:
            raise ValidationError(_('Este e-mail já está associado a um usuário.'))

        return email

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('senha')
        pass2 = cleaned_data.get('confirmar_senha')

        if pass1 is not None and pass1 != pass2:
            self.add_error('confirmar_senha', 'As senhas não correspondem.')


class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.CharField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'id': 'id_email'}))