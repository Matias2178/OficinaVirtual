# Generated by Django 3.2 on 2021-08-08 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('OficinaVirtualApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suministro', models.IntegerField()),
                ('factura', models.CharField(max_length=20)),
                ('fecha_pago', models.DateField()),
                ('importe', models.CharField(max_length=20)),
                ('medio_pago', models.CharField(max_length=20)),
                ('operacion', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OficinaVirtualApp.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Debito_Automatico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarjeta', models.CharField(max_length=20)),
                ('banco', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=80)),
                ('vencimiento', models.DateField()),
                ('estado', models.CharField(max_length=20)),
                ('suministro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OficinaVirtualApp.suministro')),
            ],
        ),
        migrations.CreateModel(
            name='Boton_Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_emision', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
                ('importe', models.CharField(max_length=10)),
                ('fecha_pago', models.DateField()),
                ('medio_pago', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=10)),
                ('suministro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OficinaVirtualApp.suministro')),
            ],
        ),
    ]
