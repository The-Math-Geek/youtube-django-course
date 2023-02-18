from django.http import HttpResponse, HttpResponseRedirect, Http404;
from django.shortcuts import render;
from .models import Movie


def movies(request):
    data = Movie.objects.all()
    return render(request, "movies/movies.html", {"movies": data})
    """ For above render statement...""" 
    """First Argument = request""" 
    """Second Argument = Template (Must include navigation for the template this render should be pulling from. i.e. within templates folder, go to movies folder, then movies.html doc"""
    """Third Argument = Data that is passed to the template in order to be rendered. 'movies' is the variable that will be set in double curly braces in the movies.html file. Everything in the square brackets--including the square brackets--will be rendered onto the website screen!"""

def home(request):
    return HttpResponse("Home page")

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, "movies/detail.html", {"movie": data})

def add(request):
    title = request.POST.get("title")
    year = request.POST.get("year")

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect("/movies")

    return render(request, "movies/add.html")

def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404("Hmmm... The movie you attempted to view does not seem to exist. Please try again, or contact your system administrator.")
    movie.delete()
    return HttpResponseRedirect("/movies")