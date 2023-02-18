from django.http import HttpResponse;
from django.shortcuts import render;

data={
    "movies": [
    {
        "id": 5,
        "title": "Jaws",
        "year": 1969,
    },

    {
        "id": 6,
        "title": "Sharknado",
        "year": 1600,
    },

    {
        "id": 7,
        "title": "The Meg",
        "year": 2000,
    },]

    }


def movies(request):
    return render(request, "movies/movies.html", data)
    """ For above render statement...""" 
    """First Argument = request""" 
    """Second Argument = Template (Must include navigation for the template this render should be pulling from. i.e. within templates folder, go to movies folder, then movies.html doc"""
    """Third Argument = Data that is passed to the template in order to be rendered. 'movies' is the variable that will be set in double curly braces in the movies.html file. Everything in the square brackets--including the square brackets--will be rendered onto the website screen!"""

def home(request):
    return HttpResponse("Home Page")