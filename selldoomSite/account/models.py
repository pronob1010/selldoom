from django.db import models
from datetime import datetime  
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


class user_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePic = models.ImageField(upload_to='userImg/', null=True, blank = True)
    self_bio = models.CharField(max_length=1500, editable=True, default='You can update your self bio. It might represent you.')
    self_level = models.IntegerField(default=0)
    total_order = models.IntegerField(default=0)
    total_perchased = models.IntegerField(default=0)
    seller = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)