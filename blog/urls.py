from django.urls import path, include
from . import views
from .views import AddPostView, EditPostView, DeletePostView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post/slug/', AddPostView.as_view(), name='add_post'),
    path('post/edit/<slug:slug>/', EditPostView.as_view(), name='edit_post'),
    path('post/<slug:slug>/remove', DeletePostView.as_view(),
         name='delete_post'),
    path('summernote/', include('django_summernote.urls')),
]
