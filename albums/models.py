from django.db import models
from musicians.models import Musician

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=255)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    RATING_CHOICES = {
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
    }
    rating = models.CharField(choices=RATING_CHOICES, max_length=10)
    def __str__(self):
        return f'{self.name}'


# Album model will have 
# Album Name
# One-to-Many Relationships with musician model
# Album release date
# Rating between 1-5