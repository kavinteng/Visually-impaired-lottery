from django.db import models

# Create your models here.
class lottery(models.Model):
    num = models.CharField(max_length=6)

    def __str__(self):
        return self.num