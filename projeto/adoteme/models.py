from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11)

class Estado(models.Model):
    estado_id = models.AutoField(primary_key=True)
    nome_estado = models.CharField(max_length=100, unique=True, error_messages={'unique': 'O Estado em questão já foi registrado.'})

class Unidade(models.Model):
    unidade_id = models.AutoField(primary_key=True)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE, db_column='fk_estado_id', related_name='unidade_estado_fk')
    responsavel = models.ForeignKey('Usuario',on_delete=models.CASCADE, db_column='fk_responsavel_id', related_name='unidade_responsavel_fk')
    nome_unidade = models.CharField(max_length=200, blank=True, null=True)
    telefone_unidade = models.CharField(max_length=20, blank=True, null=True)
    descricao_unidade = models.CharField(max_length=200, blank=True, null=True)

class Animal(models.Model):
    animal_id = models.AutoField(primary_key=True)
    unidade = models.ForeignKey('Unidade',on_delete=models.CASCADE, db_column='fk_unidade_id', related_name='animal_unidade_fk')
    nome_animal = models.CharField(max_length=100, blank=True, null=True)
    tipo_animal = models.CharField(max_length=100, blank=True, null=True)
    descricao_animal = models.CharField(max_length=200, blank=True, null=True)

class ListaAdocao(models.Model):
    lista_id = models.AutoField(primary_key=True)
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE, db_column='fk_animal_id', related_name='lista_animal_fk')
    adotante = models.ForeignKey('Usuario',on_delete=models.CASCADE, db_column='fk_responsavel_id', related_name='lista_responsavel_fk')

    class Meta:
        unique_together = ('animal', 'adotante')

