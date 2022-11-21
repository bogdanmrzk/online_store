from django.urls import path
from .views import *

urlpatterns = [
    path('items/', basic_view, name='homepage'),
    path('<str:category_v>', category_list, name='category_name'),
]


