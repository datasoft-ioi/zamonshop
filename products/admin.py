from django.contrib import admin
from .models import Product, ProductCategory
from mptt.admin import MPTTModelAdmin

class ProductCategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

admin.site.register(ProductCategory)
admin.site.register(Product)
# admin.site.register(SubCategory)
