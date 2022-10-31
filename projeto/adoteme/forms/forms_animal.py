from django import forms


class AnimalForm(forms.Form):
    nome_animal = forms.CharField(label='Nome do Animal', widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_animal = forms.CharField(label='Tipo do Animal', widget=forms.TextInput(attrs={'class': 'form-control'}))
    descrição_animal = forms.CharField(label='Sobre o Animal', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}))


