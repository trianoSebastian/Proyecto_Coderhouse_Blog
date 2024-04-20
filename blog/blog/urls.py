from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import (
    PostHomeView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostRegisterView,
    UploadAvatarView,
    login_view,
    like,
    logout_view,
    profile_view,
    update_profile)
    

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('accounts/', include('allauth.urls')),
    path('',PostHomeView.as_view(),name='home'),
    path('list/',PostListView.as_view(),name='list'),
    path('register/',PostRegisterView.as_view(),name='register'),
    path('login/',login_view,name='login'),
    path('profile/',profile_view,name='profile'),    
    path('update_profile/',update_profile,name='update_profile'),    
    path('create/',PostCreateView.as_view(),name='create'),
    path('<slug>/detail',PostDetailView.as_view(),name='detail'),
    path('<slug>/update/',PostUpdateView.as_view(),name='update'),
    path('<slug>/delete/',PostDeleteView.as_view(),name='delete'),
    path('like/<slug>/',like,name='like'),    
    path('logout_view/',logout_view,name='logout_view'),    
    path('upload_avatar/',UploadAvatarView.as_view(),name='upload_avatar')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)