# Generated by Django 5.0.6 on 2024-07-05 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='created_at',
            field=models.DateTimeField(blank=True),
        ),
    ]
