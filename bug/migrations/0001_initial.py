# Generated by Django 5.0.3 on 2024-03-05 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bug.parent')),
            ],
        ),
    ]
