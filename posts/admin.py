from django.contrib import admin

from .models import Category, Entry


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'slug', 'description']
    ordering = ('slug',)


class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'category']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'slug']
    ordering = ('-date',)
    date_hierarchy = 'date'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
