# Generated by Django 3.0.3 on 2020-04-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_transhis_transdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transhis',
            name='transDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]