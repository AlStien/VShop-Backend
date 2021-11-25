# Generated by Django 3.2.9 on 2021-11-25 05:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('seller_product', '0002_alter_coupon_expiry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='picture2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='picture3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='picture4',
        ),
        migrations.AlterField(
            model_name='coupon',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 5, 53, 49, 673714, tzinfo=utc)),
        ),
    ]