# Generated by Django 2.2.1 on 2019-05-11 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('created', models.DateTimeField()),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_synergy.Groups')),
            ],
        ),
    ]
