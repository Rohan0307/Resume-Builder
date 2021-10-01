from django.contrib import admin
from django.urls import path
from resume.views import *

urlpatterns = [
    path('',home,name="home"),
    path('main',main,name='main'),
    path('tnc',tnc,name='tnc'),
    path('about',about,name='about'),
    path('policy', policy, name='policy'),
    path('carousal',generatecv,name='carousal'),
    path('format1',format1,name='format1'),
    path('format2',format2,name='format2'),
    path('format3',format3,name='format3'),
    path('format4',format4,name='format4')
]