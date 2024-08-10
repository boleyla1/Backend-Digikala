from django.urls import path
from . import views

urlpatterns = [
    path('', views.Shop, name='shop'),
    path('login/', views.UserLogin, name='login'),
    path('logout/', views.UserLogout, name='logout'),
    path('register/', views.Rigester, name='register'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:cat>', views.category, name='category'),
    path('category/', views.category_summary, name='category_summary'),
    path('updateuser/',views.updateuser,name='updateuser')

]
