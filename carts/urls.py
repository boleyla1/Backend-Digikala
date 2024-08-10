from django.urls import path
from . import views

urlpatterns = [
    path('',views.Cartsummary,name='Cartsummary'),
    path('add/',views.Cartadd,name='Cartadd'),
    path('delete/',views.Cartdelete,name='Cartdelete'),
    path('update/',views.Cartupdate,name='Cartupdate')
]