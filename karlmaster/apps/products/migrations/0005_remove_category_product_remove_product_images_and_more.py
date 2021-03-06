# Generated by Django 4.0.4 on 2022-05-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productimages_product_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AlterField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='available'),
        ),
        migrations.DeleteModel(
            name='ProductImages',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
