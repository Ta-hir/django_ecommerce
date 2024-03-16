from store.models import Product,Profile

class Cart():
    def __init__(self, request):
        self.session = request.session
        # get request
        self.request = request
        # get current session key if it exists
        cart = self.session.get('session_key')

        # if the user is new, no session socreate one

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

    # make sure cartis available on all pages of the site
        self.cart = cart

    def db_add(self, product, quantity):
        product_id = str(product)
        product_quantity = str(quantity)
        # logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_quantity)       

        self.session.modified = True

        # deal with logged in user
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            # save carty to profile model
            current_user.update(old_cart=str(carty))
        

    def add(self, product,quantity):
        product_id = str(product.id)
        product_quantity = str(quantity)
        # logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_quantity)       

        self.session.modified = True

        # deal with logged in user
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            # save carty to profile model
            current_user.update(old_cart=str(carty))

        

    def __len__ (self):
        return len(self.cart)
    
    def get_products(self):
        # get product ids romcart
        product_ids = self.cart.keys()
        # lookup products usingids
        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quants(self):
        quantites = self.cart
        return quantites
    
    def update(self, product,quantity):
        product_id = str(product)
        product_qty = int(quantity)
            # get cart
        ourcart = self.cart
        # update cart
        ourcart[product_id] = product_qty

        self.session.modified = True

          # deal with logged in user
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            # save carty to profile model
            current_user.update(old_cart=str(carty))


        thing = self.cart
        return thing
    
    def delete(self, product):
        product_id = str(product)
        # deletefrom cart/dictionary
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True

          # deal with logged in user
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            # save carty to profile model
            current_user.update(old_cart=str(carty))


    def cart_total(self):
        # get product ids
        produt_ids = self.cart.keys()
        # lookup keys in product dbmodel
        products= Product.objects.filter(id__in=produt_ids)
        # get quantitites
        total_quantities = self.cart
        total = 0
        for key, value in total_quantities.items():
            key = int(key)
            for product in products:
                if product.id  == key:
                    if product.on_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total

