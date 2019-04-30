from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length = 100)
    paradism = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
