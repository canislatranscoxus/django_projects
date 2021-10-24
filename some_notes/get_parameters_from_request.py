import json

from django.conf                    import settings
from django.shortcuts               import render, redirect, get_object_or_404
from django.urls                    import reverse, reverse_lazy
from django.utils.regex_helper import contains
from django.views                   import View
from django.contrib.sites.models    import Site

class MyView( View ):

    context_object_name = 'my pretty view'
    success_url         = 'my_app1:ok'
    fail_url            = 'my_app1:fail'

    def get(self, request, *args, **kwargs):
        pet_id    = self.kwargs[ 'pet_id' ]
        pet_name  = int( request.session  [ 'pet_name' ] )
        food      = request.GET[ 'food' ]
        
        if pet_id != '':
            url = self.success_url
        else:
            url = self.fail_url
        return redirect( reverse( url ) )
        
        
    def post(self, request, *args, **kwargs):
        pet_id    = self.kwargs[ 'pet_id' ]
        pet_name  = int( request.session  [ 'pet_name' ] )
        age       = request.POST[ 'age' ]

	# do something
	
        return redirect( reverse( success_url ) )

