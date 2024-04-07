from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from six import text_type
from rest_framework.pagination import PageNumberPagination

class MyTokenObtainPairSerializer(TokenObtainPairSerializer): 
    def validate(self, obj): 
        self.user = obj 
        refresh = self.get_token(self.user) 
        data = {}
        data['refresh'] = text_type(refresh)
        data['access'] = text_type(refresh.access_token) 
        return data
    


class CustomPagination(PageNumberPagination):
    page_size = 20  
    page_size_query_param = 'page_size'
    max_page_size = 1000  