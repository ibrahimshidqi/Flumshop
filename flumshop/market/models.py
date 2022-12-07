from unicodedata import decimal
from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Order(models.Model):
    datecreated = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.datecreated

# Banner
class Banner(models.Model):
    img = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural='1. Banners'

# Category
class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural='2. Categories'
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

# Brand
class Brand(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural='3. Brands'

    def __str__(self):
        return self.title

# Color
class Color(models.Model):
    title = models.CharField(max_length=200)
    color_code = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural='4. Colors'

    def __str__(self):
        return self.title

# Size
class Size(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural='5. sizes'

    def __str__(self):
        return self.title

# Product Model
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=500, null=True)
    slug = models.CharField(max_length=400)
    detail = models.TextField()
    specs = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural='6. Products'
    
    def __str__(self):
        return self.title

# Product Attribute
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural='7. ProductAttributes'

    def __str__(self):
        return self.product.title

