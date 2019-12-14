from django.shortcuts import render,redirect
from .models import shows
import datetime
from django.contrib import messages


# Create your views here.
def home(request):
    context={'shows':shows.objects.all()}
    # context={'users':Users.objects.all()}
    print(context)
    return render(request,"shows/home.html",context)

def new(request):
    return render(request,"shows/new.html")

def add_show(request):
    errors=shows.objects.valid_show(request.POST)
    if len(errors)>0:
        print(errors)
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/new")

    new_show=shows.objects.create(title=request.POST['title'],network=request.POST['network'],release_date=request.POST['release_date'],desc=request.POST['desc'],poster=request.FILES['poster'])

    print(new_show.poster)
    return redirect("/")

def showDetails(request,show_id):
    # context={'book':Books.objects.get(id=book_id)
    context={'show':shows.objects.get(id=show_id)}
    
    print(context)
    return render(request,"shows/showDetails.html",context)

def delete_show(request,show_id):
    show=shows.objects.get(id=show_id)
    show.delete()
    return redirect("/")

def editShow(request,show_id):
    context={'show':shows.objects.get(id=show_id)}
    print(context)
    return render(request,"shows/editShow.html",context)
    
def update_show(request):
    show=shows.objects.get(id=request.POST['id'])
    print(f"update {show.id}")
    show.title=request.POST['title']
    show.network=request.POST['network']
    show.release_date= request.POST['release_date']
    show.desc=request.POST['desc']
    show.save() 

    return redirect("/")
    

