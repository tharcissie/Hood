from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt

class Hood(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/',default='a.jpg')
    police = models.IntegerField(null=True,blank=True)
    health = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name

    def create_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def find_hood(cls, neighborhood_id):
        return cls.objects.filter(id=hood_id)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='default.jpg')
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='user_hood',null=True, )

    def __str__(self):
         return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


class Business(models.Model):
    name = models.CharField(max_length=200)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='hood_business',null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="business")
    business_email=models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()


    
class Post(models.Model):
    title = models.CharField(max_length=200)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='hood_post',null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    def create_post(self):
        self.save()

    def delete_post(self):
        self.delete()

   


