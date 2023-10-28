# Generated by Django 4.2.6 on 2023-10-14 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('deviceModel', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('note', models.TextField()),
                ('serial', models.CharField(max_length=100)),
            ],
        ),
    ]
