from django.shortcuts import render
from .models import Student
from .forms import StudentForm

# Create your views here.
def new(request):
    form = StudentForm()
    return render(request, 'new.html',{'form':form})