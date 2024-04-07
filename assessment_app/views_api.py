from assessment_app.utility import *
from .models import *
from django.http import JsonResponse
import traceback
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import random
import datetime
from rest_framework.permissions import IsAuthenticated  
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.decorators import api_view , permission_classes, authentication_classes
from .serializer import *

@api_view(['post'])
@csrf_exempt
def user_registration(request):
    try:
        send_data = {'status':403 , 'response' : 'Something went wrong'}
        data = request.data
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        referral_code = data.get('referral_code')

        my_referral_code = f'ASSESSMENTPROJ{random.randint(1111, 9999)}' 
        obj = UserDetails.objects

        if not obj.filter(email = email).exists():
            if ( referral_code != "" and referral_code != None ) and (not obj.filter(my_referral_code = referral_code).exists()) :
                    return JsonResponse({'status':403 , 'response' : 'Invalid referral code' })

            user_obj = UserDetails.objects.create(name = name, email = email, password = password ,my_referral_code = my_referral_code, referral_code = referral_code , registeration_dt = datetime.datetime.today()  )
            api_token = MyTokenObtainPairSerializer().validate(user_obj)

            send_data = {'status':200 , 'user_id' : user_obj.id , 'api_token' : api_token,  'response' : 'Registered Successfully' }

        else:
            send_data = {'status':403 , 'response' : 'Email Already Exists' }

    except:
        traceback.print_exc
        send_data = {'status':403 , 'response' : 'Something went wrong'}
    return JsonResponse(send_data)



@permission_classes((IsAuthenticated,)) 
@authentication_classes((JWTAuthentication,))
@csrf_exempt
def get_users_info(request):
    try:
        user_details = UserDetails.objects.all().order_by('-id')
        payload = UserDetailsSerializer(user_details, many=True)
        serializer = payload.data
        for key in serializer:
            key.pop('password', None)
            key.pop('referral_code', None)
        send_data = {'status':200,'response' : 'Registered Users', 'payload':payload.data}
    except:
         traceback.print_exc
         send_data = {'status':403 , 'response' : 'Something went wrong'}
    return JsonResponse(send_data)


@permission_classes((IsAuthenticated,)) 
@authentication_classes((JWTAuthentication,))
@csrf_exempt
def get_referral_users_info(request):
    try:
        user_details = UserDetails.objects.all().exclude(referral_code = "").order_by('-id')

        serializer = UserDetailsSerializer(user_details, many=True)
        data = serializer.data

        for key in data:
            key.pop('my_referral_code', None)
        send_data = {'status':200,'response' : 'Referral Users', 'payload':data}
    except:
         traceback.print_exc()
         send_data = {'status':403 , 'response' : 'Something went wrong'}
    return JsonResponse(send_data)