# Generated by Django 3.0.5 on 2022-04-13 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_auto_20220413_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
