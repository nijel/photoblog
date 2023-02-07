# Generated by Django 2.0.2 on 2018-02-21 22:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_auto_20180221_2158"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="entry",
            options={"verbose_name": "Post", "verbose_name_plural": "Posts"},
        ),
        migrations.RemoveField(
            model_name="entry",
            name="_summary_rendered",
        ),
        migrations.RemoveField(
            model_name="entry",
            name="summary_markup_type",
        ),
        migrations.AlterField(
            model_name="entry",
            name="summary",
            field=models.CharField(max_length=300, verbose_name="Summary"),
        ),
    ]
