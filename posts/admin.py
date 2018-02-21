from django.contrib import admin

from .models import Category, Entry


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'slug', 'description']
    ordering = ('slug',)


class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'summary', 'date', 'category']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'summary', 'description', 'slug']
    ordering = ('-date',)
    list_filter = ['category']
    date_hierarchy = 'date'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
