from django.contrib import admin

from .models import (
    Article
)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'image_show', 'body', 'owner')
