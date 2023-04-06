# Generated by Django 3.2.13 on 2023-04-05 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='parent',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='subcat',
            field=models.ManyToManyField(related_name='_products_productcategory_subcat_+', to='products.ProductCategory'),
        ),
    ]
