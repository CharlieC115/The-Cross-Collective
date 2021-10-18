from django.contrib import admin
from .models import Camp, Category

# Register your models here.

class CampAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'start_date',
        'finish_date',
        'location',
        'price',
        'description',
        'coaches',
        'staff',
        'image',
    )

    ordering = ('start_date',)

admin.site.register(Camp, CampAdmin)
admin.site.register(Category)
