from django.shortcuts       import render
from django.views.generic   import ListView, DetailView, CreateView, UpdateView, DeleteView
from cbvApp.models          import Student
from django.urls            import reverse_lazy

# Create your views here.
class StudentListView( ListView ):

    model = Student
    ''' to change the default values, use the variables: 
        template_name
        context_object_name
    '''
    # default template_name is student_list.html
    # default context_object_name is stuent_list

class StudentDetailView( DetailView ):
    model = Student
    # default template_name is student_detail.html
    # default context_object_name is stuent

class StudentCreateView( CreateView ):
    model = Student
    fields = ( 'firstName', 'lastName', 'testScore' )
    # this view uses student_form.html

class StudentUpdateView( UpdateView ):
    model = Student
    fields = (  'testScore', )
    # this view uses student_form.html

class StudentDeleteView( DeleteView ):
    model = Student
    success_url = reverse_lazy( 'students' )