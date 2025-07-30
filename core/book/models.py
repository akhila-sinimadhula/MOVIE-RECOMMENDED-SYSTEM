from django.db import models

class Emenitites(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_description = models.TextField()
    movie_image = models.URLField(blank=True, null=True)  # Store external image URL
    price = models.DecimalField(max_digits=10, decimal_places=2)
    emenities = models.ManyToManyField(Emenitites, blank=True)

    def __str__(self):
        return self.movie_name
