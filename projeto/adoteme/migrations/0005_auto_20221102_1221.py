# Generated by Django 3.2.5 on 2022-11-02 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adoteme', '0004_animal_raca_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='listaadocao',
            name='adotado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='listaadocao',
            name='adotante',
            field=models.ForeignKey(db_column='fk_adotante_id', on_delete=django.db.models.deletion.CASCADE, related_name='lista_adotante_fk', to=settings.AUTH_USER_MODEL),
        ),
    ]