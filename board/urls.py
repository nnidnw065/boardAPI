from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import post_view, reply_view, base_view

app_name = 'board'

urlpatterns = [
    # base_view
    path('', base_view.index),

    # post_view
    path('posts/', post_view.PostListView.as_view({'get': "list"})),
    path('post/<int:post_id>/', post_view.PostDetailView.as_view()),
    path('post/create/', post_view.postCreate),

    # reply_view
    path('replys/', reply_view.ReplyListView.as_view({'get': 'list'})),
    path('reply/<int:reply_id>/', reply_view.ReplyDetailView.as_view()),
    path('<int:post_id>/reply/create/', reply_view.replyCreate),
]

urlpatterns = format_suffix_patterns(urlpatterns)