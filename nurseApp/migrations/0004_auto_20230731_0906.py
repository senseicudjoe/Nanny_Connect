# Generated by Django 3.2 on 2023-07-31 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurseApp', '0003_auto_20230727_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurse',
            name='DoB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]