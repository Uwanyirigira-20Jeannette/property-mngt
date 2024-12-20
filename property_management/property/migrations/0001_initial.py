# Generated by Django 5.1.4 on 2024-12-19 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('property_type', models.CharField(max_length=50)),
                ('rent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='property_images/')),
                ('more_images', models.ImageField(blank=True, null=True, upload_to='property_images/')),
            ],
        ),
    ]