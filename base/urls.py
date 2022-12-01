from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('newsletter/email', newsletterformview, name='newsletterform'),
    path('message', receivedmessagesview, name='receivedmessages'),
]