from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to='media/')
    description=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    #tags=models.ManyToManyField(Category)

    def __str__(self):
        return self.name
