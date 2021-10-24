'''
description:

render and pass 3 arguments:

request
html template
dictionary with data 

return render( request, 'my_pet.html', my_dic  )   

links:
https://github.com/canislatranscoxus/dj_prj/blob/main/prj_01/app_01/views.py
'''
from django.shortcuts           import render, redirect, get_object_or_404
from django.urls                import reverse, reverse_lazy
from django.views               import View

from .forms                     import *


class MyPetView( View ):
    def get(self, request, *args, **kwargs):
        pet = kwargs.get( 'pet', None )
        my_dic = {
            'pet' : pet
        }
        return render( request, 'my_pet.html', my_dic  )   