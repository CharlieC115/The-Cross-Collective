from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'total',)

    fields = ('order_number', 'user_profile', 'date', 'first_name', 'last_name',
              'email', 'contact_number', 'postcode', 'total',)

    list_display = ('order_number', 'date', 'first_name',
                    'last_name', 'total',
                    'postcode',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
