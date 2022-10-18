# Generated by Django 4.1 on 2022-10-18 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feriavirtualapp', '0017_alter_post_estadosolicitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rol',
            field=models.CharField(choices=[('1', 'Productor'), ('2', 'Cliente externo'), ('3', 'Cliente interno'), ('4', 'Transportista'), ('5', 'Consultor'), ('6', 'Administrador'), ('7', 'Revisor de calidad')], max_length=50, null=True),
        ),
    ]
