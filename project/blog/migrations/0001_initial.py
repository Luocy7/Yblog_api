# Generated by Django 3.1 on 2020-11-19 03:16

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='FriendLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_avatar', models.CharField(blank=True, max_length=200, verbose_name='Link Avatar')),
                ('link_name', models.CharField(max_length=200, verbose_name='Link Name')),
                ('link_url', models.CharField(max_length=200, verbose_name='Link Url')),
                ('link_order', models.IntegerField(verbose_name='Link Order')),
            ],
            options={
                'verbose_name': 'Friend Link',
                'verbose_name_plural': 'Friend Link',
                'ordering': ['link_order'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('markdown', models.TextField(verbose_name='Post Markdown')),
                ('html', models.TextField(blank=True, verbose_name='Html')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Datetime Created')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='Datetime Modified')),
                ('excerpt', models.CharField(blank=True, max_length=200, verbose_name='Excerpt')),
                ('post_views', models.PositiveIntegerField(default=0, editable=False, verbose_name='Post Views')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_posts', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('category', models.ForeignKey(on_delete=models.SET(blog.models.get_default_cate), related_name='related_posts', to='blog.category', verbose_name='Category')),
                ('tags', models.ManyToManyField(blank=True, related_name='related_posts', to='blog.Tag', verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Post',
                'ordering': ['-created_time'],
            },
        ),
    ]
