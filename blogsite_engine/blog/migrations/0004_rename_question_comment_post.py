# Generated by Django 3.2.7 on 2021-09-26 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210926_0512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='question',
            new_name='post',
        ),
    ]
