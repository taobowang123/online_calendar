from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone

# Create your models here.
EVENT_TYPE = (('active','active'),('old','old'))

class Events(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateField(default = timezone.now)
    start_time= models.TimeField(default = timezone.now)
    end_time = models.TimeField(default = timezone.now)
    event = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100, choices=EVENT_TYPE,default='active')
    # def __str__(self):
    #     return self.description

# Create your models here.
