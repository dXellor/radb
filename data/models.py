from django.db import models
from user_auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Predmet(models.Model):
    naziv = models.CharField(max_length=50)
    ESPB = models.IntegerField()

    def __str__(self):
        return self.naziv

class Ocena(models.Model):
    student_id = models.ForeignKey(to=User, default=1,  on_delete=models.CASCADE)
    predmet_id = models.ForeignKey(to=Predmet, default=1, on_delete=models.CASCADE) 
    ocena = models.IntegerField(default=5, validators=[MinValueValidator(5), MaxValueValidator(10)])

