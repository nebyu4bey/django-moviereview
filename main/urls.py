from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [ 
    path('', views.home, name="home"),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('addmovies/', views.addmovie, name="addmovie"),
    path('editmovies/<int:id>/', views.edit_movie, name="edit_movie"),
    path('deletemovie/<int:id>/', views.delete_movie, name="delete_movie"),
]