from distutils.command.upload import upload
from django.db import models

# Create your models here.
GENRE_CHOICES={
    ('A',"ACTION"),
    ('S',"SCI-FI"),
    ('D',"DRAMA"),
    ('C',"COMEDY"),
}

class Movie(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField(max_length=1000)
    genre=models.CharField(max_length=1, choices=GENRE_CHOICES)
    rating=models.DecimalField(max_digits=3,decimal_places=2,)    
    trailer_link=models.CharField(max_length=255)
    image=models.ImageField(upload_to='images')
    poster=models.ImageField(upload_to="poster")