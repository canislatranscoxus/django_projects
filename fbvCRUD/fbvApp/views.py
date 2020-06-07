from django.shortcuts   import render, redirect
from fbvApp.models      import Student
from fbvApp.forms       import StudentForm


# Create your views here.
def getStudents(request):
    students = Student.objects.all()
    my_dict  = { 'students' : students }
    return render( request, 'fbvApp/index.html', my_dict )


def createStudent(request):
    form    = StudentForm()
    my_dict = { 'form': form }
    if request.method == 'POST':
        form = StudentForm( request.POST )
        if form.is_valid():
            form.save()
        return redirect( '/' )

    return render( request, 'fbvApp/create.html', my_dict )

def deleteStudent( request, id ):
    student = Student.objects.get( id = id)
    student.delete()
    return redirect( '/' )

def updateStudent( request, id ):
    student = Student.objects.get( id = id)
    my_dict = { 'student' : student }
    if request.method == 'POST':
        form = StudentForm( request.POST, instance = student )
        if form.is_valid():
            form.save()
            return redirect( '/' )
    return render( request, 'fbvApp/update.html', my_dict )

def updateStudent2( request, id ):
    student = Student.objects.get( id = id)
    form = StudentForm( instance = student )
    my_dict = { 'form' : form }
    if request.method == 'POST':
        form = StudentForm( request.POST, instance = student )
        if form.is_valid():
            form.save()
            return redirect( '/' )

    return render( request, 'fbvApp/update2.html', my_dict )