from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.TextField()

class Movie(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.TextField()
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()

class Score(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.IntegerField()


