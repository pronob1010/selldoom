from django.db import models
from datetime import datetime  
from django.utils import timezone
from django.contrib.auth.models import User


class Website_Details(models.Model):
    site_Title = models.CharField(max_length=200)
    site_Logo = models.ImageField(upload_to='logo')
    site_background = models.ImageField(upload_to='background', null=True)
    physical_address = models.CharField(max_length=500, blank = True)
    site_Description = models.CharField(max_length=500)
    about_Us_short = models.CharField(max_length=500)
    what_we_really_do =  models.CharField(max_length=1500)
    history_of_the_company =  models.CharField(max_length=1500)
    our_vision =  models.CharField(max_length=1500)
    cooperation_detais =  models.CharField(max_length=1500)
    support_details = models.CharField(max_length=1500)
    quality_details = models.CharField(max_length=1500)
    delivery_details = models.CharField(max_length=1500)
    customer_care_details = models.CharField(max_length=1500)
    customers_contribution = models.CharField(max_length=1500)

    def __str__(self):
        return self.site_Title

class Social_Media(models.Model):
    helpLine = models.CharField(max_length=200)
    email = models.EmailField(default = None)
    fbLink = models.CharField(max_length=200)
    twiterLink = models.CharField(max_length=200)
    linkedinLink = models.CharField(max_length=200)


class Terms_and_Conditions(models.Model):
    last_modified = models.DateField(auto_now=True)
    customer_agreement = models.CharField(max_length=8000)
    intellectual_Propertly = models.CharField(max_length=8000)
    Termination = models.CharField(max_length=8000)

    def __str__(self):
        return self.last_modified

class Notice(models.Model):
    page_top_Notice = models.CharField(max_length=100)
    shiping_Notice = models.CharField(max_length=100)
    special_cuppon_title = models.CharField(max_length=100, null=True)
    special_cuppon = models.CharField(max_length=50, null=True)
    supportHour =  models.IntegerField()
    off_day = models.CharField(max_length=500, null=True)
    why_off_this_day = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.page_top_Notice



class Frequently_Asked_Questions(models.Model):
    question = models.CharField(max_length=500)
    ans = models.CharField(max_length=500)

    def __str__(self):
        return self.question
    
