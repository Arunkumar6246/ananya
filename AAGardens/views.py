from email import message
from urllib import response
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.models import *
from .models import *

import json

# Create your views here.

def dash_home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/aboutus.html')

def gallary(request):
    return render(request, 'pages/gallary.html')

def projects(request):
    return render(request, 'pages/projects.html')

def contact(request):
    return render(request, 'pages/contact.html')


def Projectdetails(request):
    return render(request, 'pages/projectdetails.html')