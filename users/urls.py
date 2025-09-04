from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', views.register),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # ✅ Login JWT
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # ✅ Refresh Token
    path('logout/', views.logout),
    path('forgot_password/', views.forgot_password),
    path('reset_password/', views.reset_password),
    path('reset_password/<uidb64>/<token>/', views.reset_password),
]
