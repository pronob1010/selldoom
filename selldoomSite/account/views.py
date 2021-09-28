from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def profile(request):
    return render(request, 'profile.html', {})

def updateprofile(request):
    return render(request, 'updateprofile.html', {})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist.")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exist.")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                messages.info(request,"User created")
                return redirect('/')
        else:
            messages.info(request,"Password doesn't match.")
    else:
        return render(request, '/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Doesn't match.")
            return redirect('/')
    else:
        return render(request, '')

def logout(request):
    auth.logout(request)
    return redirect('/')