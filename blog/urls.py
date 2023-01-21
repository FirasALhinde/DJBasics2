from django.urls import path
from .import views

app_name = 'blog'
urlpatterns = [
    # path('',views.post_list,name='post_list'),
    # path('new',views.new_post,name='new_post'),
    # path('<int:id>',views.post_detail,name='post_detail'),
    # path('<int:id>/edit',views.edit_post,name='edit_post'),
    # path('<int:id>/delete',views.delete_post,name='delete_post'),


    # class based view
    path('cbv',views.PostList.as_view(),name='cbv_list'),
    path('cbv/new',views.PostNew.as_view(),name='cbv_new'),
    path('cbv/<int:pk>',views.PostDetail.as_view(),name='cbv_detail'),
    path('cbv/<int:pk>/delete',views.PostDelete.as_view(),name='cbv_deleta'),
    path('cbv/<int:pk>/edit',views.PostEdit.as_view(),name='cbv_edit'),

]
