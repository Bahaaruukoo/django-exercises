from django.db import models

# Create your models here.

class users(models.Model):
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    email = models.EmailField()

    def __str__(self):
        return self.firstname
