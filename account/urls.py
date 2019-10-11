from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'account'

urlpatterns = [
    #path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='account_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='account_logout'),
    path('', views.dashboard, name='account_dashboard'),
    #path('password_change/', auth_views.PasswordChangeView.as_view(), name='account_password_change'),
    #path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='account_password_change_done'),
]