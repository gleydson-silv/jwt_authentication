from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('logout/', views.logout,name='logout'),
    path('forgot_password/', views.forgot_password,name='forgot_password'),
    path('reset_password/<uidb64>/<token>/', views.reset_password,name='reset_password_confirm'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile/', views.profile, name='get_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('token/verify/', views.verify_token, name='token_verify'),
    path('account/delete/', views.delete_account, name='delete_account'),
]
