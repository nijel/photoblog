# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import markupfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(unique_for_date='date', verbose_name='URL slug')),
                ('description', markupfield.fields.MarkupField(rendered_field=True, verbose_name='Description')),
                ('description_markup_type', models.CharField(choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown'), (b'restructuredtext', 'Restructured Text')], default='markdown', max_length=30)),
                ('_description_rendered', models.TextField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug', models.SlugField(unique_for_date='date', verbose_name='URL slug')),
                ('date', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Date')),
                ('summary', markupfield.fields.MarkupField(rendered_field=True, verbose_name='Summary')),
                ('body', markupfield.fields.MarkupField(rendered_field=True, verbose_name='Text')),
                ('summary_markup_type', models.CharField(choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown'), (b'restructuredtext', 'Restructured Text')], default='markdown', max_length=30)),
                ('body_markup_type', models.CharField(choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown'), (b'restructuredtext', 'Restructured Text')], default='markdown', max_length=30)),
                ('_summary_rendered', models.TextField(editable=False)),
                ('_body_rendered', models.TextField(editable=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Category', verbose_name='Category')),
            ],
        ),
    ]
