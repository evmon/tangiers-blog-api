from django.contrib.auth.models import Group, Permission

from rest_framework import serializers

from blog.models import UserProfile, Post


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = UserProfile
		fields = ('url', 'first_name', 'last_name', 'email', 'is_staff', 
			'phone', 'site_url',
		)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	permissions = serializers.SlugRelatedField(
		slug_field='codename',
		queryset=Permission.objects.all(),
		many=True
	)

	class Meta:
		model = Group
		fields = ('url', 'name', 'permissions', )


class PostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'


class BasicPostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields = ('url', 'author', 'title', )
