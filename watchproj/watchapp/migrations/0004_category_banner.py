# Generated by Django 5.0.2 on 2024-02-16 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchapp', '0003_delete_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='banner',
            field=models.ImageField(blank=True, upload_to='category'),
        ),
    ]
