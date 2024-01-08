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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from app.views.system.auth_view import LoginView, RegisterUserView
from app.views.system.user_view import UserPagination, UserList, UserDetail,UserCreate, UserUpdate, UserEnabled, UserDisabled
from app.views.system.groups_view import GroupPagination, GroupList, GroupCreate, GroupDetail
from app.views.system.permissions_view import PermissionPagination, PermissionList, PermissionDetail

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/auth/login/', LoginView.as_view(), name='login_token'),
    path('api/v1/auth/refresh-token/', jwt_views.TokenRefreshView.as_view(), name='refresh_token'),
    path('api/v1/auth/register/', RegisterUserView.as_view(), name='register_user'),
    path('api/v1/auth/forgot-password/', RegisterUserView.as_view(), name='forgot_password'),
    path('api/v1/auth/reset-password/', RegisterUserView.as_view(), name='reset_password'),
    path('api/v1/auth/verify-email/', RegisterUserView.as_view(), name='verify_email'),

    path('api/v1/users/', UserList.as_view(), name='user-list'),
    path('api/v1/users/pagination/', UserPagination.as_view(), name='user-pagination'),
    path('api/v1/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('api/v1/users/create/', UserCreate.as_view(), name='user-create'),
    path('api/v1/users/<int:pk>/update/', UserPagination.as_view(), name='user-update'),
    path('api/v1/users/<int:pk>/enabled/', UserEnabled.as_view(), name='user-enabled'),
    path('api/v1/users/<int:pk>/disabled/', UserDisabled.as_view(), name='user-disabled'),

    path('api/v1/groups/pagination/', GroupPagination.as_view(), name='group-pagination'),
    path('api/v1/groups/', GroupList.as_view(), name='group-list'),
    path('api/v1/groups/<int:pk>/', GroupDetail.as_view(), name='group-detail'),
    path('api/v1/groups/create', GroupCreate.as_view(), name='group-create'),
    path('api/v1/groups/<int:pk>/update/', GroupDetail.as_view(), name='group-update'),
    path('api/v1/groups/<int:pk>/delete/', GroupDetail.as_view(), name='group-delete'),

    path('api/v1/permissions/', PermissionList.as_view(), name='group-list'),
    path('api/v1/permissions/pagination/', PermissionPagination.as_view(), name='group-pagination'),
    path('api/v1/permissions/<int:pk>/', PermissionDetail.as_view(), name='group-detail'),
]
