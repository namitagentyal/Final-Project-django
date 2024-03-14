# Generated by Django 5.0.1 on 2024-03-04 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_bestsellers_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bestsellers_combos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(default='NA', upload_to='bestsellers')),
            ],
        ),
    ]