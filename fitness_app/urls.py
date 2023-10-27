from django.urls import path
from . import views

urlpatterns = [
    # User Profile URLs
    path('userprofile/', views.userprofile_detail, name='userprofile_detail'),
    path('userprofile/new/', views.userprofile_create, name='userprofile_create'),
    path('userprofile/edit/<int:pk>/', views.userprofile_update, name='userprofile_update'),
    path('userprofile/delete/<int:pk>/', views.userprofile_delete, name='userprofile_delete'),

    # Fitness Tip URLs
    path('fitnesstips/', views.fitnesstip_list, name='fitnesstip_list'),
    path('fitnesstip/<int:pk>/', views.fitnesstip_detail, name='fitnesstip_detail'),
    path('fitnesstip/new/', views.fitnesstip_create, name='fitnesstip_create'),
    path('fitnesstip/edit/<int:pk>/', views.fitnesstip_update, name='fitnesstip_update'),
    path('fitnesstip/delete/<int:pk>/', views.fitnesstip_delete, name='fitnesstip_delete'),
]
