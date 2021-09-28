from django.shortcuts import render, get_object_or_404
from datetime import datetime, date
from django.utils import timezone
from account.models import *
from seller.models import *
from .models import *
from django.contrib.auth.models import User, auth
from account .models import *
from seller. models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_protect

class superCart:
    def __init__(self, request):
        self.request = request  
    def cart(self,request):
        if self.request.user.is_authenticated:
            customer = self.request.user.user_info
            order, created = Order.objects.get_or_create(customer = customer, complete = False)
            items = order.orderitem_set.all()
            cartItem = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
            cartItem = order['get_cart_items']
        return {'items':items, 'order': order}

    def wish(self,request):
        if self.request.user.is_authenticated:
            customer = self.request.user.user_info
            wish, created = mywish.objects.get_or_create(customer = customer)
            items = wish.wishItem_set.all()
            wishItem = wish.get_wish_items
        else:
            items = []
            wish = {'get_wish_total':0, }
            wishItem = wish['get_wish_items']
        return {'wish_items':items, 'wish': wish}

def index(request):
    site_social_link = Social_Media.objects.get(id=1)
    site_info = Notice.objects.get(id=1)
    base_info = Website_Details.objects.get(id=1)

    product_list1 = product.objects.filter(product_actions__featured_product=True).order_by("-created_on")[:8]
    product_list2 = product.objects.filter(OfferPercent__gte = 20).order_by("-created_on")[:8]
    product_list3 = product.objects.filter(OfferPercent__gte = 30).order_by("-created_on")[:8]

    product_list1_footer = product.objects.filter(product_actions__featured_product=True).order_by("-created_on")[:4]
    product_list2_footer = product.objects.filter(OfferPercent__gte = 20).order_by("-created_on")[:4]
    product_list3_footer = product.objects.filter(OfferPercent__gte = 30).order_by("-created_on")[:4]

    product_list4 = product.objects.filter(OfferPercent__gte = 40).order_by("-created_on")[:4]    
    product_list5 = product.objects.filter(OfferPercent__gte = 40).order_by("created_on")[:4]

    product_list6 = product.objects.filter(product_category__title='Fashion').order_by("-created_on")[:4]
    product_list7 = product.objects.filter(product_category__title='Fashion').order_by("-created_on")[:4]
    
    product_list8 = product.objects.filter(product_category__title='Watches & Accessories').order_by("-created_on")[:4]
    product_list9 = product.objects.filter(product_category__title='Watches & Accessories').order_by("-created_on")[:4]

    product_list10 = product.objects.filter(product_category__title='Electronic Devices').order_by("-created_on")[:4]
    product_list11 = product.objects.filter(product_category__title='Electronic Devices').order_by("-created_on")[:4]

    
    product_list12 = product.objects.filter(product_category__title='TV & Home Appliances').order_by("-created_on")[:4]
    product_list13 = product.objects.filter(product_category__title='TV & Home Appliances').order_by("-created_on")[:4]

    product_list14 = product.objects.filter(product_category__title='Health & Beauty').order_by("-created_on")[:4]
    product_list15 = product.objects.filter(product_category__title='Health & Beauty').order_by("-created_on")[:4]

    product_list18 = product.objects.filter(product_category__title='Home & Lifestyle').order_by("-created_on")[:4]
    product_list19 = product.objects.filter(product_category__title='Home & Lifestyle').order_by("-created_on")[:4]

    product_list20 = product.objects.filter(product_category__title='Babies & Toys').order_by("-created_on")[:4]
    product_list21 = product.objects.filter(product_category__title='Babies & Toys').order_by("-created_on")[:4]

    product_list22 = product.objects.filter(product_category__title='Sports & Outdoor').order_by("-created_on")[:4]
    product_list23 = product.objects.filter(product_category__title='Sports & Outdoor').order_by("-created_on")[:4]

    product_list24 = product.objects.filter(product_actions__slider_promotion=True).order_by("-created_on")[:5]
    # product_list17 = product.objects.filter(product_category__title='Health & Beauty').order_by("-created_on")[:4]

    customer_cart = superCart(request)
    context = customer_cart.cart(customer_cart)
    context.update({
        "site_social_link":site_social_link,
        "site_notice":site_info,
        "base_info":base_info,
        "products_featured": product_list1, 
        "products_On_sale": product_list2, 
        "products_top_rated": product_list3,

        "products_featured_footer": product_list1_footer,
        "products_On_sale_footer": product_list2_footer, 
        "products_top_rated_footer": product_list3_footer,
        

        "products_best_deals_1":product_list4,
        "products_best_deals_2":product_list5,

        "products_fashion_1":product_list6,
        "products_fashion_2":product_list7,

        "products_Watches_Accessories_1":product_list8,
        "products_Watches_Accessories_2":product_list9,

        "products_Electronic_Devices_1":product_list10,
        "products_Electronic_Devices_2":product_list11,

        "products_TV_Home_Appliances_1":product_list12,
        "products_TV_Home_Appliances_2":product_list13,

        "products_Health_Beauty_1":product_list14,
        "products_Health_Beauty_2":product_list15,
        
        # "products_Health_Beauty_1":product_list16,
        # "products_Health_Beauty_2":product_list17,

        "products_Home_Lifestyle_1":product_list18,
        "products_Home_Lifestyle_2":product_list19,

        "products_Babies_Toys_1":product_list20,
        "products_Babies_Toys_2":product_list21,

        "products_Sports_Outdoor_1":product_list22,
        "products_Sports_Outdoor_2":product_list23,

        "products_slider_promotion":product_list24,
        })
    return render(request, 'index.html', context)

