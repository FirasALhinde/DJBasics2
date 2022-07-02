from django.urls import path
from .views import post_list,post_detail,new_post,edit_post,delete_post,PostList,PostDetail,PostDelete

app_name='blog'

urlpatterns = [
    path('',post_list,name='post_list'),
    path('<int:id>',post_detail,name='post_detail'),
    path('new',new_post,name="new_post"),
    path('<int:id>/edit',edit_post,name='edit_post'),
    path('<int:id>/delete',delete_post,name='delete_post'),
    path('cbv',PostList.as_view(),name='cbv_post_list'),
    path('cbv/<int:pk>',PostDetail.as_view(),name='cbv_post_detail'),
    path('cbv/<int:pk>/delete',PostDelete.as_view(),name='cbv_post_detete')

]