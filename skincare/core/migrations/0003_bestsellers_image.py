# Generated by Django 5.0.1 on 2024-03-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_bestsellers_delete_cream'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestsellers',
            name='image',
            field=models.ImageField(default='NA', upload_to='bestsellers'),
        ),
    ]