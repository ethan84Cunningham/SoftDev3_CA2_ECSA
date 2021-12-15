from django.urls import path 
from .views import FilmCat, FilmDetail

app_name = 'shop'

urlpatterns = [
    path('', FilmCat.as_view(), name='allFilmCat'),
    path('<uuid:category_id>/', FilmCat.as_view(), name = 'films_by_category'),
    path('<uuid:category_id>/<uuid:film_id>/', FilmDetail.as_view(), name= 'film_detail'),
]