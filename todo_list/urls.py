from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('cross_off/<list_id>',views.cross_off,name="cross_off"),    
    path('delete/<list_id>',views.delete,name="delete"),
    path('cross_on/<list_id>',views.cross_on,name="cross_on"),
    path('edit/<list_id>',views.edit,name="edit"),
]
