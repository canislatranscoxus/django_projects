'''
description:

"redirect" needs the complete url.
"reverse"  can take a url and a tuple or arguments.

return redirect( reverse( 'app_01:my_pet', args=( pet, )   ) )

links:

https://github.com/canislatranscoxus/dj_prj/blob/main/prj_01/app_01/views.py
'''

from django.shortcuts           import render, redirect, get_object_or_404
from django.urls                import reverse, reverse_lazy
from django.views               import View

from .forms                     import *

# Create your views here.

class TakePetView( View ):
    context_object_name = 'take_pet'
    template_name = 'take_pet.html'

    def get(self, request, *args, **kwargs):
        form = TakePetForm()
        my_dic = { 'form' : form }
        return render( request, self.template_name, my_dic  )     

    def post(self, request, *args, **kwargs):
        #address_id          = kwargs.get( 'pk', None )
        my_dic = {}
        form = TakePetForm( request.POST )
        if form.is_valid():
            
            # get the seleceted option
            value = int( form.cleaned_data[ 'pet' ] )
            label = ''
            for _value, _label in form.PET_CHOICES: 
                if value == _value:
                    label = _label
                    break

            print( 'option value: {}'.format( value ) )
            print( 'option label: {}'.format( label ) )
            pet = label

        my_url = reverse( 'app_01:my_pet', args=( pet, )   ) 
        print( 'my_url: {}'.format( my_url ) )
        return redirect( reverse( 'app_01:my_pet', args=( pet, )   ) )


