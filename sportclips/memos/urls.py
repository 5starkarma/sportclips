from django.urls import path

from . import views
from .views import (
    MemoListView,
    MemoDetailView,
    MemoCreateView,
    MemoUpdateView,
    MemoDeleteView,
    UserMemoListView
)

urlpatterns = [
    path('', MemoListView.as_view(template_name='memos/memos.html'),
         name='memos-memos'),
    path('<int:pk>', MemoDetailView.as_view(),
         name='memos-detail'),
    path('user/<str:username>', UserMemoListView.as_view(),
         name='user-memos'),
    path('create/', MemoCreateView.as_view(),
         name='memos-create'),
    path('<int:pk>/update/', MemoUpdateView.as_view(),
         name='memos-update'),
    path('<int:pk>/delete/', MemoDeleteView.as_view(),
         name='memos-delete'),
    path('<int:pk>/comment/', views.add_comment_to_memo,
         name='add-comment-to-memo'),
]
