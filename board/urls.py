from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import post_view, reply_view, base_view

app_name = 'board'

urlpatterns = [
    # base_view
    path('', base_view.index),

    # post_view
    path('posts/', post_view.post_list),
    path('post/<int:id>/', post_view.post_detail),
    path('post/create/', post_view.post_create),

    # reply_view
    path('replys/', reply_view.reply_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)