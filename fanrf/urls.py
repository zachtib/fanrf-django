"""fanrf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from fan.views import FanList, FanUpdate, api_fan_speed, api_brightness

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', FanList.as_view(), name='fan_list'),
    url(r'^(?P<pk>\d+)/$', FanUpdate.as_view(), name='fan_update'),
    url(r'^api/(?P<pk>\d+)/light/(?P<brightness>\d+)/$', api_brightness, name='api_brightness'),
    url(r'^api/(?P<pk>\d+)/speed/(?P<speed>\w+)/$', api_fan_speed, name='api_speed'),
]
