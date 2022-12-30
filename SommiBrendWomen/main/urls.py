from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', views.basa),
    path('glavnoe', views.glavnoe),
    path('corzina', views.corzina),
    path('men', views.men),
    path('women', views.women),
    path('acsesuariwomen', views.acsesuariwomen),
    path('newwomen', views.newwomen),
    path('obuwwomen', views.obuwwomen),
    path('salewomen', views.salewomen),
    path('odezdawomen', views.odezdawomen),
    path('acsesuarimen', views.acsesuarimen),
    path('newmen', views.newmen),
    path('obuwmen', views.obuwmen),
    path('salemen', views.salemen),
    path('odezdamen', views.odezdamen),
]