def base(request):
    site_social_link = Social_Media.objects.get(id=1)
    site_info = Notice.objects.get(id=1)
    base_info = Website_Details.objects.get(id=1)
    customer_cart = superCart(request)
    context = customer_cart.cart(customer_cart)
    context.update({
        "site_social_link":site_social_link,
        "site_notice":site_info,
        "base_info":base_info,
    })
    return render(request, 'base.html', context)

def shop(request):
    site_social_link = Social_Media.objects.get(id=1)
    site_info = Notice.objects.get(id=1)
    base_info = Website_Details.objects.get(id=1)

    product_list = product.objects.all().order_by("-created_on")
    latest_products_list = product.objects.all().order_by("-created_on")[:5]

    product_list1_footer = product.objects.filter(product_actions__featured_product=True).order_by("-created_on")[:4]
    product_list2_footer = product.objects.filter(OfferPercent__gte = 20).order_by("-created_on")[:4]
    product_list3_footer = product.objects.filter(OfferPercent__gte = 30).order_by("-created_on")[:4]

    customer_cart = superCart(request)
    context = customer_cart.cart(customer_cart) 
    context.update({

        "site_social_link":site_social_link,
        "site_notice":site_info,
        "base_info":base_info,
        
        "products": product_list, 
        'latest_products_list':latest_products_list,
        
        "products_featured_footer": product_list1_footer,
        "products_On_sale_footer": product_list2_footer, 
        "products_top_rated_footer": product_list3_footer,
        })
    return render(request, 'shop.html', context)

def cart(request):
    site_social_link = Social_Media.objects.get(id=1)
    site_info = Notice.objects.get(id=1)
    base_info = Website_Details.objects.get(id=1)

    customer_cart = superCart(request)
    context = customer_cart.cart(customer_cart)
    context.update({
        "site_social_link":site_social_link,
        "site_notice":site_info,
        "base_info":base_info,
    })
    return render(request, 'cart.html', context)

# def wish(request):
#     site_social_link = Social_Media.objects.get(id=1)
#     site_info = Notice.objects.get(id=1)
#     base_info = Website_Details.objects.get(id=1)

#     customer_wish = superCart(request)
#     context = customer_wish.wish(customer_wish)
#     context.update({
#         "site_social_link":site_social_link,
#         "site_notice":site_info,
#         "base_info":base_info,
#     })
#     return render(request, 'wishlist.html', context)

def checkout(request):
    site_social_link = Social_Media.objects.get(id=1)
    site_info = Notice.objects.get(id=1)
    base_info = Website_Details.objects.get(id=1)

    customer_cart = superCart(request)
    context = customer_cart.cart(customer_cart)
    context.update({
        "site_social_link":site_social_link,
        "site_notice":site_info,
        "base_info":base_info,
    })
    return render(request, 'checkout.html', context)

