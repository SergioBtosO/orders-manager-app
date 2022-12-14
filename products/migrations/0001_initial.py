# Generated by Django 4.1.2 on 2022-11-01 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ref', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=11)),
                ('size', models.CharField(max_length=100)),
                ('colors', models.CharField(max_length=255)),
            ],
        ),
    ]
