# Generated by Django 3.2.9 on 2021-11-10 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller_product', '0005_product_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='product',
        ),
        migrations.AddField(
            model_name='tag',
            name='product',
            field=models.ManyToManyField(related_name='tag_product', to='seller_product.Product'),
        ),
    ]
