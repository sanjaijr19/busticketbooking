from django.db import models



# Create your models here.
class Driver(models.Model):
    drivername=models.CharField(max_length=20)
    age=models.IntegerField()
    contact_no=models.IntegerField()
    bus_no=models.IntegerField()

    # def __str__(self):
    #     return drivername
class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    email=models.EmailField()
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
