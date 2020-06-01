from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    myDict = { 'name' : 'Crazy Skater' }
    return render( request, 'templatesApp/firstTemplate.html', context=myDict )

def renderEmployee(request):
    myDict = {
        'id'    : 123,
        'name'  : 'Nicole Hause',
        'salary':  190000
    }
    return render( request, 'templatesApp/employeeTemplate.html', myDict )
