from django.contrib import admin

from .models import Category, Entry


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name", "slug"]
    ordering = ("slug",)


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ["title", "summary", "date", "category"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "summary", "body", "slug"]
    ordering = ("-date",)
    list_filter = ["category"]
    date_hierarchy = "date"
