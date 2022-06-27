from django.urls import path
from . import views
from knox import views as knox_view

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', knox_view.LogoutView.as_view()),
]