from django.http import HttpResponse
class MiddleWareLifeCycle:
    def __init__( self, get_response):
        print ( 'MiddleWareLifeCycle.__init__(), Init Method.' )
        self.get_response = get_response

    def __call__( self, request ):
        print( 'MiddleWareLifeCycle.__cal__(), Before the view is executed' )
        response = self.get_response( request )
        print( 'MiddleWareLifeCycle.__cal__(), After  the view is executed' )
        return response

class ExceptionHandlingMiddleWare:
    def __init__( self, get_response):
        print ( 'ExceptionHandlingMiddleWare.__init__(), Init Method.' )
        self.get_response = get_response

    def __call__( self, request ):
        return self.get_response( request )

    def process_exception(self, request, exception):
        print( 'middleware.process_exception()..' )
        print( exception.__class__.__name__ )
        print( exception )
        return HttpResponse( '<b>We are currently having some issues. Please check back in a few minutes.</b>' )





