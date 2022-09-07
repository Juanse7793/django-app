from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from . import models
# Register your models here.

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable: str = ['membership']
    search_fields: str = ['first_name__istartswith', 'last_name__istartswith']
    list_per_page: int = 10

    

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    list_per_page: int = 10

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return f'Low ({product.inventory})'
        return f'OK ({product.inventory})'


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + f'collection__id__exact={collection.id}')
        return format_html('<a href="{}">{}</a>',url ,collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )