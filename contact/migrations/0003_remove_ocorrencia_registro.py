# Generated by Django 5.1.4 on 2025-01-22 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_visitante_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ocorrencia',
            name='registro',
        ),
    ]
