# Generated by Django 4.2.1 on 2023-05-08 17:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_board', '0003_alter_post_liked_alter_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='datecreation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
