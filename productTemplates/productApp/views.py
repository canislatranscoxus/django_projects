from django.shortcuts import render

# Create your views here.
def electronics( request ):
    product_dict = {
        'product1'  : 'mac',
        'product2'  : 'iphone',
        'product3'  : 'dell'
    }
    return render( request, 'productApp/product.html', product_dict )

def toys( request ):
    product_dict = {
        'product1'  : 'skateboard',
        'product2'  : 'drone',
        'product3'  : 'bike'
    }
    return render( request, 'productApp/product.html', product_dict )

def shoes( request ):
    product_dict = {
        'product1'  : 'vans',
        'product2'  : 'nike',
        'product3'  : 'adidas'
    }
    return render( request, 'productApp/product.html', product_dict )

def index( request ):
    return render( request, 'productApp/index.html' )
