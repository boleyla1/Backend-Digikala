from django.shortcuts import render, get_object_or_404, HttpResponse
from .cart import Cart
from shop.models import Product
from django.http import JsonResponse
from  django.contrib import messages


def Cartsummary(request):
    cart = Cart(request)
    cartproducts = cart.getproduct()
    quantitys = cart.get_quants()
    total = cart.get_total()
    return render(request, 'Cart/Carts.html', {'cartproducts': cartproducts, 'quantitys': quantitys,'total': total})


def Cartadd(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        Product_id = int(request.POST.get('Product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=Product_id)
        print(product_qty)
        cart.add(Product=product, quantity=product_qty)
        cart_len = cart.__len__()
        # response = JsonResponse({'product.name': product.Name})
        response = JsonResponse({'cart_len': cart_len})
        messages.success(request, ('به سبد خرید اضافه شد'))
        return response
    return HttpResponse('OK')


def Cartdelete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        Product_id = int(request.POST.get('Product_id'))
        cart.delete(product=Product_id)
        response = JsonResponse({'product':Product_id})
        messages.success(request,"محصول از سبد خرید حذف شد")
        return response



def Cartupdate(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        Product_id = int(request.POST.get('Product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=Product_id, quantity=product_qty)

        response = JsonResponse({'product_qty': product_qty})
        messages.success(request,"محصول ویرایش شد")
        return response
# Create your views here.
