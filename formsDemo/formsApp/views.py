from django.shortcuts import render
from . import forms
# Create your views here.

def userRegistrationView( request ):
    form = forms.UserRegistrationForm()
    if request.method=='POST':
        form = forms.UserRegistrationForm( request.POST )
        if form.is_valid():
            print( 'form is valid' )
            print( 'first Name  : {}'.format( form.cleaned_data[ 'firstName' ] ) )
            print( 'last  Name  : {}'.format( form.cleaned_data[ 'lastName'  ] ) )
            print( 'salary      : {}'.format( form.cleaned_data[ 'salary'    ] ) )
            print( 'email       : {}'.format( form.cleaned_data[ 'email'     ] ) )
            print( 'pic         : {}'.format( form.cleaned_data[ 'pic'       ] ) )

    return render( request, 'formsDemo/userRegistration.html', {'form' : form } )