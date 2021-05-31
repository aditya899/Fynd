from django.conf.urls import url
from django.urls import path
from user import views 
 
urlpatterns = [ 
    url(r'^api/user', views.movies_list),
    url(r'^api/home', views.home, name='home'),
    url(r'^api/find', views.find, name='find'),
]