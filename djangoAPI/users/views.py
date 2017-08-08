from django.shortcuts import render
from rest_framework.generics import CreateAPIView,GenericAPIView
from users.serializers import UserRegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status



class UserRegistrationAPIView(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            # password = serializer.data.password
            # print(password)
            self.perform_create(serializer)

            user = serializer.instance
            token, created = Token.objects.get_or_create(user=user)
            data = serializer.data
            data["token"] = token.key

            headers = self.get_success_headers(serializer.data)
            dic = {'data':data,'message':'请求成功','code':status.HTTP_201_CREATED}
            return Response(dic)
