# Generated by Django 4.2.1 on 2023-05-10 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_board', '0006_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field=100, null=True, upload_to='images/', width_field=100),
        ),
    ]
