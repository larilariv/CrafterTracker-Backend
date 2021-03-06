import django
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
        )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    # category = ArrayField(models.CharField(max_length=255))
    # complete = models.BooleanField()
    # start_date = models.DateField()
    # end_date = models.DateField()
    # notes = models.TextField()

    def __str__(self):
        return self.name

# class Image(models.Model):
#     project = models.ForeignKey(
#         Project,
#         on_delete=models.CASCADE,
#         related_name='images',
#     )
#     name = models.CharField(max_length=255)
#     image = models.ImageField(upload_to ='images/')

#     def __str__(self):
#         return self.name

# class Resource(models.Model):
#     project = models.ForeignKey(
#         Project,
#         on_delete=models.CASCADE,
#         related_name='resources',
#     )
#     name = models.CharField(max_length=255)
#     link = models.URLField(max_length=400)
#     media_type = models.CharField(max_length=255)
#     notes = models.TextField()

#     def __str__(self):
#         return self.name

# class Material(models.Model):
#     user = models.ForeignKey(User)
#     projects = models.ManyToManyField(Project)
#     name = models.CharField(max_length=255)
#     brand = models.CharField(max_length=255)
#     category = ArrayField(models.CharField(max_length=255))
#     purchase_link = models.URLField(max_length=400)
#     notes = models.TextField()

#     def __str__(self):
#         return self.name
