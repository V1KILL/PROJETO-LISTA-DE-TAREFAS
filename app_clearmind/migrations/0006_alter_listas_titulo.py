# Generated by Django 4.2.6 on 2023-10-31 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_clearmind', '0005_listas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listas',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
