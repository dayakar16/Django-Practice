# Generated by Django 3.2.4 on 2021-06-15 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='paid',
            field=models.BooleanField(default=True),
        ),
    ]
