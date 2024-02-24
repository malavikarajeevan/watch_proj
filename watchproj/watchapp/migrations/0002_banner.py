# Generated by Django 5.0.2 on 2024-02-16 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('desc', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='banner')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
