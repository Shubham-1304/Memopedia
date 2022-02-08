# Generated by Django 4.0.2 on 2022-02-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memes',
            fields=[
                ('id', models.IntegerField(blank=True, max_length=100, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('url', models.TextField(max_length=200)),
                ('width', models.IntegerField(blank=True, max_length=100)),
                ('height', models.IntegerField(blank=True, max_length=100)),
                ('box_count', models.IntegerField(blank=True, max_length=100)),
            ],
        ),
    ]
