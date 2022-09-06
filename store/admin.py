from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable: str = ['membership']
    list_per_page: int = 10


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status']
    list_editable = ['unit_price']
    list_per_page: int = 10

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return f'Low ({product.inventory})'
        return f'OK ({product.inventory})'


admin.site.register(models.Collection)

