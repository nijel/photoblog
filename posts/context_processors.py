from django.conf import settings

from .models import Category, Post


def context(request):
    return {
        'categories': Category.objects.all(),
        'og_post': Post.objects.filter(pk=settings.OG_POST),
    }
