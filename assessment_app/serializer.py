from django.conf import settings
from rest_framework import serializers
from .models import * 



class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'
