# Generated by Django 3.2.7 on 2021-09-24 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_category', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['tag_category'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('user_login', models.CharField(max_length=200)),
                ('user_banned', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('post_text', models.TextField(max_length=1000)),
                ('post_publish_time', models.DateTimeField(auto_now_add=True, verbose_name='time published')),
                ('post_amend_time', models.DateTimeField(auto_now=True, verbose_name='time amended')),
                ('post_published', models.BooleanField(default=True)),
                ('author', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.user')),
                ('categories', models.ManyToManyField(to='blog.Tag')),
            ],
            options={
                'ordering': ['-post_publish_time', 'post_title'],
            },
        ),
    ]
