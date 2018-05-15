# tangiers URL Configuration
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	path('', include('accounts.urls')),
	path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

urlpatterns += [
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
