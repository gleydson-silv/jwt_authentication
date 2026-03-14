from django.urls import path
from . import views
from . import frontend_views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.logout, name='logout'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='reset_password_confirm'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile/', views.profile, name='get_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('token/verify/', views.verify_token, name='token_verify'),
    path('account/delete/', views.delete_account, name='delete_account'),
    path('2fa/verify/', views.verify_2fa, name='verify_2fa'),
    path('2fa/enable/', views.enable_2fa, name='enable_2fa'),
    path('2fa/disable/', views.disable_2fa, name='disable_2fa'),
    path('app/', frontend_views.app_home, name='app_home'),
    path('app/register/', frontend_views.app_register, name='app_register'),
    path('app/login/', frontend_views.app_login, name='app_login'),
    path('app/logout/', frontend_views.app_logout, name='app_logout'),
    path('app/forgot-password/', frontend_views.app_forgot_password, name='app_forgot_password'),
    path('app/reset-password/', frontend_views.app_reset_password, name='app_reset_password'),
    path('app/reset-password/<uidb64>/<token>/', frontend_views.app_reset_password, name='app_reset_password_token'),
    path('app/change-password/', frontend_views.app_change_password, name='app_change_password'),
    path('app/profile/', frontend_views.app_profile, name='app_profile'),
    path('app/profile/update/', frontend_views.app_profile_update, name='app_profile_update'),
    path('app/token/verify/', frontend_views.app_token_verify, name='app_token_verify'),
    path('app/token/refresh/', frontend_views.app_token_refresh, name='app_token_refresh'),
    path('app/account/delete/', frontend_views.app_account_delete, name='app_account_delete'),
    path('app/2fa/verify/', frontend_views.app_2fa_verify, name='app_2fa_verify'),
    path('app/2fa/enable/', frontend_views.app_2fa_enable, name='app_2fa_enable'),
    path('app/2fa/disable/', frontend_views.app_2fa_disable, name='app_2fa_disable'),
    path('app/security/', frontend_views.app_security, name='app_security'),
    
]
