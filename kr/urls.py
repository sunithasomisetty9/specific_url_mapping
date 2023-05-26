from django.urls import path
from kr.views import *

app_name='virat'

urlpatterns=[
    path('kolkatta/',kolkatta,name='kolkatta'),
    path('hello/',hello,name='hello'),
]