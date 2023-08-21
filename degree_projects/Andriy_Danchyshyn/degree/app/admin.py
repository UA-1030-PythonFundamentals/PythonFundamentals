from django.contrib import admin

from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published', 'created', 'updated', 'cat']
    list_filter = ['published']
    search_fields = ['title']
    prepopulated_fields = {"slug": ["title"]}
    date_hierarchy = 'published'
    ordering = ['published']


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ["name"]}