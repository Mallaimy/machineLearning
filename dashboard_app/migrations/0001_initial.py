# Generated by Django 4.0 on 2022-05-13 20:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('sex', models.PositiveBigIntegerField(choices=[(0, 'Female'), (1, 'Male')], null=True)),
                ('age', models.PositiveBigIntegerField(null=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(50)])),
                ('nombre_de_personnes', models.CharField(max_length=100, null=True)),
                ('predictions', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
