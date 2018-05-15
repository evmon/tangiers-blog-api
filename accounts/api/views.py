from django.contrib.auth.models import Group

from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from blog.models import UserProfile, Post
from .serializers import ( UserProfileSerializer, GroupSerializer,
	PostSerializer, BasicPostSerializer, 
	)
from .permissions import IsAuthorOrReadOnly, IsUserOwnerOrReadOnly

@api_view(['GET'])
def api_root(request, format=None):
	"""
	The entry endpoint of our API.
	"""
	return Response({
		'users': reverse('userprofile-list', request=request),
		'groups': reverse('group-list', request=request),
		'posts': reverse('post-list', request=request),
	})

@permission_classes((IsUserOwnerOrReadOnly,))
class UserProfileListView(generics.ListCreateAPIView):
	"""
	API endpoint that represents a list of user profiles.
	"""
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer

@permission_classes((IsUserOwnerOrReadOnly,))
class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	API endpoint that represents a single user profile.
	"""
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer

@permission_classes((IsAdminUser,))
class GroupListView(generics.ListCreateAPIView):
	"""
	API endpoint that represents a list of groups.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

@permission_classes((IsAdminUser,))
class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	API endpoint that represents a single group.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

@permission_classes((IsAuthorOrReadOnly, ))
class PostListView(generics.ListCreateAPIView):
	"""
	API endpoint that represents a list of posts.
	"""
	queryset = Post.objects.all()

	def get_serializer_class(self):
		if self.request.user.is_authenticated:
			return PostSerializer
		return BasicPostSerializer

@permission_classes((IsAuthorOrReadOnly, ))
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	API endpoint that represents a single post.
	"""
	queryset = Post.objects.all()

	def get_serializer_class(self):
		if self.request.user.is_authenticated:
			return PostSerializer
		return BasicPostSerializer
