from django.db import models


class Name(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
