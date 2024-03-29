# Generated by Django 4.0.3 on 2022-04-25 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_user_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='modul_druga_zelja',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='modul_prva_zelja',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='modul_score',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='indeks',
            field=models.CharField(default='raXX/YYYY', max_length=15),
        ),
    ]
