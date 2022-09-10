from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Atik
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#module de cryptage
from hashlib import sha3_256
import getpass
import os
import shutil
import zipfile


def  hash_1(f_first,last_1,password_user) :
    try:
        keys = sha3_256(password_user.encode('utf-8')).digest()
        with open(f_first,'rb') as f_first:
            with open(last_1,'wb') as last_1:
                i = 0
                while f_first.peek():
                    f = ord(f_first.read(1))
                    l = i % len(keys)
                    b = bytes([f^keys[l]])
                    last_1.write(b)
                    i +=1

    except:
        print('sa pa yon fichye')

        return



def zip_dossier(filename):
    format = "zip"
    directory = os.getcwd()
    shutil.make_archive(filename, format, directory)
    return

def dekrypte_dossier(test_file_name):
    try:
        with zipfile.ZipFile(test_file_name, 'r') as zip:
            zip.printdir()
            zip.extractall() 
    except zipfile.BadZipFile:
        print('zipfile.BadZipFile')
        return


# Create your views here.
def akey(request):
    if request.user.is_authenticated:
        konekte = True
    else:
        konekte = False
    context = {"konekte": konekte}
    return render(request,'index.html',context)

	
def continue1(request):
	return render(request,'continue.html')
	
def about(request):
	return render(request,'about.html')	

def encryptfile(request):
	return render(request,'encryptfile.html')
			
def encryptfolder(request):
	return render(request,'encryptfolder.html')
	
def konekte(request):
    if request.method == "POST":
        non = request.POST['non']
        password = request.POST['password']
        user = authenticate(username=non, password=password)
        if user is not None:
            login(request, user)
            print("Itilizatè a otantifye, li konekte")
            return redirect(akey)
        else:
            print("Idantifyan yo pa bon")
    context = {'user':User.objects.filter(is_active=True)}
    return render(request, "konekte.html", context)

def dekonekte(request):
    logout(request)
    messages.success(request,'Ou dekonekte ak sikse')
    return redirect(akey)

def inskri(request):
    if request.method=='POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confpassword=request.POST.get('confpassword')
        if password!=confpassword:
            messages.error(request,'konfime modpass ou a')
          
        else:
            User.objects.create_user(username=username,email=email,password=password)
            messages.success(request,'Ou inskri ak sikse')
            return redirect(akey)
    return render(request,'inskri.html')