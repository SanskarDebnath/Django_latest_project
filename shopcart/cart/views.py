from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .cart import Cart
from product.models import Product
# Create your views here.


def add_cart (request):
    #initializes a blank cart or get an existing cart
    mycart = Cart(request)
    
    if request.method == "POST":
        prod_id = int(request.POST['product_id'])
        qty = int(request.POST['product_qty'])
        select_product = get_object_or_404 (Product, product_id = prod_id)
        mycart.add_item(added_product = select_product, prod_qty=qty)
        cart_quantity = len(mycart)
        print(cart_quantity)
        response = JsonResponse({'qty':cart_quantity})
        return response
    

def cart_page(request):
    cart = Cart(request)         #object(request) --> retrieve from session
    cart_products = cart.get_prod_list()
    return render(request, 'cart.html', {'cart_products':cart_products})    
    