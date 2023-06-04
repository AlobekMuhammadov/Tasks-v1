from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def plans(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Plan.objects.create(
                sarlavha = request.POST.get('s'),
                batafsil = request.POST.get('b'),
                holat = request.POST.get('h'),
                sana = request.POST.get('sa'),
                foydalanuvchi = request.user,
            )
            return redirect('plans')

        if request.method == 'GET':
            content = {
                'todolar':Plan.objects.filter(foydalanuvchi=request.user)
            }
            return render(request,'index.html',content)
    else:
        return redirect('login')

def todo_ochir(request,son):
    Plan.objects.filter(id=son,foydalanuvchi=request.user).delete()
    return redirect('/plans/')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username= request.POST.get('username'),
            password = request.POST.get('password')
            )
        if user is None:
            messages.error(request, 'login yoki parolda hatolik bor')
            return redirect('login')
        login(request, user)
        return redirect('plans')
    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('logout')


def register_view(request):
    if request.method == 'POST' and request.POST.get('password') == request.POST.get('password2'):
        User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )

        return redirect('login')
    return render(request,'register.html')


