from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from .forms import SearchMovieForm
from user.services import *
from imdb.models import Genre, Movie
from imdb.serializers import GenreSerializer, MovieSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def movies_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        movie_title = request.GET.get('name',None)
        if movie_title is not None:
            movies = movies.filter(movie_title__icontains=movie_title)
        movies_serializer = MovieSerializer(movies,many=True)
        return JsonResponse(movies_serializer.data, safe=False)

def home(request):
    form = SearchMovieForm()
    context = {
        "form": form
    }
    return render(request, 'search.html', context)


def find(request):
    if request.method == 'GET':
        form = SearchMovieForm(request.GET)

        if form.is_valid():
            search_key = form.cleaned_data.get('search', '')

        # For a single movie search
        if '+' not in search_key:
            movie_details = find_a_movie(form)
            return render(request, 'result.html', movie_details)

        # For multiple movies search using '+' as a delimiter
        else:
            desired_movies = find_many_movies(form)
            return render(request, 'results.html', {'movies': desired_movies})