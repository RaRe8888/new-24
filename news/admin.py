from django.contrib import admin
from .models import Category,Tags,Article
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_at','is_active')

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active','created_at')

@admin.register(Article)
class ArcticleAdmin(admin.ModelAdmin):
    list_display = ('id','category','is_active','created_at')
    readonly_fields = ('views',)

    filter_horizontal = ('tags',)