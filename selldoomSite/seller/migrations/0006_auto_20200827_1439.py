# Generated by Django 3.0.8 on 2020-08-27 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_product_actions_slider_promotion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_actions',
            name='slider_Base_Title',
        ),
        migrations.RemoveField(
            model_name='product_actions',
            name='slider_Sub_Title',
        ),
        migrations.AddField(
            model_name='product',
            name='slider_Base_Title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slider_Sub_Title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
