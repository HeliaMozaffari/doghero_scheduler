from django.db import models

class owner(models.Model):
    owner_name = models.CharField(max_length=60, default="")
    owner_email = models.CharField(max_length=50, default="")
    owner_number = models.CharField(max_length=10, default="")
    owner_address = models.CharField(max_length=100, default="")
    owner_emergency_name = models.CharField(max_length=60, default="")
    owner_emergency_relation = models.CharField(max_length=30, default="")
    owner_emergency_number = models.CharField(max_length=10, default="")

class dog(models.Model):
    owner_number = models.CharField(max_length=10, default="")
    dog_name =models.CharField(max_length=30, default="")
    dog_age = models.CharField(max_length=2, default="")
    dog_breed = models.CharField(max_length=50, default="")
    dog_medical_notes = models.CharField(max_length=500, default="")
    dog_behavioral_notes = models.CharField(max_length=500, default="")





    
