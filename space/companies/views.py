# coding: utf-8

from __future__ import  unicode_literals

from django.shortcuts import render

from .models import Company

def list(request):
    context = {
        'companies': Company.objects.all()
    }
    return render(request, 'companies/list.html', context)

def detail(request, company_id):
    return True