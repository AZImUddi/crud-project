from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import*


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'NOT FOUND')
            return redirect('Registration')

    return render(request, "login.html")


def Registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['Password']
        password1 = request.POST['Password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Your account expires in three days.')
                return redirect('Registration')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Your yyyyyyyy three days.')
                return redirect('Registration')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.set_password(password)
                user.save()
                messages.success(request, 'User Created')
                return redirect('login')

    return render(request, "Registration.html")

def userprofile(request):
    picture = Pic.objects.all()
    return render(request, "userprofile.html", locals())


def logout_user(request):
    auth.logout(request)
    return redirect('login')