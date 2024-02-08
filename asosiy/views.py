import datetime

from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View

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
                'todolar':Plan.objects.filter(foydalanuvchi=request.user),
                'user':request.user.username
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
            messages.error(request, 'Login yoki Parolda  hatolik bor')
            return redirect('login')
        login(request, user)
        return redirect('plans')
    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.method == 'POST' and request.POST.get('password') == request.POST.get('password2'):
        User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )

        return redirect('login')
    return render(request,'register.html')

class EditPlanView(View):
    def get(self,request, pk):
        plan = Plan.objects.filter(id=pk, foydalanuvchi=request.user)
        content = {
            'plans':plan
        }
        return render(request, 'edit.html', content)

    def post(self,request,pk):
        Plan.objects.filter(id=pk, foydalanuvchi=request.user).update(
            sarlavha=request.POST.get('s'),
            batafsil=request.POST.get('b'),
            holat=request.POST.get('h'),
            foydalanuvchi=request.user,
        )
        return redirect('plans')


