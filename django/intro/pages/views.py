from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request,'index.html')

# Template variable
def dinner(request):
    menu = ['선산곱창','버거킹','와촌','지코바']
    pick = random.choice(menu)
    return render(request,'dinner.html',{'dinner':pick})
    
#variable routing
def hello(request, name):
    return render(request, 'hello.html',{'name':name})
    
def hi_dinner(request, user):
    menu = ['취두부','홍어','조리퐁']
    pick = random.choice(menu)
    return render(request, 'hi_dinner.html',{'user':user,'pick':pick})
    
def lol(request, user_name):
    champ = ['루시안', '노틸러스', '레오나', '타릭', '베이가', '마스터이', '에코', '하창언']
    pick = random.choice(champ)
    return render(request, 'lol.html',{'user_name':user_name,'pick':pick })
    
# Form tag    
def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    return render(request, 'catch.html',{'message':message})

#Form 외부로 요청    
def naver(request):
    return render(request, 'naver.html')

def bootstrap(request):
    return render(request,'bootstrap.html')