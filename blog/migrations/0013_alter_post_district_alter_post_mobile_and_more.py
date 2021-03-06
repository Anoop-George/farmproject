# Generated by Django 4.0 on 2021-12-27 19:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20211227_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='district',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='mobile',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999999999), django.core.validators.MinValueValidator(999999)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='state',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
