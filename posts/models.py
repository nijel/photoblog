from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from markupfield.fields import MarkupField
from versatileimagefield.fields import VersatileImageField, PPOIField


class Category(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=100
    )
    slug = models.SlugField(
        verbose_name=_('URL slug'),
        db_index=True,
    )
    description = MarkupField(
        verbose_name=_('Description'),
        default_markup_type='markdown'
    )

    def __str__(self):
        return self.name


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
    image = VersatileImageField(
        'Image',
        upload_to='posts/%Y/%m/%d/',
        width_field='width',
        height_field='height',
        ppoi_field='ppoi'
    )
    height = models.PositiveIntegerField(
        'Image Height',
        editable=False,
        blank=True,
        null=True
    )
    width = models.PositiveIntegerField(
        'Image Width',
        editable=False,
        blank=True,
        null=True
    )
    ppoi = PPOIField(
        'Image PPOI'
    )

    def __str__(self):
        return self.title
