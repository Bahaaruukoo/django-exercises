# Generated by Django 4.0.1 on 2022-01-15 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0002_alter_users_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='firstname',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='users',
            name='lastname',
            field=models.CharField(max_length=120),
        ),
    ]
