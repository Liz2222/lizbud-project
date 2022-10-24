from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('room/<pk>', views.room , name='rooms'),
    path('create-room/', views.createRoom , name='create-room'),
    path('update-room/<str:pk>', views.updateRoom , name='update-room'),

]
