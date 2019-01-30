from django.shortcuts import render, redirect
from .models import Student
# Create your views here.



def new(request):
    return render(request,'new.html')
    
def create(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    email = request.POST.get('email')
    
    student = Student(name=name, age=age, email=email)
    student.save()
    
    return redirect(f'/students/{student.pk}')
    

def index(request):
    students = Student.objects.all()
    return  render(request,'index.html', {'students':students})
    
def detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'detail.html', {'student':student})
    
def delete(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('/students/')
    
def edit(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'edit.html', {'student':student})
    
def update(request,student_id):
    student = Student.objects.get(pk=student_id)
    student.name = request.POST.get('name')
    student.age = request.POST.get('age')
    student.email = request.POST.get('email')
    student.save()
    
    return  redirect(f'/students/{student_id}/')