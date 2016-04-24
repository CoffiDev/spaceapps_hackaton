# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from space.companies import views as companies

urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url('^$', companies.list, name='list'),
    url('^(?P<company_id>\d+)', companies.detail, name='detail'),
    url('^data$', companies.get_data, name='get_data'),
    url(r'^media/(?P<path>.*)$',
                'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
)