from django import template
register = template.Library()

def custLower( value ):
    result = value[ : 3 ].lower()
    return result

# register a filter using the template library instance
register.filter( "myLower", custLower )

#register the filter using a decorator
@register.filter( name= 'myUpper' )
def custUpper( value ):
    result = value[ : 3 ].upper() + value[3:]
    return result

@register.filter( name= 'myAppend' )
def custAppend( value, arg ):
    result = str(arg) + value
    return result


