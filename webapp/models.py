from django.db import models

# Create your models here.
class word(models.Model):
    text=models.CharField(max_length=255)

    def __str__(self) :
        return self.text