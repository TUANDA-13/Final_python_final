# Generated by Django 4.0.2 on 2022-06-16 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_post_content_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Topic',
        ),
    ]