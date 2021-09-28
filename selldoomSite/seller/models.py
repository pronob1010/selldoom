from django.db import models
from datetime import datetime  
from django.utils import timezone
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from account .models import user_info

class Product_Category(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title    


STATUS = (
    (0,"Block"),
    (1,"Publish")
)

class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    seller_info = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    product_Title = models.CharField(max_length=200)   
    slug = AutoSlugField(populate_from='product_Title')
    product_category = models.ForeignKey('Product_Category', on_delete=models.SET_NULL, blank= True, null = True)
    product_sub_category = models.CharField(max_length=200)
    product_stock = models.IntegerField(null=True)
    product_Selling_price = models.FloatField(default=0)
    product_offer_price = models.FloatField()
    OfferPercent = models.IntegerField(blank=True, default=0)
    
    if product_offer_price:    
         def save(self, *args, **kwargs):
            self.OfferPercent = (100-(100*float(self.product_offer_price)/float(self.product_Selling_price)))
            super().save(*args, **kwargs)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    productDescription = models.CharField(max_length=500, default = 'This is product description.')
    productImg =  models.ImageField(upload_to='productsImg', blank=True, null = True)
    
    @property
    def imageURL(self):
        try:
            url = self.productImg.url
        except:
            url= ''
        return url

    digital = models.BooleanField(default=False, null=True, blank=False)
    slider_Base_Title = models.CharField(max_length=200, null= True)
    slider_Sub_Title = models.CharField(max_length=200, null= True)
    def __str__(self):
        return self.product_Title  

#     def __int__(self):
#         return self.OfferPercent

#     class Meta:
#         ordering = ['-created_on']

# class productImage(models.Model):
#     post = models.ForeignKey(product, default=None, on_delete=models.CASCADE)
#     productImg =  models.ImageField(upload_to='productsImg/') 

#     def __str__(self):
#         return self.post.product_Title


class product_actions(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    featured_product = models.BooleanField(default=False)
    special_promotion = models.BooleanField(default=False)
    slider_promotion = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=1)

    # def __str__(self):
    #     return self.product_id


class Order(models.Model):
    customer = models.ForeignKey(user_info,on_delete=models.SET_NULL, blank= True, null = True)
    date_of_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()

        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    # def __str__(self):
    #     return self.customer

class OrderItem(models.Model):
    product = models.ForeignKey(product, on_delete= models.SET_NULL, blank = True, null=True)
    Order = models.ForeignKey(Order, on_delete= models.SET_NULL, blank = True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.product_offer_price * self.quantity
        return total

class mywish(models.Model):
    customer = models.ForeignKey(user_info,on_delete=models.SET_NULL, blank= True, null = True)
    
    @property
    def get_wish_items(self):
        wishitems = self.orderitem_set.all()
        total = sum([item.quantity for item in wishitems])
        return total

class wishItem(models.Model):
    product = models.ForeignKey(product, on_delete= models.SET_NULL, blank = True, null=True)
    Order = models.ForeignKey(mywish, on_delete= models.SET_NULL, blank = True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    
    @property
    def get_total(self):
        total = self.product.product_offer_price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(user_info,on_delete=models.SET_NULL, blank= True, null = True)
    Order = models.ForeignKey(Order, on_delete= models.SET_NULL, blank = True, null=True)
    address = models.CharField(max_length=200, null= True)
    city = models.CharField(max_length=200, null= True)
    state = models.CharField(max_length=200, null= True)
    zipcode = models.CharField(max_length=200, null= True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


