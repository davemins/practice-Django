from django.urls import path

from .views import post_list_view, post_create_view, post_delete_view, post_detail_view, post_update_view

app_name = 'posts'

urlpatterns = [
    path('', post_list_view, name='post-list'), # 글 목록
    path('create/', post_create_view, name='post-create'), # 글 생성
    path('<int:id>/', post_detail_view), # 글 상세
    path('<int:id>/edit/', post_update_view), # 글 입력
    path('<int:id>/delete/', post_delete_view), # 글 삭제
]