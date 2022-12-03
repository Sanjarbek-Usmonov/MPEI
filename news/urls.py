from django.urls import path
from .views import *

urlpatterns = [
    path('', newsview, name='news'),    
    path('<int:pk>', news_detailview, name='news-detail'),    
]
