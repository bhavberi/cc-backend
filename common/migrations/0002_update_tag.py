# Generated by Django 3.0.6 on 2020-09-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='tag',
            field=models.CharField(choices=[['normal', 'NORMAL'], ['reminder', 'REMINDER'], ['important', 'IMPORTANT']], default='normal', max_length=50),
        ),
    ]