def updateItem(request):
    site_social_link = Social_Media.objects.get(id=1)
    site_info = Notice.objects.get(id=1)
    base_info = Website_Details.objects.get(id=1)

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    customer = request.user.user_info
    Product = product.objects.get(product_id = productId)

    order, created = Order.objects.get_or_create(customer = customer, complete = False)
    
    orderItem, created = OrderItem.objects.get_or_create(Order=order, product = Product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'allremove':
        orderItem.quantity = (orderItem.quantity - orderItem.quantity)

    orderItem.save()
    if orderItem.quantity<=0:
        orderItem.delete()

    return JsonResponse('item was added', safe = False)

def singleproduct(request, slug):
    site_social_link = Social_Media.objects.get(id=1)
    site_info = Notice.objects.get(id=1)
    base_info = Website_Details.objects.get(id=1)
    customer_cart = superCart(request)

    single_product= get_object_or_404(product, slug = slug)
    context = customer_cart.cart(customer_cart)
    context.update({
        "single_product":single_product,
    })
    return render(request, 'single-product-full-width.html', context)

def categories(request):
    site_social_link = Social_Media.objects.get(id=1)
    site_info = Notice.objects.get(id=1)
    base_info = Website_Details.objects.get(id=1)

    customer_cart = superCart(request)
    context = customer_cart.cart(customer_cart)
    context.update({
        "site_social_link":site_social_link,
        "site_notice":site_info,
        "base_info":base_info,
    })
    return render(request, 'categories.html', context)

def contactus(request):
    site_social_link = Social_Media.objects.get(id=1)
    site_info = Notice.objects.get(id=1)
    base_info = Website_Details.objects.get(id=1)

    customer_cart = superCart(request)
    context = customer_cart.cart(customer_cart)
    context.update({
        "site_social_link":site_social_link,
        "site_notice":site_info,
        "base_info":base_info,
    })
    return render(request, 'contactus.html', context)

def trackYourOrder(request):
    site_social_link = Social_Media.objects.get(id=1)
    site_info = Notice.objects.get(id=1)
    base_info = Website_Details.objects.get(id=1)

    customer_cart = superCart(request)
    context = customer_cart.cart(customer_cart)
    context.update({
        "site_social_link":site_social_link,
        "site_notice":site_info,
        "base_info":base_info,
    })
    return render(request, 'trackYourOrder.html', context)

def about(request):
    site_social_link = Social_Media.objects.get(id=1)
    site_info = Notice.objects.get(id=1)
    base_info = Website_Details.objects.get(id=1)

    customer_cart = superCart(request)
    context = customer_cart.cart(customer_cart)
    context.update({
        "site_social_link":site_social_link,
        "site_notice":site_info,
        "base_info":base_info,
    })
    return render(request, 'about.html', context)

def faqs(request):
    site_social_link = Social_Media.objects.get(id=1)
    site_info = Notice.objects.get(id=1)
    base_info = Website_Details.objects.get(id=1)

    customer_cart = superCart(request)
    context = customer_cart.cart(customer_cart)
    context.update({
        "site_social_link":site_social_link,
        "site_notice":site_info,
        "base_info":base_info,
    })
    return render(request, 'faqs.html', context)

def wishlist(request):
    site_social_link = Social_Media.objects.get(id=1)
    site_info = Notice.objects.get(id=1)
    base_info = Website_Details.objects.get(id=1)

    customer_cart = superCart(request)
    context = customer_cart.cart(customer_cart)
    context.update({
        "site_social_link":site_social_link,
        "site_notice":site_info,
        "base_info":base_info,
    })
    return render(request, 'wishlist.html', context)

def offers(request):
    site_social_link = Social_Media.objects.get(id=1)
    site_info = Notice.objects.get(id=1)
    base_info = Website_Details.objects.get(id=1)

    customer_cart = superCart(request)
    context = customer_cart.cart(customer_cart)
    context.update({
        "site_social_link":site_social_link,
        "site_notice":site_info,
        "base_info":base_info,
    })
    return render(request, 'offers.html', context)

