from django.db import models
class User(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    phone_number = models.CharField(max_length=15,primary_key=True,null=False,blank=False)
    password = models.CharField(max_length=100,null=False,blank=False)
    create_date = models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.name