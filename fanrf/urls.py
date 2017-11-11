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
from django.conf.urls import url, include
from django.contrib import admin

from fan import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.FanList.as_view(), name='fan_list'),
    url(r'^(?P<pk>\d+)/', include([
        url(r'^$', views.FanUpdate.as_view(), name='fan_update'),
        url(r'^toggle/$', views.light_toggle, name='fan_toggle'),
    ])),
    url(r'^api/', include([
        url(r'^(?P<pk>\d+)/', include([
            url(r'^$', views.api_fanstatus, name='api_fanstatus'),
            url(r'^switch/$', views.api_switch, name='api_switch'),
            url(r'^light/(?P<brightness>\d+)/$', views.api_brightness, name='api_brightness'),
            url(r'^speed/(?P<speed>\w+)/$', views.api_fan_speed, name='api_speed'),
        ])),
    ])),

]
