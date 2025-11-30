#!/bin/sh

SRE_REPORTS_PATH=$PWD
PYTHON=$(which python)

$PYTHON $SRE_REPORTS_PATH/manage.py migrate

$PYTHON $SRE_REPORTS_PATH/manage.py createsuperuser --noinput > /dev/null 2>&1

/usr/local/bin/uwsgi uwsgi.ini

