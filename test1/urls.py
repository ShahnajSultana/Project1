from django.contrib import admin
from django.urls import path
from .views import home,contact,service,info

urlpatterns =[
    path('admin/',admin.site.urls),
    path('',home),
    path('contact',contact),
    
    path('service',service),
    path('info/<name>/<age>',info),


    ]
