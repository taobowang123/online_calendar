from django.db import models
class Events(models.Model):
    # The name of table.
    email_address = models.EmailField()
    event = models.CharField(max_length=100)
    date = models.DateField()
    important_rank = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    note = models.CharField(max_length=100)

class User_info(models.Model):
    email_address=models.EmailField()
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

# Create your models here.
