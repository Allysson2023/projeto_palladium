# Generated by Django 5.1.4 on 2025-01-23 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_apartamento_numero_apartamento_eventos'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='tipo_de_evento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
