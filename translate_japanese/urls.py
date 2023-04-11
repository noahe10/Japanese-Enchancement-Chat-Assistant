from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('enja', views.enja, name="enja"),
    path('jaen', views.jaen, name="jaen"),
    path('jaja', views.jaja, name="jaja"),
]