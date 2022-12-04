from django.urls import path
from .views import *

urlpatterns = [
    path('conc/<str:slug>', scient_concil_view, name='scient-concil'),
]
