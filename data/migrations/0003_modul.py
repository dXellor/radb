# Generated by Django 4.0.3 on 2022-05-19 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puno_ime', models.CharField(max_length=50)),
                ('skracenica', models.CharField(max_length=10)),
                ('broj_mesta', models.IntegerField()),
            ],
        ),
    ]
