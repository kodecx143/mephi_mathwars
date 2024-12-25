from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='home'),
    path('teams/', views.team_list, name='team_list'),
    path('users/', views.user_list, name='user_list'),
    path('coins/', views.coin_list, name='coin_list'),
   # path('edit_team/<int:team_id>/', views.edit_team, name='edit_team'),
   # path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
   # path('edit_coin/<int:coin_id>/', views.edit_coin, name='edit_coin'),
]