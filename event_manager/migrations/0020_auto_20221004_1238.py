# Generated by Django 3.2.6 on 2022-10-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_manager', '0019_alter_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='additional',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='equipment',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
