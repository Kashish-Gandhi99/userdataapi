# Generated by Django 3.0.6 on 2020-06-20 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_user_useractivity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='main.User'),
        ),
    ]