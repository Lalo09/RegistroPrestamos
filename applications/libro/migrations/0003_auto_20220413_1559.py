# Generated by Django 3.0.5 on 2022-04-13 15:59

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_auto_20220412_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'ordering': ['titulo', 'fecha'], 'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
        migrations.AlterModelManagers(
            name='categoria',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
