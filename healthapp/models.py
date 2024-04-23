from django.db import models

# Create your models here.
class health(models.Model):
    name = models.CharField(max_length=100)
    Age = models.IntegerField(default=0)
    Address = models.CharField(max_length=200)
    Discharge_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name