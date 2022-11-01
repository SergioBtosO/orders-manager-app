# Generated by Django 4.1.2 on 2022-11-01 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('document', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
