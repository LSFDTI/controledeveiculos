# Generated by Django 2.1.1 on 2018-09-28 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controleveiculos', '0007_veiculo_pertence'),
    ]

    operations = [
        migrations.AddField(
            model_name='seguro',
            name='Veiculo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='controleveiculos.Veiculo'),
            preserve_default=False,
        ),
    ]