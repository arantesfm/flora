# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('familia', models.CharField(max_length=300)),
                ('genero', models.CharField(max_length=300)),
                ('especie', models.CharField(max_length=300)),
                ('autor', models.CharField(max_length=300)),
                ('texto', models.TextField()),
                ('habito', models.CharField(max_length=300)),
                ('vernacular', models.CharField(max_length=300)),
                ('floracao', models.CharField(max_length=300)),
                ('frutificacao', models.CharField(max_length=300)),
                ('origem', models.CharField(max_length=300)),
                ('mapa', models.TextField()),
                ('referencias', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
