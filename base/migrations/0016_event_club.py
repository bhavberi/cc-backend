# Generated by Django 3.0.6 on 2020-06-16 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_auto_20200609_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='club',
            field=models.CharField(default='vishva.saravanan@research.iiit.ac.in', max_length=250),
            preserve_default=False,
        ),
    ]
