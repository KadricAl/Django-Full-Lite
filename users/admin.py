from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Add custom fields to display in admin
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'phone', 'address', 'city')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'phone', 'address', 'city')}),
    )

    list_display = ['username', 'email', 'role', 'city', 'is_staff']
    search_fields = ['username', 'email']

admin.site.register(CustomUser, CustomUserAdmin)