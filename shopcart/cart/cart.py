from product.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        
        if ('session_key' not in request.session):
            cart = self.session['session_key'] = {} #initializes blank session cart object
        
        self.cart = cart

    def add_item (self, added_product, prod_qty):
        product_id = str(added_product.product_id)
        product_quantity = str(prod_qty)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_quantity)

        self.session.modified = True


    def __len__(self):
        # print("items in cart #####################", len(self.cart))
        cart_qty = self.cart
        qnty = 0
        for k in cart_qty:
            qnty += cart_qty[k]
        return (qnty)
    
    
    def get_prod_list(self):
        prod_id = self.cart.keys()     #keys() -> function - list of key
        prod_list = Product.objects.filter(product_id__in=prod_id)    #like SQL in operator
        return prod_list
    
   
