from django.contrib import admin
from .models import Customer, Order, ProductOrder, Product

class ProductOrdersIniline(admin.TabularInline):
    model = ProductOrder

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'date')
    inlines = [ProductOrdersIniline]




admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductOrder)
admin.site.register(Product)
