from django.db import models

# Create your models here.

class Member(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    level = models.IntegerField(default=0)

    joined = models.DateField(auto_now_add=True)
 
class Photo(models.Model):
    pass

class User(models.Model):
    member = models.OneToOneField(Member)

    name = models.CharField(max_length=32)
    birthday = models.DateField()
    intro = models.TextField()

    phone = models.CharField(max_length=12)

    # photo = models.ForeignKey(Photo, db_column='photo_id')
    

