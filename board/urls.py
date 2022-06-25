from django.urls import path
from .views import post_view, reply_view, base_view

app_name = 'board'

urlpatterns = [
    path('', base_view.index),
    path('posts/', post_view.post_list),
    path('replys/', reply_view.reply_list),
]