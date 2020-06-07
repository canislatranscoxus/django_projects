from django.shortcuts   import render
from fbvApp             import Student

# Create your views here.
def getStudents(request):
    students = Student.objects.all()
    my_dict  = { 'students' : students }
    return render( request, 'fbvApp/index.html', my_dict )