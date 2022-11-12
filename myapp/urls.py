from django.urls import path
#My Code 
from myapp import views

urlpatterns = [
    path("",views.index,name='home'),
]