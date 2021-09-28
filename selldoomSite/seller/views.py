from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render
from.models import product, Product_Category
from http.client import responses
from django.core.files.storage import FileSystemStorage

def seller(request):
    return render(request, 'seller.html', {})

def allinall(request):
    product_list = product.objects.all().order_by("-created_on")
    return render(request, 'allinall.html', {
        "products": product_list
    })


@csrf_exempt
def addnewproduct(request):
    if request.method == 'POST'  :
        productTitle = request.POST['Title']
        productcategory = request.GET.get('Categories')
        productsub_category = request.POST['Sub-categories']
        productSelling_price = request.POST['price']
        productoffer_price = request.POST['selling_price']
        # product_brandname = request.POST['brandname']
        product_description = request.POST['text']
        product_image = request.FILES['productImage']
#  MUST READ : POST WORKS WELL. JUST PROBLEM ON UPLOAD FILE, SO START FROM HERE

        created_product = product.objects.create(
            product_Title=productTitle, 
            product_category=productcategory, 
            product_sub_category=productsub_category, 
            product_Selling_price=productSelling_price, 
            product_offer_price=productoffer_price,
            productDescription=product_description, 
            productImg=product_image)
        
        created_product.save()
        return HttpResponseRedirect('addnewproduct')  

    else:
        product_list = product.objects.all().order_by("-created_on")[:4]
        Pro_Category = Product_Category.objects.all()
        return render(request, 'addnewproduct.html', {"products": product_list, "category":Pro_Category})