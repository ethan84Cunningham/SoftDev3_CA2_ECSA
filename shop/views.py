from django.shortcuts import render, get_object_or_404
from .models import Category,Film
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, InvalidPage

class FilmCat(ListView):
    model = Film

    def get(self,request, category_id=None):
        category = None 
        films = None
        if category_id != None:
            category = get_object_or_404(Category, id = category_id)
            films = Film.objects.filter(category = category, available = True)
        else:
            films = Film.objects.all().filter(available=True)

        paginator = Paginator(films, 6)
        try: 
            page = int(request.GET.get('page','1'))
        except:
            page = 1
        try:
            films = paginator.page(page)
        except(EmptyPage,InvalidPage):
            films = paginator.page(paginator.num_pages)

        return render(request,"shop/category.html",{'category':category, 'films':films})

class FilmDetail(DetailView):
    model = Film

    def get(self, request, category_id, film_id):
        try:
            film = Film.objects.get(category_id = category_id, id = film_id)
        except Exception as e:
            raise e
        return render(request, "shop/film.html", {'film':film})