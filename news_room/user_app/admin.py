from django.contrib import admin
from .models import CustomUser
from django.db import models
from tinymce.widgets import TinyMCE

class YourModelAdminForm(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 20})},
    }

admin.site.register(CustomUser, YourModelAdminForm)
