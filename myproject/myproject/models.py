from django.db import models


class Array(models.Model):
    input = models.CharField(max_length=1000)
    output = models.CharField(max_length=1000)

    def __str__(self):
        return self.input