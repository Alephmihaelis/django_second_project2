# Generated by Django 5.1.3 on 2024-11-11 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='conteudo',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='data_expiracao',
            new_name='expiration',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='imagem',
            new_name='image',
        ),
    ]
