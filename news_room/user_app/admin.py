from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# from django.forms import TextInput, Textarea
# from tinymce.widgets import TinyMCE

# class CustomUserAdmin(UserAdmin):
#     formfield_overrides = {
#         CustomUser.description.field.name: {'widget': TinyMCE()},
#     }

admin.site.register(CustomUser)
