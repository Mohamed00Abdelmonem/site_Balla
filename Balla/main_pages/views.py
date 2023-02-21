from django.shortcuts import render, redirect
from .models import Product
# Create your views here.



def home(request):
    return render(request, 'index.html ')

def about(request):
    return render(request, 'about.html ')

def products(request):
    return render(request, 'products.html ')





# def add_to_cart(request, product_id):
#     cart = request.session.get('cart', {})
#     cart[product_id] = cart.get(product_id, 0) + 1
#     request.session['cart'] = cart
#     return redirect('cart')


#
# def cart(request):
#     cart = request.session.get('cart', {})
#     return render(request, 'cart.html', {'cart': cart})
#
#



def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = request.user.cart
    cart_item = cart.cartitem_set.filter(product=product).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart.cartitem_set.create(product=product, price=product.price, quantity=1)
    return redirect('cart')



def cart(request):
    cart = request.user.cart
    return render(request, 'cart.html', {'cart': cart})

