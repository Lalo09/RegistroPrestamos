# Generated by Django 3.0.5 on 2022-04-13 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.Persona')),
                ('empleo', models.CharField(max_length=55, verbose_name='Empleo')),
            ],
            bases=('home.persona',),
        ),
    ]
