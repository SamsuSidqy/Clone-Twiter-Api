# Generated by Django 5.0.6 on 2024-07-08 19:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0003_alter_feeds_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='slug',
            field=models.CharField(default=uuid.UUID('add2efcf-579a-46e4-8ab9-115dd969eb53'), max_length=300, unique=True),
        ),
    ]
