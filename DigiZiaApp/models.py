from django.db import models

class Phone(models.Model):
    CHOICES=(
        ('sam','SAMSUNG'),
        ('apl','APPLE'),
        ('shi','SHIOMI'),
        ('hoa','HOAWEI'),
        ('nok','NOKIA'),
    )
    title=models.CharField(max_length=100,)
    image=models.ImageField(upload_to="image")
    is_exist=models.BooleanField('is exist:',default=True)
    price = models.IntegerField()
    brand= models.CharField(max_length=3,choices=CHOICES)
    specification=models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.title


class Laptop(models.Model):
    CHOICES=(
        ('sam','SAMSUNG'),
        ('apl','APPLE'),
        ('asu','ASUS'),
        ('len','LENOVA'),
        ('hpp','HP'),
        ('hpp','DELL'),
        ('hpp','MSI'),
        ('mic','MICROSOFT'),
        ('ace','ACER'),
    )
    title=models.CharField(max_length=100,)
    image=models.ImageField(upload_to="image")
    is_exist=models.BooleanField('is exist:',default=True)
    price = models.IntegerField()
    brand= models.CharField(max_length=3,choices=CHOICES)
    specification=models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.title



class Book(models.Model):
    CHOICES=(
        ('art','ARTS $ PHOTOGRAPHY'),
        ('chi','CHILDERENS BOOK'),
        ('his','HISTORY'),
        ('rom','ROMANCE'),
        ('tee','TEENS & YOUNG ADULT'),
        ('all','ALL CATEGORIES'),
    )
    title = models.CharField(max_length=100,)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to="image")
    is_exist = models.BooleanField('is exist:',default=True)
    price = models.IntegerField()
    category = models.CharField(max_length=3,choices=CHOICES,blank=False,default='all')
    summary = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.title



class Camera(models.Model):
    CHOICES=(
        ('can','CANON'),
        ('nik','NIKON'),
        ('shi','SHIOMI'),
        ('sam','SAMSUNG'),
        ('son','SONY'),
        ('fuj','FUJIFILM'),
    )
    title=models.CharField(max_length=100,)
    image=models.ImageField(upload_to="image")
    is_exist=models.BooleanField('is exist:',default=True)
    price = models.IntegerField()
    brand= models.CharField(max_length=3,choices=CHOICES)
    specification=models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.title
