from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    TYPE_CHOICE = {
        "Guitar": "Guitar",
        "Piano": "Piano",
        "Violin": "Violin"
    }
    instrument_type = models.CharField(choices=TYPE_CHOICE, default=None, blank=False, max_length=10)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"