from django.db import models

# Create your models here.


class Phonebook (models.Model):
    name = models.CharField(max_length=255)
    phone = models.TextField

    def __str__(self):
        return self.name + '===' + self.phone
