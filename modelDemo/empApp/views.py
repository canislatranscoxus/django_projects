from django.shortcuts   import render
from empApp.models      import Employee

# Create your views here.
def employeedata( request ):
    ''' retrieve all the employees'''
    employees   = Employee.objects.all( )
    empDict     = { 'employees' : employees }
    return render( request, 'empApp/employees.html', empDict )

