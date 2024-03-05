import uuid
from django.db import models

# Create your models here.
class Parent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)


class Child(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
