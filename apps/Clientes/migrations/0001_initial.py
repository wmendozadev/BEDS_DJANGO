# Generated by Django 3.0.8 on 2020-07-26 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnombre', models.CharField(max_length=50)),
                ('snombre', models.CharField(max_length=50)),
                ('pape', models.CharField(max_length=50)),
                ('sape', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=300)),
                ('celular', models.CharField(max_length=8)),
                ('activo', models.BooleanField()),
            ],
        ),
    ]
