from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from DB.models import Location, Hotel, Room, Review, Wishlist

# from .forms import SignupForm

def index(request):
    Locations = Location.objects.all()
    Hotels = Hotel.objects.all()

    return render(request, 'home/index.html', {
        'Locations': Locations,
        'Hotels': Hotels,
    })

def wish_list(request):
    Locations = Location.objects.all()
    Hotels = Hotel.objects.all()

    return render(request, 'home/wish_list.html', {
        'Locations': Locations,
        'Hotels': Hotels,
    })

def profile(request):
    return render(request,"home/profile.html")

def base(request):
    return render(request,"home/base.html")

def about(request):
    return render(request,"home/about.html")
def contact(request):
    return render(request,"home/contact.html")

def login(request):
    return render(request,"login.html")

def choice_of_login_page(request):
    return render(request,"choice_of_login_page.html")

def profile(request):
    return render(request,"profile.html")