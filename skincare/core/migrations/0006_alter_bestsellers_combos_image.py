# Generated by Django 5.0.1 on 2024-03-04 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_bestsellers_combos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestsellers_combos',
            name='image',
            field=models.ImageField(default='NA', upload_to='bestsellers_combos'),
        ),
    ]
