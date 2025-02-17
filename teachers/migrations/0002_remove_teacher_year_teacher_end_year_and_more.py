# Generated by Django 5.1.6 on 2025-02-14 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='year',
        ),
        migrations.AddField(
            model_name='teacher',
            name='end_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='start_year',
            field=models.IntegerField(null=True),
        ),
    ]
