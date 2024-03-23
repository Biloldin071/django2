from django.contrib import admin
from .models import News
from .models import Category

# admin.site.register(News)
# admin.site.register(Category)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'status', 'publish_time']
    list_filter = ['status', 'created_time', 'publish_time', 'category']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'body']
    date_hierarchy = 'created_time'

@admin.register(Category)
class NewsCategory(admin.ModelAdmin):
    list_display = ['id', 'name']