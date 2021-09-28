from re import S
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('shop/', views.shop, name="shop"),
    path('offers/', views.offers, name="offers"),
    path('about/', views.about, name="about"),
    path('faqs/', views.faqs, name="faqs"),
    path('contactus/', views.contactus, name="contactus"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('singleproduct/<str:slug>', views.singleproduct, name="singleproduct"),
    path('updateItem/', views.updateItem, name = "updateItem"),
]
