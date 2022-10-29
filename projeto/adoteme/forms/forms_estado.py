from django import forms
from django.core.exceptions import ValidationError
from ..models import Estado


ESTADOS_BRASILEIROS = (
    ('Acre', 'Acre'),
    ('Alagoas', 'Alagoas'), 
    ('Amapá', 'Amapá'), 
    ('Amazonas', 'Amazonas'),
    ('Bahia', 'Bahia'), 
    ('Ceará', 'Ceará'), 
    ('Distrito Federal', 'Distrito Federal'), 
    ('Espírito Santo', 'Espírito Santo'),
    ('Goiás', 'Goiás'), 
    ('Maranhão', 'Maranhão'), 
    ('Mato Grosso', 'Mato Grosso'), 
    ('Mato Grosso do Sul', 'Mato Grosso do Sul'),
    ('Minas Gerais', 'Minas Gerais'), 
    ('Pará', 'Pará'), 
    ('Paraíba', 'Paraíba'), 
    ('Paraná', 'Paraná'),
    ('Pernambuco', 'Pernambuco'), 
    ('Piauí', 'Piauí'), 
    ('Rio de Janeiro', 'Rio de Janeiro'), 
    ('Rio Grande do Norte', 'Rio Grande do Norte'),
    ('Rio Grande do Sul', 'Rio Grande do Sul'), 
    ('Rondônia', 'Rondônia'), ('Roraima', 'Roraima'), 
    ('Santa Catarina', 'Santa Catarina'),
    ('São Paulo', 'São Paulo'), 
    ('Sergipe', 'Sergipe'), ('Tocantins', 'Tocantins')
)

class EstadoForm(forms.ModelForm):
    nome_estado = forms.ChoiceField(choices=ESTADOS_BRASILEIROS, widget=forms.Select(attrs={'class': 'form-control'}), initial='Rio de Janeiro')

    def clean_estado(self):
        cleaned_data = super().clean()
        nome_estado = cleaned_data.get('nome_estado')

        if Estado.objects.filter(nome_estado=nome_estado).count() > 0:
            raise ValidationError(_('Este Estado já existe.'))

        return nome_estado

    class Meta:
        model = Estado
        exclude = ['estado_id']