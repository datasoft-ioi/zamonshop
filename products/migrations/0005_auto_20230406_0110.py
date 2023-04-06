# Generated by Django 3.2.13 on 2023-04-05 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20230406_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='subcat',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='subcat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.productcategory'),
        ),
    ]
