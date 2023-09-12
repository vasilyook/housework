from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    time_dependence = models.BooleanField(default=False)
    last_time = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


