from django.db import models

# Create your models here.


class UserDetails(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
    password = models.CharField(max_length=300, blank=True, null=True)
    my_referral_code = models.CharField(max_length=300, blank=True, null=True)
    referral_code = models.CharField(max_length=300, blank=True, null=True)
    registeration_dt = models.DateTimeField(blank=True, null=True)

