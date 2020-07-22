# Generated by Django 3.0.8 on 2020-07-21 22:23

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Npc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Loneliness', max_length=70)),
                ('attack', models.PositiveIntegerField(default=5)),
                ('defense', models.PositiveIntegerField(default=5)),
                ('health', models.PositiveIntegerField(default=10)),
                ('dialogue', django.contrib.postgres.fields.jsonb.JSONField()),
                ('options', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(), size=None)),
            ],
        ),
    ]
