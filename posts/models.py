from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from markupfield.fields import MarkupField
from versatileimagefield.fields import PPOIField, VersatileImageField


class Category(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=100)
    slug = models.SlugField(
        verbose_name=_("URL slug"),
        db_index=True,
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("archive", kwargs={"slug": self.slug})


class Entry(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=100)
    slug = models.SlugField(
        verbose_name=_("URL slug"), db_index=True, unique_for_date="date"
    )
    category = models.ForeignKey(
        Category,
        verbose_name=_("Category"),
        on_delete=models.deletion.CASCADE,
    )
    date = models.DateTimeField(
        verbose_name=_("Date"), default=timezone.now, db_index=True
    )
    summary = models.CharField(
        verbose_name=_("Summary"),
        max_length=300,
    )
    body = MarkupField(verbose_name=_("Text"), default_markup_type="markdown")
    image = VersatileImageField(
        "Image",
        upload_to="posts/%Y/%m/%d/",
        width_field="width",
        height_field="height",
        ppoi_field="ppoi",
    )
    height = models.PositiveIntegerField(
        "Image Height", editable=False, blank=True, null=True
    )
    width = models.PositiveIntegerField(
        "Image Width", editable=False, blank=True, null=True
    )
    ppoi = PPOIField("Image PPOI")

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ("-date",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "detail",
            kwargs={
                "slug": self.slug,
                "year": self.date.year,
                "month": self.date.month,
                "day": self.date.day,
            },
        )

    def get_related(self):
        return self.category.entry_set.exclude(pk=self.pk)[:4]


@receiver(models.signals.post_delete, sender=Entry)
def delete_post_images(sender, instance, **kwargs):
    # Deletes Image Renditions
    instance.image.delete_all_created_images()
    # Deletes Original Image
    instance.image.delete(save=False)
