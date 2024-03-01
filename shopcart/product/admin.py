from django.contrib import admin
from product.models import Product, ProductCategory

class ProductAdmin (admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'product_description', 'product_price')

# Register your models here.
# admin.site.register(Product)

admin.site.register(Product, ProductAdmin)

admin.site.register(ProductCategory)