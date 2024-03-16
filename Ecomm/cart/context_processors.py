from .cart import Cart

# create context processor so our cart can ork on all pages of the site
def cart(request):
    # return default data from our cart
    return {'cart':Cart(request)}