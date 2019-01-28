from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request, 'create.html')

def new(request):
    message = request.GET.get('message')
    return  render(request,'new.html', {'message':message})