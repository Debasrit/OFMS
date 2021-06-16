# Generated by Django 3.0.7 on 2020-06-28 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(default=None, max_length=20, null=True)),
                ('address', models.CharField(blank=True, default='None', max_length=500, null=True)),
                ('password', models.CharField(max_length=20)),
                ('register_date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
