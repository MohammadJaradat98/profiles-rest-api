from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):


    def get(self, requset, format=None):
        """returns a list of APIview features"""
        an_apiview = ['good']

        return Response({'message':'Hello!', 'an_apiview':an_apiview})