from django.contrib import admin
from .models import *

# Register your models here.


class UserDetailAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name', 'email', 'password', 'my_referral_code', 'referral_code']
admin.site.register(UserDetails , UserDetailAdmin)
