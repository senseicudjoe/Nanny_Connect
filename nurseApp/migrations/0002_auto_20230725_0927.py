# Generated by Django 3.2 on 2023-07-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurseApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurse',
            name='end_work',
        ),
        migrations.RemoveField(
            model_name='nurse',
            name='start_work',
        ),
        migrations.AddField(
            model_name='nurse',
            name='bio',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='nurse',
            name='day_shift',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nurse',
            name='night_shift',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
