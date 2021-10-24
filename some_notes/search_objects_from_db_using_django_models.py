'''
Search objects in the Database using Django Models

https://docs.djangoproject.com/en/3.2/topics/db/queries/
'''


# search 1 object with get_object_or_404
from django.shortcuts           import get_object_or_404

pet = get_object_or_404( Pet, id = pet_id) 


# one object.
one_book = Book.objects.get( pk = 1 )

# search many with Model Filter

pets = Pets.objects.filter( specie = 'cat' )

# all objects
all_books = Book.objects.all()

# 
