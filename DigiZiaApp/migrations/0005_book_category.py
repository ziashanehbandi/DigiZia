# Generated by Django 3.1.7 on 2021-04-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigiZiaApp', '0004_book_camera_laptop'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('art', 'ARTS $ PHOTOGRAPHY'), ('chi', 'CHILDERENS BOOK'), ('his', 'HISTORY'), ('rom', 'ROMANCE'), ('tee', 'TEENS & YOUNG ADULT'), ('pop', 'POPULAR')], default='pop', max_length=3),
        ),
    ]
