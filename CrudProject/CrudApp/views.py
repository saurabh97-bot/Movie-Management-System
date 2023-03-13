from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,get_object_or_404
from .models import Movie,Slides
from .forms import MovieForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.


def movie_list(request):
    movie = Movie.objects.all()
    movie_paginator = Paginator(movie,3)
    page = movie_paginator.get_page(1)
    if request.method == 'GET':
        st = request.GET.get('searchname')
        if st != None:
            movie = Movie.objects.filter(name__icontains=st)
    return render(request,'movielist.html',{'count':movie_paginator.count,'page':page,'movie':movie})

def movie_detail(request,id):
    movie = get_object_or_404(Movie,pk=id)
    return render(request,'moviedetail.html',{'movie':movie})


def add_movie(request):
    form = MovieForm
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/movie')
    return render(request,'addmovie.html',{'form':form})


def update_movie(request,id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(instance=movie)
    if request == 'POST':
        form = MovieForm(request.POST,instance=movie)
        if form.is_valid():
            form.save()
            # messages.success(request,'Data has been updated!')
            return redirect('/movie')
    return render(request,'updatemovie.html',{'form':form})

def delete_movie(request,id):
    movie = Movie.objects.filter(id=id).delete()
    return redirect('/')


def SlidesPage(request):
    sld = Slides.objects.all()
    return render(request,'Slides.html',{'sld':sld})

def Signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Your Password does not match")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('/Signin')
    return render(request,'Signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render (request,'Signin.html')