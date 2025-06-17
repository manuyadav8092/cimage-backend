from django.db import models

class userdetails(models.Model):
    name= models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)
    mobile = models.IntegerField(unique=True)
    password= models.CharField(max_length=20)
    address =models.CharField(max_length=100)

memberShipName =(
        ("Silver","Silver"),
        ("Gold","Gold"),
        ("Platinum","Platinnum")

    )

class membershipdetails(models.Model):
    membershipCategory = models.CharField(max_length=20,choices=memberShipName)
    membershipID = models.AutoField(primary_key=True)
    email = models.ForeignKey(userdetails,on_delete=models.CASCADE)
    validity = models.DateField()
 
class eventDetails(models.Model):
    eventID = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=50,unique=True)
    eventDescription =models.CharField(max_length=100)
    eventDate = models.DateField()
    eventVenue =models.CharField(max_length=50)

class registrationDetails(models.Model):
    registrationDetails = models.AutoField(primary_key=True)
    eventID = models.ForeignKey(eventDetails,on_delete=models.CASCADE)
    email = models.ForeignKey(userdetails,on_delete=models.CASCADE)