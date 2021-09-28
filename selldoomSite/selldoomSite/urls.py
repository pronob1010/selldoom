from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shopmain.urls')),
    path('', include('seller.urls')),
    path('', include('account.urls')),
    path('', include('shippingStatus.urls')),
]
