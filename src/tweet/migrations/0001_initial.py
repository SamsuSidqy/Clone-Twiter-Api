# Generated by Django 5.0.6 on 2024-06-30 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=300, unique=True)),
                ('media', models.FileField(blank=True, upload_to='cdn/')),
                ('retweet', models.BooleanField(default=False)),
                ('likes', models.BigIntegerField(default=0)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 6, 30, 15, 6, 14, 266811, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.IntegerField()),
                ('feeds', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Retweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
