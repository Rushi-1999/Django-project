from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


#password for harry is shivram143


# Create your views here.
def index (request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    return render (request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect ('/')
        else:
            return render (request, 'login.html')
        
    return render (request, 'login.html')
        
def logoutUser(request):
    logout(request)
    return redirect ('/login')


# def Uploadcsv(request):
#     if request.method =='abc':
#         uploaded_file =request.FILES['document']
#         fs= FileSystemStorage()
#         fs.save(uploaded_file.name, uploaded_file)
#     return render (request,'upload.html',{})

    