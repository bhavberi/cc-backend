# Generated by Django 3.2.6 on 2022-03-24 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
