# Generated by Django 4.0.6 on 2022-10-01 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myecom', '0004_product_change_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='Address',
            new_name='address',
        ),
    ]
