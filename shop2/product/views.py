from django.http import HttpResponse
from django.shortcuts import render, redirect
from product.models import Product
from . import forms #. means current folder

#for messages framework
from django.contrib import messages


# Create your views here.
def say_hello(request):
    return HttpResponse('Hello Django')

def startpage(request):
    # context = {"name":"sanskar", "roll_no":21670}
    return render(request, 'index.html')
    #return render(request, 'index.html', context)

def garmentpage(request):
    return render(request, 'garment.html')

def mobilepage(request):
    return render(request, 'mobile.html')

def testpage (request):
    context = {"name":"sanskar", "roll_no":21670}
    return render (request, 'test.html', context)

def viewall (request):
    # context = {"name":"sanskar", "roll_no":21670}
    # get all records from database
    allproduct = Product.objects.all()
    print(allproduct)
    context = {"my_products": allproduct}
    return render (request, 'showproduct.html', context)


def editorder (request, pid):
    selcted_product = Product.objects.get(product_id=pid) #seelcted_product commom section
    
    if request.method == "POST":
        pname = request.POST.get("p_name")
        pdesc = request.POST.get("p_desc")
        pprice = request.POST.get("price")
        
        print ("just to debug ***********---------", pname, pdesc, pprice)
        
        # po = Product (product_name = pname, product_description = pdesc, product_price = pprice)
        # po.save()
        selcted_product.product_name =pname
        selcted_product.product_description = pdesc
        selcted_product.product_price = pprice
        
        selcted_product.save()
        messages.success(request,"Data Updated")
        return redirect('/allibaba/showprod')
    
    context = {"edit_product" : selcted_product}
    return  render (request, 'edit_product.html', context)



def add_product(request):
    print("debug_method ***********")
    if request.method == "POST":
        pname = request.POST.get("p_name")
        pdesc = request.POST.get("p_desc")
        pprice = request.POST.get("price")
        
        print ("just to debug ***********---------", pname, pdesc, pprice)
        
        po = Product (product_name = pname, product_description = pdesc, product_price = pprice)
        po.save()
        
        messages.success(request,"Data saved successfully thank you")
        
    return render(request, 'add_product.html')



def deleteorder (request, pid):
    selcted_product = Product.objects.get(product_id=pid) #seelcted_product commom section
    selcted_product.delete()
    messages.warning(request,"Data deleted")
    return redirect ('/showprod')
    # return  render (request, 'edit_product.html')
    
def prod_cat (request):
    
    #print(myform)
    if request.method == "POST":
        form = forms.ProductCategoryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "your file has been uploaded")
            return redirect('product-catagory')

    
    myform = forms.ProductCategoryForm()
    return render (request, 'prod_cat.html',{'my_form':myform})