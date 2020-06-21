from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def home(request):
    
    allmovies = Movie.objects.all()

    context = {"movies":allmovies,}
    
    
    return render(request, 'main/index.html', context)

def detail(request,id):
    movie = Movie.objects.get(id=id)
    context = {
        "movie":movie,
    }
    return render(request, 'main/detail.html', context)


def addmovie(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form = MovieForm(request.POST or None)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()

                    return redirect("main:home")
            else:
                form = MovieForm()
                return render(request,'main/addmovie.html',{"form":form,"controller":"Add Movie"})

        else:
            return redirect("main:home")

    else:
        return redirect("accounts:login")



def edit_movie(request,id):
    movie = Movie.objects.get(id = id)

    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form = MovieForm(request.POST or None, instance = movie)

                if form.is_valid():
                    data = form.save(commit = False)
                    data.save()
                    return redirect("main:detail",id)


            else:
                form = MovieForm(request.POST or None, instance=movie)
                return render(request, 'main/addmovie.html', {"form":form,"controller":"Edit Movie"})

        else:
            return redirect("main:home")
    else:
        return redirect("accounts:login")

def delete_movie(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            movie = Movie.objects.get(  id = id )
            movie.delete()
            return redirect("main:home")
        else:
            return redirect("main:home")
    else:
        return redirect("main:login")