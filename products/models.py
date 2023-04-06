from django.db import models

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(null=True, blank=True, max_length=255)
    # parent = TreeForeignKey(
    #     'self',
    #     on_delete=models.SET_NULL,
    #     related_name='child_category_list',
    #     blank=True,
    #     null=True,
    # )

    # parent = models.ForeignKey(to=, null=True, blank=True, on_delete=models.PROTECT)
    # parent = models.ForeignKey('self', null=True, blank=True, related_name='chilldren', on_delete=models.SET_NULL)


    def __str__(self):
        return self.name

    # class MPTTMeta:
    #     order_insertion_by = ['name']


    # def __str__(self):
    #     full_path = [self.name]
    #     k = self.parent
    #     while k is not None:
    #         full_path.append(k.name)
    #         k = k.parent
    #     return ' -> '.join(full_path[::-1])
    


class Category(models.Model):
    name = models.CharField(max_length=255)


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(null=True, blank=True, max_length=255)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='prod_images')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)


    def __str__(self) -> str:
        return self.name
    
