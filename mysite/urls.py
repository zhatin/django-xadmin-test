# -*- coding: utf-8 -*-
# from django.conf.urls import include, url
from django.urls import include, path

# Uncomment the next two lines to enable the admin:
import xadmin
xadmin.autodiscover()

# versionģ���Զ�ע����Ҫ�汾���Ƶ� Model
from xadmin.plugins import xversion
xversion.register_models()

from django.contrib import admin

urlpatterns = [
    path(r'', xadmin.site.urls)
]
