# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import posixpath

from fabric.api import *
from fabric.colors import *
from fabric.context_managers import contextmanager


@contextmanager
def environment():
    "Sets virtualenv and settings module"

    with prefix('. ../env/bin/activate'),\
        shell_env(DJANGO_SETTINGS_MODULE='%s.settings.%s' % (env.project, env.name)):
            yield


@contextmanager
def message(content):
    "Hides output from command and prints a message"

    print(cyan(content))

    with hide('commands'):
        yield


@task(default=True)
def full():
    "Deploys application code to the selected environment"

    update()
    provision()
    migrate()
    restart()

    print(green('Success!'))


@task
def update():
    "Pulls new code from the repo"

    require('name', provided_by=['production', 'staging'],
            used_for='setting the name of the branch to update from.')

    with message('Pulling code..'):
        run('git pull')


@task
def provision():
    "Installs python and frontend dependencies"

    require('name', provided_by=['production', 'staging'],
            used_for='installing python and frontend dependencies.')

    with message('Updating project dependencies..'):
        with environment():
            run('pip install -r requirements/%s.txt' % env.name)


@task
def migrate():
    "Executes database migrations"

    require('name', provided_by=['production', 'staging'],
            used_for='setting the django project  module.')

    with message('Running database migrations..'), environment():
        run('python2.7 manage.py migrate --noinput')


@task
def assets():
    "Collects static files"

    require('name', provided_by=['production', 'staging'],
            used_for='setting the django project module.')

    with message('Collecting static files..'), environment():
        run('python2.7 manage.py collectstatic --noinput')


@task
def restart():
    "Restart uwsgi server"

    require('name', provided_by=['production', 'staging'],
            used_for='set the path to the server.')

    with message('Restarting web server..'):
        run('touch ../reload')

