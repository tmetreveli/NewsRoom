from django.contrib import admin
from .models import Category, Tag, Article
from tinymce.widgets import TinyMCE
from django.db import models


class ArticleAdminForm(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 20})},
    }

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)