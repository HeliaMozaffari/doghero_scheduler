from django.db import models

class owner(models.Model):
    owner_name = models.CharField(max_length=60)
    owner_email = models.CharField(max_length=50)
    owner_number = models.CharField(max_length=10)
    owner_address = models.CharField(max_length=100)
    owner_emergency_name = models.CharField(max_length=60)
    owner_emergency_relation = models.CharField(max_length=30)
    owner_emergency_number = models.CharField(max_length=10)

class dog(models.Model):
    owner_number = models.CharField(max_length=10, default="")
    dog_name =models.CharField(max_length=30)
    dog_age = models.CharField(max_length=2)
    dog_breed = models.CharField(max_length=50)
    dog_medical_notes = models.CharField(max_length=500)
    dog_behavioral_notes = models.CharField(max_length=500)



    
