# Generated by Django 4.0.6 on 2022-09-30 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myecom', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='change_price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
