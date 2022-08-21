from tkinter.tix import Tree
from django.contrib import messages
from urllib import response
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.models import *
from .models import *
import random

SMS_User="nananani"
SMS_Pwd="Ananya@2010"

sms_url="http://login.bulksmsservice.net.in/api/mt/SendSMS"

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
    if request.method == "POST":
        Otp=random.randint(1111,9999)
        Name=request.POST["txtname"]
        print(Otp)
        Email=request.POST["txtemail"]
        Mobilenumber=request.POST["txtmob"]
        request.session["Name"]=Name
        request.session["Email"]=Email
        create=SMS_OTP.objects.create(Name=Name,Email=Email,MobileNumber=Mobilenumber,OTP=Otp)
        # sms="Hi ,We are Ananyashelters ,here is your OTP {Otp}".format(Otp=Otp)
        # params={
        #     "user":,
        #     "password":,
        #     "senderid":,

        # }
        # sms=requests.post(sms_url,)
        print(create.OTP_Id)
        request.session["OTP_Id"]=create.OTP_Id
        otpsent=True
        context={'otpsent':otpsent}
        return render(request, 'pages/projectdetails.html',context=context)
    else:
        return render(request, 'pages/projectdetails.html')
    


def checkotp(request):
    if request.method == "POST":
        Confirm_OTP=request.POST["confirmotp"]
        print(type(Confirm_OTP))
        OTP_Id=request.session["OTP_Id"]
        otp_data=SMS_OTP.objects.get(OTP_Id=OTP_Id)
        Otp=otp_data.OTP
        print(Otp)
        otpsent=True
        context={'otpsent':otpsent}
        if Otp == int(Confirm_OTP):
            context["status"]="Success"
            context["message"]="OTP match"
            return render(request, 'pages/projectdetails.html',context=context)
        else:
            context["status"]="Failure"
            context["message"]="OTP Mismatch"
            return render(request, 'pages/projectdetails.html',context=context)
    else:
        return render(request, 'pages/projectdetails.html')
