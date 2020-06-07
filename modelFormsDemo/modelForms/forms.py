from django             import forms
from modelForms.models  import Project

class ProjectForm( forms.ModelForm ):
    class Meta:
        model  = Project
        fields = '__all__'
        startDate = forms.DateField( widget = forms.SelectDateWidget() )
        endDate   = forms.DateField( widget = forms.SelectDateWidget() )
