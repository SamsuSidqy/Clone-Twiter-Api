# Generated by Django 5.0.6 on 2024-06-22 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retweet',
            name='retwet',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retwet', to='tweet.feeds'),
        ),
    ]
