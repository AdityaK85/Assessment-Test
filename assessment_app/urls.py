from django.urls import path
from .views_api import *

urlpatterns = [
    path('user_registration/', user_registration) ,
    path('get_users_info/', get_users_info),
    path('get_referral_users_info/', get_referral_users_info)
]
