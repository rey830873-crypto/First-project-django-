from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_contacts, name='liste'),
    path('contact/<int:id>/', views.detail_contact, name='detail'),
]