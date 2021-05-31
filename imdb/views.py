from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from imdb.models import Genre, Movie
from imdb.serializers import GenreSerializer, MovieSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST','DELETE'])
def movies_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        movie_title = request.GET.get('name',None)
        if movie_title is not None:
            movies = movies.filter(movie_title__icontains=movie_title)
        movies_serializer = MovieSerializer(movies,many=True)
        return JsonResponse(movies_serializer.data, safe=False)
    elif request.method == 'POST':
        movie_data = JSONParser().parse(request)
        movies_serializer = MovieSerializer(data=movie_data)
        if movies_serializer.is_valid():
            movies_serializer.save()
            return JsonResponse(movies_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(movies_serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Movie.objects.all().delete()
        return JsonResponse({'message': '{} Movies were deleted successfully!'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, name):
    try:
        movie = Movie.objects.filter(name__icontains=name)
        if request.method == 'GET':
            movie_serializer = MovieSerializer(movie,many=True)
            return JsonResponse(movie_serializer.data, safe=False)
        elif request.method == 'PUT':
            movie_data = JSONParser.parse(request)
            movie_serializer = MovieSerializer(movie, data=movie_data)
            if movie_serializer.is_valid():
                movie_serializer.save()
                return JsonResponse(movie_serializer.data)
            return JsonResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            movie.delete()
            return JsonResponse({'message':'Movie was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except Movie.DoesNotExist:
        return JsonResponse({'message': 'The movie does not exist'}, status=status.HTTP_404_NOT_FOUND)