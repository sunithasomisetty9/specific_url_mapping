from django.urls import path
from csk.views import *

app_name='Dhoni'

urlpatterns=[
    path('msd/',msd,name='msd'),
    path('hi/',hi,name='hi'),

]
