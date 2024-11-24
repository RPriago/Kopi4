from product.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        
        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        self.cart = cart
    
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
           # self.cart[product.id] = {'price': str(product.price)}
            self.cart[product.id] = int(product_qty)
        
        self.session.modified = True
    
    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product.id)  # Ensure product_id is a string for consistent keys
        if product_id in self.cart:
            if isinstance(self.cart[product_id], dict):  # Check if it's a dictionary
                self.cart[product_id]['quantity'] = quantity
            else:
                # In case it's an integer (incorrectly set), convert it to a dict
                self.cart[product_id] = {'quantity': quantity}
        else:
            # Handle case where the product is not in the cart yet
            self.cart[product_id] = {'quantity': quantity}
    
    