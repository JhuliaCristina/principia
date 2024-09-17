# Generated by Django 5.1.1 on 2024-09-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cpf',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nome_completo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='telefone',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
