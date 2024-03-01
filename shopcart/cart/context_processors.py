from .cart import Cart

# Create a context processor so that our cart is accessible from all pages

def cart_ctx(request):
    # return the default data from our cart

    return {'mycart' : Cart(request)}  # Create a Cart object by pasing the request
