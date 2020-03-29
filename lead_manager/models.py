from django.db import models

# Create your models here.
class Leads(models.Model):
    '''Store the information for potential leads'''

    first_name = models.CharField(null=True, max_length=255)
    last_name = models.CharField(null=True, max_length=255)
    email = models.EmailField(null=True, unique=True)
    contacted = models.TextField(null=True) # make this TextField instead of boolean to allow for details
    notes = models.TextField(null=True)
    created_At = models.DateTimeField(null=False, auto_now=True)
    updated_At = models.DateTimeField(null=False, auto_now=True)