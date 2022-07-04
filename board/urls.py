from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import post_view, reply_view, base_view

app_name = 'board'

urlpatterns = [
    # base_view
    path('', base_view.IndexViewSet.as_view({'get': 'list'}), name='index'),

    # post_view
    path('posts/<str:category_name>/', post_view.PostListView.as_view({'get': 'list'}), name='postList'),
    path('post/<int:post_id>/', post_view.PostDetailView.as_view(), name='postDetail'),
    path('post/create/', post_view.postCreate, name='postCreate'),
    path('post/<int:pk>/like/', post_view.postLike, name='postLike'),

    # reply_view
    path('replys/', reply_view.ReplyListView.as_view({'get': 'list'}), name='replyList'),
    path('reply/<int:reply_id>/', reply_view.ReplyDetailView.as_view(), name='replyDetail'),
    path('<int:post_id>/reply/create/', reply_view.replyCreate, name='replyCreate'),
    path('reply/<int:pk>/like/', reply_view.replyLike, name='replyLike'),
]

urlpatterns = format_suffix_patterns(urlpatterns)