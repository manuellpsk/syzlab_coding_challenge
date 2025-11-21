from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profiles/', views.profiles, name='profiles'),
    path('drawing/create/<int:user_id>/', views.create_drawing, name='create_drawing'),
]
