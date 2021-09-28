from django.contrib import admin
from. models import *
# singleproduct

# class productImage_admin(admin.StackedInline):
#     model = productImage


# class PostAdmin(admin.ModelAdmin):
#     inlines = [productImage]

#     class Meta:
#         model = product


# @admin.register(productImage)
# class PostproductImageAdmin(admin.ModelAdmin):
#     pass

admin.site.register(product)
admin.site.register(Product_Category)
admin.site.register(product_actions)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

admin.site.register(mywish)
admin.site.register(wishItem)