from django.shortcuts import render
from django.contrib.auth import login, authenticate
from app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def Dashboard(request):
    return render(request, 'base.html',{})


