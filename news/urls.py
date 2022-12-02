from django.urls import path
from .views import *

urlpatterns = [
    path('', newsview, name='news'),    
]
