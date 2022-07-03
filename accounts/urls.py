from django.urls import path
from . import views
from knox import views as knox_view

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', knox_view.LogoutView.as_view(), name='logout'),
    path('user_delete/<int:pk>/', views.UserDeleteAPI.as_view(), name='user_delete'),

    path('profile/create/', views.profile_create, name='profile_create'),
    path('profile/<int:user_id>/', views.profile_view, name='profile_view'),
    path('profile/update/<int:profile_id>/', views.profile_update, name='profile_update'),
]