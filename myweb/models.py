from django.db import models

class MovieType(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.text}'

class Movie(models.Model):
    movie_type = models.ForeignKey(MovieType, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.movie_type.text} - {self.name}'