# Generated by Django 3.0.6 on 2020-06-20 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_user_useractivity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Useractivity',
        ),
    ]
