from django import forms
from fbvApp import models


class StudentForm( forms.ModelForm ):
    class Meta:
        model = models.Student
        fields = '__all__'


