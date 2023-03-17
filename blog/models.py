from django.db import models

class Writer(models.Model):
    name = models.CharField(max_length=60,null=True,blank=True)

class Post(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    subtitle = models.CharField(max_length=40,null=True,blank=True)
    writer = models.ForeignKey(Writer,on_delete=models.CASCADE,default=1)
    image = models.ImageField(null=True,blank=True,upload_to='blog-main/')
    summary = models.TextField(max_length=500,null=True,blank=True)
    text = models.TextField(max_length=1500,null=True,blank=True)

