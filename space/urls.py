# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url, include

from space.companies import views as companies

urlpatterns = (
    url('', companies.list, name='list'),
    url('/(?P<company_id>[-\w]{1,144})', companies.detail, name='detail')
)
