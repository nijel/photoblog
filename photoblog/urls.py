"""photoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import index, sitemap
from django.urls import include, path
from django.utils.timezone import now
from django.views.generic.dates import DateDetailView

from posts.models import Category, Entry
from posts.views import ArchiveView, CategoryView, ContactView


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return Entry.objects.filter(date__lte=now())

    def lastmod(self, obj):
        return obj.date


class CategorySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Category.objects.all()


sitemaps = {
    "prispevky": BlogSitemap(),
    "typy": CategorySitemap(),
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "detail/<int:year>/<int:month>/<int:day>/<slug:slug>/",
        DateDetailView.as_view(
            model=Entry,
            date_field="date",
            month_format="%m",
        ),
        name="detail",
    ),
    path(
        "",
        ArchiveView.as_view(),
        name="index",
    ),
    path(
        "<int:page>/",
        ArchiveView.as_view(),
        name="index",
    ),
    path("typ/<slug:slug>/", CategoryView.as_view(), name="archive"),
    path("typ/<slug:slug>/<int:page>/", CategoryView.as_view(), name="archive"),
    path("kontakt/", ContactView.as_view(), name="contact"),
    path("sitemap.xml", index, {"sitemaps": sitemaps}),
    path(
        "sitemap-<section>.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
