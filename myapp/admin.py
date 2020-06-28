from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(PythonCategory)
class PythonCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Python)
class PythonAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'publish_date']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['title', 'category', 'publish_date']

@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name', 'description']



@admin.register(Django)
class DjangoAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['posted_by', 'title', 'publish_date', 'text']

@admin.register(JavaScript)
class JavaScriptAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['posted_by', 'title', 'publish_date', 'text']

@admin.register(React)
class ReactAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['posted_by', 'title', 'publish_date', 'text']

admin.site.register(About)
