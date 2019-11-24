# Generated by Django 2.2.7 on 2019-11-21 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(help_text='Ej. César', max_length=50)),
                ('Apellidos', models.CharField(help_text='Ej. Orellana', max_length=50)),
                ('CorreoElectronico', models.CharField(help_text='Ej. ce.orellanaa@alumnos.duoc.cl', max_length=50)),
                ('Direccion', models.CharField(help_text='Antonio Varas 666', max_length=50)),
                ('Ciudad', models.CharField(help_text='Providencia', max_length=500)),
                ('Pais', models.CharField(help_text='Chile', max_length=500)),
                ('CodigoPostal', models.CharField(help_text='8640000', max_length=500)),
                ('Telefono', models.CharField(help_text='+5692222222', max_length=500)),
            ],
        ),
    ]