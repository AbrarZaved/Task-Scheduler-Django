from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login_page,name='login'),
    path('cross_off/<list_id>',views.cross_off,name="cross_off"),    
    path('delete/<list_id>',views.delete,name="delete"),
    path('cross_on/<list_id>',views.cross_on,name="cross_on"),
    path('edit/<list_id>',views.edit,name="edit"),
    path('',views.land,name='landing_page'),
    path('register/',views.register_page,name='register'),
    path('log_out/',views.log_out,name='logout'),
    path('home/',views.home,name='home'),
]
