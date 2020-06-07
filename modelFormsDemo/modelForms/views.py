from django.shortcuts   import render
from modelForms.forms   import ProjectForm
from modelForms.models  import Project

# Create your views here.
def index( request ):
    return render( request, 'modelForms/index.html' )

def listProjects( request ):
    projectsList = Project.objects.all()
    my_dict = { 'projects' : projectsList  }
    return render( request, 'modelForms/listProjects.html', my_dict )

def addProject( request ):
    form = ProjectForm()
    my_dict = { 'form' : form }
    if request.method == 'POST':
        print( 'views.addProject(), method is POST'  )
        form = ProjectForm( request.POST )
        if form.is_valid():
            print('views.addProject(), form is valid')
            form.save()
            return index( request )

        else:
            print('views.addProject(), form NOT valid')



    return render( request, 'modelForms/addProject.html', my_dict )
