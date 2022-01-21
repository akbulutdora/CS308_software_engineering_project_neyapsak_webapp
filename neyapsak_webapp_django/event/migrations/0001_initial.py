# Generated by Django 3.2.8 on 2021-12-14 12:37

from django.db import migrations, models
import event.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('eventID', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('description', models.TextField(default='', null=True)),
                ('region', models.CharField(default='', max_length=20, null=True)),
                ('city', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('minPrice', models.IntegerField()),
                ('maxPrice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='manages',
            fields=[
                ('key', models.IntegerField(default=event.models.generateID, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('eventID', models.IntegerField()),
            ],
            options={
                'unique_together': {('email', 'eventID')},
            },
        ),
    ]
