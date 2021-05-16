from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http.request import QueryDict
from django.shortcuts import render

@login_required

def homepage(request):
    return render(request, "logout.html")