# Generated by Django 4.0.2 on 2022-02-07 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_memes_box_count_alter_memes_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='memes',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
