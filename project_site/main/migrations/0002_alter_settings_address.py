# Generated by Django 5.1.2 on 2024-10-19 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
    ]
