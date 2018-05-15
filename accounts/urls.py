from django.urls import path
from .api.views import ( UserProfileListView, UserProfileDetailView,
	GroupListView, GroupDetailView, api_root, PostListView, PostDetailView,
	)

urlpatterns = [
	path('', api_root),
    path('profiles', UserProfileListView.as_view(), name='userprofile-list'),
    path('profile/<int:pk>', UserProfileDetailView.as_view(),
    	name='userprofile-detail'),
    path('groups', GroupListView.as_view(), name='group-list'),
    path('group/<int:pk>', GroupDetailView.as_view(), name='group-detail'),
    path('posts', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
]
