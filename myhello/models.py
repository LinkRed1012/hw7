from django.db import models

from django.db import models


class personal_account(models.Model):
    #title = models.CharField(max_length=100)
    #content = models.TextField(blank=True)
    #photo = models.URLField(blank=True)
    #location =models.CharField(max_length=100)
    #created_at = models.DateTimeField(auto_now_add=True)
    account = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

'''class contact(models.Model):     
    cName=models.CharField(max_length=20, null=False)     
    cBirthday=models.DateField(null=False)     
    cEmail=models.EmailField(max_length=100, blank=True, default='')     
    cPhone=models.CharField(max_length=50, blank=True, default='')     
    cAddress=models.CharField(max_length=255, blank=True, default='')     
    def __str__(self):         
        return self.cName'''