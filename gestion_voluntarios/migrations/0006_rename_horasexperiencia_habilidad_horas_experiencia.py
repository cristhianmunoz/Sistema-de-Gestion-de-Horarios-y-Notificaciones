# Generated by Django 4.1.7 on 2023-03-02 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_voluntarios', '0005_voluntario_edad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habilidad',
            old_name='horasExperiencia',
            new_name='horas_experiencia',
        ),
    ]
