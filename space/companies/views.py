# coding: utf-8

from __future__ import unicode_literals
import random

from django.shortcuts import render
from django.http import HttpResponse

from .models import Company, InformationRecovered


def get_sensor_extra_info():
    return {
        'precipitation_mm': random.random(),
        'monoxid': random.random(),
        'water_quality': random.random()
    }


def list(request):
    context = {
        'companies': Company.objects.all()
    }
    return render(request, 'companies/list.html', context)


def detail(request, company_id):
    return True


def get_data(request):

    company = Company.objects.order_by('?').first()

    data = get_sensor_extra_info()
    data.update({'company': company})
    data.update({
        key: field[0]
        for key, field in dict(request.GET).items()
    })

    company.informationrecovered_set.add(InformationRecovered.objects.create(**data))

    return HttpResponse('knowledge')
