# Generated by Django 3.0.6 on 2020-06-20 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20200620_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useractivity',
            options={'ordering': ['id']},
        ),
    ]