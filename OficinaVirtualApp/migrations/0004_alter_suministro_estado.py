# Generated by Django 3.2 on 2021-08-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OficinaVirtualApp', '0003_auto_20210808_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suministro',
            name='estado',
            field=models.CharField(choices=[('ACT', 'Activo'), ('SOL', 'Solicitado'), ('BJA', 'Baja'), ('DES', 'Desconectado')], max_length=3),
        ),
    ]