from django.contrib import admin
from .models import Manager

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'number', 'deal_count', 'created_at')
    search_fields = ('user__username', 'number')
    list_filter = ('deal_count',)
    date_hierarchy = 'created_at'
