from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from markupfield.fields import MarkupField


class Category(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=100
    )
    slug = models.SlugField(
        verbose_name=_('URL slug'),
        db_index=True,
        unique_for_date='date'
    )
    description = MarkupField(
        verbose_name=_('Description'),
        default_markup_type='markdown'
    )


class Entry(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=100
    )
    slug = models.SlugField(
        verbose_name=_('URL slug'),
        db_index=True,
        unique_for_date='date'
    )
    category = models.ForeignKey(
        Category,
        verbose_name=_('Category'),
        on_delete=models.deletion.CASCADE,
    )
    date = models.DateTimeField(
        verbose_name=_('Date'),
        default=timezone.now,
        db_index=True
    )
    summary = MarkupField(
        verbose_name=_('Summary'),
        default_markup_type='markdown'
    )
    body = MarkupField(
        verbose_name=_('Text'),
        default_markup_type='markdown'
    )
