# Generated by Django 4.0.6 on 2022-10-31 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
