from django.shortcuts import render, get_object_or_404
from .cart import Cart
from product.models import Product
from django.http import JsonResponse 

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request, "cart_summary.html", {"cart_products": cart_products, "quantities": quantities})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)

        cart_quantity = cart.__len__()

        #response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty: ': cart_quantity})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    if request.method == 'POST':
        # Get the product ID and quantity from the request
        product_id = request.POST.get('product_id')
        if not product_id:
            return JsonResponse({'error': 'Product ID is required'}, status=400)

        try:
            product_id = int(product_id)
        except ValueError:
            return JsonResponse({'error': 'Invalid product ID'}, status=400)

        product_qty = request.POST.get('product_qty', 1)  # Default to 1 if not provided
        try:
            product_qty = int(product_qty)
        except ValueError:
            return JsonResponse({'error': 'Invalid quantity'}, status=400)

        # Get the product object
        product = get_object_or_404(Product, id=product_id)

        # Initialize and update the cart
        cart = Cart(request)
        cart.update(product=product, quantity=product_qty)

        # Get the updated cart info
        cart_quantity = cart.__len__()
        # Return the updated cart info as JSON
        return JsonResponse({
            'qty': cart_quantity,
        })