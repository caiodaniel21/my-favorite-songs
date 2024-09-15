from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def axe_music(request):
    return render(request, 'axe_music.html')

def chill_vibes(request):
    return render(request, 'chill_vibes.html')

def city_pop(request):
    return render(request, 'city_pop.html')

def indie_rock(request):
    return render(request, 'indie_rock.html')

def jazz(request):
    return render(request, 'jazz.html')

def mpb(request):
    return render(request, 'mpb.html')

def rock(request):
    return render(request, 'rock.html')

def romantic(request):
    return render(request, 'romantic.html')