# Generated by Django 2.1 on 2021-12-27 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20211227_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='post_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='post_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='post_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image4',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='post_pics'),
        ),
    ]
