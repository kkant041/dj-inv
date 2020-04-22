# Generated by Django 3.0.3 on 2020-04-22 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prodDir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodName', models.CharField(max_length=100)),
                ('numOfPieces', models.PositiveIntegerField(default=0)),
                ('buyingPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sellingPrice', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name': 'prodDir',
                'verbose_name_plural': 'prodDirs',
            },
        ),
        migrations.CreateModel(
            name='transHis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodId', models.IntegerField()),
                ('transType', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name': 'transHis',
                'verbose_name_plural': 'transHis',
            },
        ),
    ]
