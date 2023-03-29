import json
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.forms import CharField


class Array(models.Model):
    input = CharField(max_length=300)

    def destructuring(self):
        str = json.dumps(self)
        str = str.replace(" ", "")
        str = str.replace("[", "")
        str = str.replace("]", "")
        lst = str.split(",")
        lst_int = [int(i) for i in lst]
        return lst_int
    def __str__(self):
        return self
    
