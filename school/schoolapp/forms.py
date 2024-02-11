from django import forms
from .models import School

class FORMSchool(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_name','school_code','school_type','school_grade']


        


 