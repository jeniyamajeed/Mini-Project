from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    course = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='profile')

class News(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    pic = models.ImageField(upload_to='news')

    def __str__(self) -> str:
        return self.title

class Event(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    pic = models.ImageField(upload_to='events')
    mission = models.TextField()
    vission = models.TextField()

    def __str__(self) -> str:
        return self.title

class Photo(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=300)
    pic = models.ImageField(upload_to='photos')

    def __str__(self) -> str:
        return self.name

class Response(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    response = models.TextField()

class FeedBack(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    feedback = models.TextField()
    response = models.ForeignKey(Response, on_delete=models.CASCADE, null=True, blank=True)