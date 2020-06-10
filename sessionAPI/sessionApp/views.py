from django.shortcuts   import render
from django.http        import HttpResponse
from .forms             import ItemForm


# Create your views here.
def pageCount( request ):
    count = request.session.get( 'count', 0 )
    count = count + 1
    request.session[ 'count' ] = count
    my_dict = { 'count' : count }
    return render( request, 'sessionApp/count.html', my_dict )


def index( request ):
    request.session.set_expiry( 180 ) # 180seconds
    #del request.session[ 'count' ]
    return render( request, 'sessionApp/index.html' )

def addItem( request ):
    form = ItemForm()
    my_dict = { 'form' : form }

    if request.method == 'POST':
        name     = request.POST[ 'name'     ]
        quantity = request.POST[ 'quantity' ]
        request.session[ name ] = quantity

    return render( request, 'sessionApp/addItem.html', my_dict )

def displayCart( request ):
    return render( request, 'sessionApp/displayItems.html' )



