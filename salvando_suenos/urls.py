from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^api/v1/', include('apps.user.urls', namespace="users")),
	url(r'^api/v1/', include('apps.device.urls', namespace="devices")),
  url(r'^api/v1/', include('apps.account.urls', namespace="accounts")),
	url(r'^api/v1/', include('apps.result.urls', namespace="results")),
]
