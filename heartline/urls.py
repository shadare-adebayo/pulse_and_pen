from django.urls import path 
from .views import(
    bp_list, bp_detail, bp_create, 
    bp_update, bp_confirm_delete, 
    registration, dashboard, bp_journal_list,
    bp_journal_detail, bp_journal_create, bp_journal_delete,
    bp_journal_update,
)
urlpatterns= [
    path("", bp_list, name='bp_list' ),
    path('bp_detail/<int:pk>/', bp_detail, name= 'bp_detail'),
    path( "add/", bp_create, name='bp_create' ),
    path('<int:pk>/edit/', bp_update, name = 'bp_update'),
    path('<int:pk>/delete/', bp_confirm_delete, name= 'bp_confirm_delete'),
    path('register/', registration, name='register'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path('journal/', bp_journal_list, name='bp_journal_list'),
    path('journal/<int:pk>/detail/', bp_journal_detail, name='bp_journal_detail'),
    path("journal/add/", bp_journal_create, name='bp_journal_create'),
    path("journal/<int:pk>/edit/", bp_journal_update, name='bp_journal_update'),
    path('journal/<int:pk>/delete/', bp_journal_delete, name='bp_journal_delete'),
]