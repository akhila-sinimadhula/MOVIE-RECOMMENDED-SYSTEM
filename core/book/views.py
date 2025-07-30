from django.shortcuts import render, redirect
from django.http import JsonResponse  # ✅ Missing import added
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Emenitites, Movie

# Home - Display all movies
@login_required(login_url="/login/")
def home(request):
    emenities = Emenitites.objects.all()
    movies = Movie.objects.all()  # Fetch all movies

    return render(request, 'home.html', {
        'emenities': emenities,
        'movies': movies
    })

# API - Return movies in JSON
@login_required(login_url="/login/")
def api_movies(request):
    movies_objs = Movie.objects.all()

    # Filter by price if provided
    price = request.GET.get('price')
    if price:
        try:
            movies_objs = movies_objs.filter(price__lte=float(price))
        except ValueError:
            pass  # Ignore invalid price inputs

    # Filter by amenities if provided
    emenities = request.GET.get('emenities')
    if emenities:
        emenities_ids = [int(e) for e in emenities.split(',') if e.isdigit()]
        if emenities_ids:
            movies_objs = movies_objs.filter(emenities__in=emenities_ids).distinct()

    # Prepare JSON payload
    payload = [
        {
            'movie_name': movie.movie_name,
            'movie_description': movie.movie_description,
            'movie_image': movie.movie_image,
            'price': str(movie.price)  # ✅ Convert Decimal to string for JSON
        }
        for movie in movies_objs
    ]
    return JsonResponse(payload, safe=False)

# Login Page
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()
        if not user_obj:
            messages.error(request, "Username not found")
            return redirect('/login/')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Wrong Password")
            return redirect('/login/')

    return render(request, "login.html")

# Register Page
def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is taken")
            return redirect('/register/')

        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, "Account created successfully")
        return redirect('/login/')

    return render(request, "register.html")

# Logout
def custom_logout(request):
    logout(request)
    return redirect('login')
