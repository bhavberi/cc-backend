# Generated by Django 3.0.6 on 2020-09-11 20:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('organizers', '0003_budgetproposal_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('creator', models.CharField(max_length=250)),
            ],
        ),
    ]
