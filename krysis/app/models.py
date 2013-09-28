from django.db import models

class Tweet(models.Model):
   text=models.CharField(max_length=140, unique=True)
   sender=models.CharField(max_length=50)
   latitude=models.DecimalField(max_digits=11,decimal_places=8,null=True)
   longitude=models.DecimalField(max_digits=11,decimal_places=8,null=True)
   keywords=models.ManyToManyField('Keyword')
   date=models.CharField(max_length=100, null=True)

class Text(models.Model):
   text=models.CharField(max_length=255, unique=True)
   sender=models.CharField(max_length=15)
   latitude=models.DecimalField(max_digits=11,decimal_places=8,null=True)
   longitude=models.DecimalField(max_digits=11,decimal_places=8,null=True)
   keywords=models.ManyToManyField('Keyword')
   date=models.CharField(max_length=100, null=True)

class Keyword(models.Model):
   word=models.CharField(max_length=100)
