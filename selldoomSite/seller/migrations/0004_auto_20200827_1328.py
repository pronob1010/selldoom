# Generated by Django 3.0.8 on 2020-08-27 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_product_seller_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_actions',
            name='slider_Base_Title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product_actions',
            name='slider_Sub_Title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]