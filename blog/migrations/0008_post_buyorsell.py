# Generated by Django 2.1 on 2021-12-23 12:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_catagory'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='buyorsell',
            field=models.CharField(default=django.utils.timezone.now, max_length=3),
            preserve_default=False,
        ),
    ]
