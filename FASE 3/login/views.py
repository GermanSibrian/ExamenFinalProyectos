from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def logon(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        userSession = authenticate(request,username= username,password=password)
        if userSession:
            login(request,userSession)
            return redirect("homepage")
        else:
            return render(request,"index.html")
    return render(request,"index.html")

def logout_view(request):
    logout(request)
    return redirect("login")

