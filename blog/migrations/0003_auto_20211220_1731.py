# Generated by Django 2.1 on 2021-12-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211220_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pincode',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
