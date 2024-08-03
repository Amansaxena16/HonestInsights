from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signUp.html')

def dashboard(request):
    return render(request,'dashboard.html')