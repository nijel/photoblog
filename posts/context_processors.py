from django.conf import settings

from .models import Category, Entry


def context(request):
    return {
        "categories": Category.objects.all(),
        "og_entry": Entry.objects.get(pk=settings.OG_POST),
    }
