from django.shortcuts   import render
from django.http        import HttpResponse
from .forms              import ItemForm


# Create your views here.

# set one cookie
def home( request ):
    request.session.set_test_cookie()
    return HttpResponse( '<h2>Home Page, Cookie Monster </h2>' )

def page2( request):
    s = 'cookies are enabled'
    if request.session.test_cookie_worked():
        print( s )
    request.session.delete_test_cookie()
    return HttpResponse( '<b>page2. {} </b>'.format( s ) )

def countView( request ):
    if 'count' in request.COOKIES:
        count = 1 + int( request.COOKIES[ 'count' ] )
    else:
        count = 1

    my_dict = { 'count' : count }
    response = render( request, 'cookiesApp/count.html', my_dict )
    response.set_cookie( 'count', count )
    return response

def index( request ):
    return render( request, 'cookiesApp/index.html' )

def addItem( request ):
    form = ItemForm()
    my_dict = { 'form' : form }
    response = render( request, 'cookiesApp/addItem.html', my_dict )
    if request.method == 'POST':
        form = ItemForm( request.POST )
        if form.is_valid():
            name        = form.cleaned_data[ 'name'     ]
            quantity    = form.cleaned_data[ 'quantity' ]
            two_minutes = 120
            response.set_cookie( name, quantity, two_minutes )

    return response

def displayCart( request ):
    return render( request, 'cookiesApp/displayItems.html' )

