# Generated by Django 5.0.2 on 2024-02-16 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchapp', '0004_category_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='banner',
        ),
    ]
