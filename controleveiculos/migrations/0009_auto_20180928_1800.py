# Generated by Django 2.1.1 on 2018-09-28 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controleveiculos', '0008_seguro_veiculo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seguro',
            old_name='Veiculo',
            new_name='Veículo',
        ),
        migrations.RenameField(
            model_name='veiculo',
            old_name='pertence',
            new_name='pertence_a',
        ),
    ]
