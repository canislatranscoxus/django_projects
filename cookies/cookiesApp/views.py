from django.shortcuts   import render
from django.http        import HttpResponse

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

