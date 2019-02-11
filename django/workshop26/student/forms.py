from django import forms
from .models import Student

class StudentForm(forms.Form):
    name = forms.CharField(label='이름')
    age = forms.IntegerField(label='나이')
    
class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age']