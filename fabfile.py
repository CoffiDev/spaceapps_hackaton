# -*- encoding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from fabric.api import env, task

import deploy


env.project = 'disbursements'
env.cwd = '/var/www/%s.mimoni.com/src' % env.project


@task
def production():
    "Sets variables for the production environment"

    env.user = 'production'
    env.hosts = ['54.208.104.101', '54.209.2.231']
    env.name = 'production'

@task
def staging():
    "Sets  variables for the staging environment"

    env.host_string = 'staging@korriban-services-staging.mimoni.com'
    env.name = 'staging'
