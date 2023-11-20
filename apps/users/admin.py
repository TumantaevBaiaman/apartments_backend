from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_manager')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_manager')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Custom Permissions', {'fields': ('is_manager',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
