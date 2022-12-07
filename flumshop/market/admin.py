from django.contrib import admin
from . import models 

# Register your models here.
admin.site.register(models.Blog)
admin.site.register(models.Order)
admin.site.register(models.Banner)
admin.site.register(models.Brand)
admin.site.register(models.Color)
admin.site.register(models.Size)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('title', 'image_tag')
admin.site.register(models.Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id', 'title','brand', 'color', 'size', 'status')
    list_editable=('status',)
admin.site.register(models.Product,ProductAdmin)

# Product Attribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id', 'product', 'color', 'size', 'price')
admin.site.register(models.ProductAttribute,ProductAttributeAdmin)
