# Generated by Django 5.1.6 on 2025-03-06 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_categoria_banner_categoria_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': ['variedades_activas'], 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.RemoveField(
            model_name='produto',
            name='epoca_colheita_produto',
        ),
        migrations.AddField(
            model_name='produto',
            name='numero_variedades',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='produto',
            name='proximas_colhetas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='produto',
            name='variedades_activas',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
