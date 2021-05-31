from django.conf.urls import url
from django.urls import path
from imdb import views 
 
urlpatterns = [ 
    url(r'^api/imdb', views.movies_list),
    path('api/bank/<str:name>', views.movie_detail),
]