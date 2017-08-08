from django.conf.urls import url, include
from django.contrib import admin
from users.views import UserRegistrationAPIView
urlpatterns = [

    url(r'registration/',UserRegistrationAPIView.as_view())

]
