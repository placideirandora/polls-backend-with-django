from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    country = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    bio = models.TextField(max_length=300, default="")
    registered_on = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Poll(models.Model):
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(
        Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    choice = models.ForeignKey(
        Choice, related_name='votes', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice

    class Meta:
        unique_together = ("poll", "voted_by")
