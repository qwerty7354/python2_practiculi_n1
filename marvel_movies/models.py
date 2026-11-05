from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')


    def __str__(self):
        return f"{self.title} ({self.release_date.year})"

class MovieRating(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, primary_key=True, related_name='rating_info')
    imdb_score = models.DecimalField(max_digits=3, decimal_places=1)
    votes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Rating for {self.movie.title}: {self.imdb_score} IMDb"