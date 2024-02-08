# Generated by Django 4.1 on 2024-02-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoira',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALAXI', 'Galaxia'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
    ]
