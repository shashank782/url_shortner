# Generated by Django 4.1.7 on 2023-08-31 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_url', models.CharField(max_length=400, unique=True)),
                ('S_url', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
