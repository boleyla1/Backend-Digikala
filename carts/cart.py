from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, Product, quantity):
        Product_id = int(Product.id)
        product_qty = int(quantity)
        if Product_id in self.cart:
            pass
        else:
            self.cart[Product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def getproduct(self):
        Product_id = self.cart.keys()
        Products = Product.objects.filter(id__in=Product_id)
        return Products

    def get_quants(self):
        quantitys = self.cart
        return quantitys

    def get_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        total = 0
        for key, value in self.cart.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.Offer:
                        total = total + (product.OfferPrice * value)
                    else:
                        total = total + (product.Price * value)
        return total

    def update(self, product, quantity):
        Product_id = str(product)
        product_qty = int(quantity)

        ourcart = self.cart
        ourcart[Product_id] = product_qty
        self.session.modified = True
        return ourcart

    def delete(self, product):
        Product_id = str(product)
        if Product_id in self.cart:
            del self.cart[Product_id]

        self.session.modified = True
