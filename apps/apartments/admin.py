from django.contrib import admin
from .models import Object, Apartment

@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'object', 'number', 'floor', 'price', 'client', 'status', 'kv', 'created_at')
    list_filter = ('object', 'status')
    search_fields = ('client',)
    date_hierarchy = 'created_at'
