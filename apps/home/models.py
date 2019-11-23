from django.db import models

class Pickup(models.Model):
    Driver = models.ForeignKey('app1.Driver')
    User= models.ForeignKey('app1.User')
    price= models.IntegerField(default=0)
    distanceTraveled=models.IntegerField(default=0)
    driverAccepted=models.BooleanField(default=0)
    #item=models.ForeignKey(Item)
    dropOff_lat=models.DecimalField(default=0.00, max_digits=10, decimal_places=7)
    dropOff_lng=models.DecimalField(default=0.00, max_digits=10, decimal_places=7)
    completed=models.BooleanField(default=0)
