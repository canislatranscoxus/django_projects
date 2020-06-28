from django.http          import request
from django.shortcuts     import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls          import reverse_lazy

from clinicalsApp.models  import ClinicalData, Patient
from clinicalsApp.forms   import ClinicalDataForm



# Create your views here.
# these are views are inheritated from Generics.

class PatientListView( ListView ):
    model = Patient

class PatientCreateView( CreateView ):
    model       = Patient
    success_url = reverse_lazy( 'index' )
    fields      = ( 'firstName', 'lastName', 'age' )

class PatientUpdateView( UpdateView ):
    model       = Patient
    success_url = reverse_lazy( 'index' )
    fields      = ( 'firstName', 'lastName', 'age' )

class PatientDeleteView( DeleteView ):
    model       = Patient
    success_url = reverse_lazy( 'index' )


def addData( request, **kwargs ):
    form    = ClinicalDataForm()
    patient = Patient.objects.get( id = kwargs[ 'pk' ] )
    my_dict = { 'form' : form, 'patient' : patient }
    if request.method == 'POST':
        form = ClinicalDataForm( request.POST )
        if form.is_valid():
            form.save()

        return redirect( '/' )

    return render( request, 'clinicalsApp/clinicaldata_form.html ', my_dict )

def analyze( request, **kwargs):
    data         = ClinicalData.objects.filter( patient_id = kwargs[ 'pk' ] )
    responseData = []
    for eachEntry in data:
        if eachEntry.componentName == 'hw' :
            heightAndWeight = eachEntry.componentValue.split( '/' )
            if len( heightAndWeight ) > 1:
                height = float( heightAndWeight[ 0 ] )
                weight = float( heightAndWeight[ 1 ] )
                BMI = height / weight ** 2
                bmiEntry = ClinicalData()
                bmiEntry.componentName  = 'BMI'
                bmiEntry.componentValue = BMI
                responseData.append( bmiEntry )
        responseData.append( eachEntry )


    my_dict = {'data': responseData}
    return render( request, 'clinicalsApp/generateReport.html', my_dict  )

    #

