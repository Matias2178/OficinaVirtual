# Generated by Django 3.2 on 2021-08-05 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AvisosAlertasApp', '0003_alter_aviso_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerta',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
