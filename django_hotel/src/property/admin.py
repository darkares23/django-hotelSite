from django.contrib import admin

# Register your models here.
from .models import Property, Category, Reserve


class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'type',
                    'category', 'beds_number', 'baths_number', 'garages_number']
    search_fields = ['name', 'type']
    list_filter = ['category']


admin.site.register(Property, PropertyAdmin)
admin.site.register(Category)
admin.site.register(Reserve)
