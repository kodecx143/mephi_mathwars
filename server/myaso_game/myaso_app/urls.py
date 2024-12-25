from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='home'),
    path('teams/', views.team_list, name='team_list'),
    path('users/', views.user_list, name='user_list'),
    path('coins/', views.coin_list, name='coin_list'),
    path('position_cost/<int:position>/', views.position_cost, name='position_cost'),
    path('coins_generation/<int:count>/', views.generate_coin, name='generate_coin'),
    path('destruct_coin/<int:position>/', views.destruct_coin, name='destruct_coin'),
    path('api/check-coin/<int:position>/', views.position_cost, name='position_cost'),
    path('api/generate-coin/<int:count>/', views.generate_coin, name='generate_coin'),
    path('api/delete-coin/<int:position>/', views.destruct_coin, name='destruct_coin'),
]