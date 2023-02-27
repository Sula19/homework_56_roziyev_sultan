from django.contrib import admin
from webapp.models import Products


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'created_at']
    list_filter = ['id', 'name', 'category']
    search_fields = ['name', 'category']
    fields = ['name', 'description', 'category', 'price', 'remainder']
    readonly_fields = ['created_at']


admin.site.register(Products, ProductAdmin)
