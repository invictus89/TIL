from django.shortcuts import render, redirect
from .models import Movie, Score, Genre
from django.db.models import Avg, Sum

def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies,}
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    genre = Genre.objects.get(pk=movie.genre_id)
    scores = movie.score_set.order_by('-pk')

    context = {'movie': movie, 'genre': genre, 'scores': scores,}
    return render(request, 'movies/detail.html', context)

def delete(request, movie_pk):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_pk)
        movie.delete()

def create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    my_score = request.POST.get('score')
    my_content = request.POST.get('content')
    score = Score(movie=movie, content=my_content, score=my_score)
    score.save()
    return redirect('detail', movie_pk)

def delete(request, movie_pk, score_pk):
    score = Score.objects.get(pk=score_pk)
    score.delete()
    return redirect('detail', movie_pk)

def update(request, movie_pk):
    if request.method == 'POST':
        print("POST 방식")
        title = request.POST.get('title')
        audience = request.POST.get('audience')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')
        genre_name = request.POST.get('genre')
        genre = Genre.objects.get(name=genre_name)

        movie = Movie.objects.get(pk=movie_pk)
        movie.title = title
        movie.audience = audience
        movie.poster_url = poster_url
        movie.description = description
        movie.genre_id = genre.pk

        movie.save()

        return redirect('detail', movie_pk)
    else:
        movie = Movie.objects.get(pk=movie_pk)
        genres = Genre.objects.all()
        context = {'genres': genres, 'movie': movie, }
        return render(request, 'movies/update.html', context)
