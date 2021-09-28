from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('seller', views.seller, name='seller'),
    path('allinall', views.allinall, name='allinall'),
    path('addnewproduct', views.addnewproduct, name='addnewproduct'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)