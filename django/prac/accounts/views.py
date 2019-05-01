from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required 

def main(request):
    return render(request, 'main.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:main')
        
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)
            return redirect('accounts:main')
    else:
        signup_form = UserCreationForm()
    return render(request, 'signup.html', {'signup_form':signup_form})


def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:main')
        
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            auth_login(request, user)
            return redirect('accounts:main')
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form':login_form})

def logout(request):
    auth_logout(request)
    return redirect('accounts:main')

@login_required
def update(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:main')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'update.html', {'form':form})


def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('accounts:main')
    return render(request, 'delete.html')