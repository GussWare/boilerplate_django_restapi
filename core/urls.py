"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from app.views.system.auth.login_view import LoginView
from app.views.system.auth.register_user_view import RegisterUserView
from app.views.system.users.user_view import UserPagination, UserList, UserDetail, UserEnabled, UserDisabled

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/auth/login/', LoginView.as_view(), name='login_token'),
    path('api/v1/auth/refresh-token/', jwt_views.TokenRefreshView.as_view(), name='refresh-token'),
    path('api/v1/auth/register/', RegisterUserView.as_view(), name='register_user'),

    path('api/v1/users/', UserList.as_view(), name='user-list'),
    path('api/v1/users/pagination/', UserPagination.as_view(), name='user-pagination'),
    path('api/v1/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('api/v1/users/<int:pk>/enabled/', UserEnabled.as_view(), name='user-enabled'),
    path('api/v1/users/<int:pk>/disabled/', UserDisabled.as_view(), name='user-disabled'),
]