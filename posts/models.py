from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User




# Create your models here.
#MVC M-MODEL, V-VIEW , C-CONTROLLER

class signUp(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    father_name=models.CharField(max_length=200)
    mother_name=models.CharField(max_length=225)
    email=models.EmailField(blank=True, verbose_name ='e-mail')
    password=models.ForeignKey(User)
    updated=models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.first_name

    
class Register(models.Model):
   
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=225)
    password=models.CharField(max_length=200)
    house_no = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    updated=models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.name

    


import datetime
from django.contrib.auth.models import User     # if you want to user desvription then you should import it.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):                    # python 2.7 is working like __unicode___ and __str___  both
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=256)
    uploader = models.ForeignKey(User)  # This is most importtant Forgeinkey(user) used here autamatically it come
    abstract = models.TextField()
    keywords = models.CharField(max_length=512)
    pdf = models.FileField(upload_to='articles')
    submittedOn = models.DateField(default=datetime.date.today())
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    volume = models.IntegerField(blank=True, null=True)
    issue = models.IntegerField(blank=True, null=True)
    publishedOn = models.DateField(blank=True, null=True)
    isPublished = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.title


class LikeArticle(models.Model):
    user = models.ForeignKey(User)        # for use always should use ForeignKey
    article = models.ForeignKey(Article)


class LikeCategory(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    
    class Meta:
        verbose_name_plural = "likeCategories"


class UserProfile(models.Model):
    
    PROF_CHOICES = (
                        ('ST','Student'),
                        ('AL','Alumnus/alumna'),
                        ('LC','Lecturer'),
                        ('LS','Library Staff'),
                        ('AS','Administrative Staff'),
                        ('MS','Management Staff'),
                        ('OT','Other')
                    )
    
    UG_PG_CHOICES = (
                     ('UG','Undergraduate'),
                     ('PG','Postgraduate')
                     )
    
    CSE = 'CSE'
    CS = 'CS'
    ECE = 'ECE'
    EEE = 'EEE'
    IT = 'IT'
    EIE = 'EIE'
    MECH = 'MECH'
    CIVIL = 'CIV'
    VLSI = 'VLSI'
    ES = 'ES'
    EPE = 'EPE'
    WMC = 'WMC'
    DEPT_CHOICES = (
                    (CSE, 'Computer Science and Engineering'),
                    (CS, 'Computer Science'),
                    (ECE, 'Electronics and Communication Engineering'),
                    (EEE, 'Electrical and Electronics Engineering'),
                    (IT, 'Information Technology'),
                    (EIE, 'Electronics and Instrumentation Engineering'),
                    (MECH, 'Mechanical Engineering'),
                    (CIVIL, 'Civil Engineering'),
                    (VLSI, 'VLSI Design'),
                    (ES, 'Embedded Systems'),
                    (EPE, 'Electrical Power Engineering'),
                    (WMC, 'Wireless and Mobile Communication')
                    )
    
    user = models.OneToOneField(User)
    idnum = models.CharField(max_length=12, blank=True)
    isOutsider = models.BooleanField(default=False)
    profession = models.CharField(max_length=30, choices=PROF_CHOICES, blank=True)
    ugorpg = models.CharField(max_length=2, choices=UG_PG_CHOICES, blank=True)
    dept = models.CharField(max_length=4, choices=DEPT_CHOICES, blank=True)
    exactprofession = models.CharField(max_length=30, blank=True)
    place = models.CharField(max_length=40, blank=True)
    year = models.CharField(max_length=4, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __unicode__(self):
        return self.user.username    
    
