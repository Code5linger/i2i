from django.db import models

# Create your models here.


class Phonebook (models.Model):
    name = models.CharField(max_length=255)
    phone = models.TextField
