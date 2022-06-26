from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('users/', views.userList),
    # path('signup/'),
    # path('login/'),
    # path('logout/'),
]