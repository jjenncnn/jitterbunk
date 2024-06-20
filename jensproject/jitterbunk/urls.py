from django.urls import path

from . import views

app_name = "jitterbunk"

urlpatterns = [
    # ex: /jitterbunk/
    path('', views.index, name='index'),
    # ex: /jitterbunk/users/
    path('users/', views.users, name='users'),
    # ex: /jitterbunk/users/5/
    path('users/<int:user_id>/', views.user, name='user'),
    # ex: /jitterbunk/bunks/
    path('bunks/', views.bunks, name='bunks'),
    # ex: /jitterbunk/bunkform/
    path('bunkform/', views.bunkform, name='bunkform'),

    path('bunk_form', views.bunk_form, name='bunk_form'),
]