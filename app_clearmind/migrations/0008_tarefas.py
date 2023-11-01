# Generated by Django 4.2.6 on 2023-11-01 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_clearmind', '0007_alter_listas_titulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('data', models.CharField(default='', max_length=100)),
                ('lista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_clearmind.listas')),
            ],
        ),
    ]
