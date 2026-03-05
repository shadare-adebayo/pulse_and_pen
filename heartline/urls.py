from django.urls import path 
from .views import bp_list, bp_detail, bp_create, bp_update, bp_confirm_delete, registration, dashboard

urlpatterns= [
    path("", bp_list, name='bp_list' ),
    path('bp_detail/<int:pk>/', bp_detail, name= 'bp_detail'),
    path( "add/", bp_create, name='bp_create' ),
    path('<int:pk>/edit/', bp_update, name = 'bp_update'),
    path('<int:pk>/delete/', bp_confirm_delete, name= 'bp_confirm_delete'),
    path('register/', registration, name='registration'),
    path('dashboard/', dashboard, name = 'dashboard')
]