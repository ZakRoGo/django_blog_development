# Generated by Django 4.2.3 on 2023-07-22 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]