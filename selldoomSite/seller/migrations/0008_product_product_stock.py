# Generated by Django 3.0.7 on 2020-09-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0007_mywish_wishitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_stock',
            field=models.IntegerField(null=True),
        ),
    ]