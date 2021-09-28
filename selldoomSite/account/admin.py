from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from. models import user_info

class user_info_Inline(admin.StackedInline):
    model = user_info
    can_delete = False
    verbose_name_plural = 'user_info'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (user_info_Inline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(user_info)

