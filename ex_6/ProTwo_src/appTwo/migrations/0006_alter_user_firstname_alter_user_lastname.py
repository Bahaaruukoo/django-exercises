# Generated by Django 4.0.1 on 2022-01-15 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0005_user_delete_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(max_length=256),
        ),
    ]
