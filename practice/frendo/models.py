from django.db import models

# Create your models here.

class Userslogin(models.Model):

    user_img = models.ImageField(upload_to = "frendo/images")
    user_id  = models.AutoField
    user_name =models.CharField(max_length=50)
    user_pwd = models.CharField(max_length=30)
