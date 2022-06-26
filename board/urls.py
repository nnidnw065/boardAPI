from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import post_view, reply_view, base_view

app_name = 'board'

urlpatterns = [
    # base_view
    path('', base_view.index),

    # post_view
    path('posts/', post_view.PostListViewSet.as_view({'get': "list"})),
    path('post/<int:post_id>/', post_view.postDetail),
    path('post/create/', post_view.postCreate),

    # reply_view
    path('replys/', reply_view.ReplyListViewSet.as_view({'get': 'list'})),
    path('reply/<int:reply_id>/', reply_view.replyDetail),
    path('<int:post_id>/reply/create/', reply_view.replyCreate),
]

urlpatterns = format_suffix_patterns(urlpatterns)