"""
WSGI config for examples project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import site
import sys

sys.path.append('/home/blck/Projects/djangozone/djangozone')
sys.path.append('/home/blck/Projects/djangozone')
site.addsitedir('/home/blck/.virtualenvs/djangozone/local/lib/python2.7/site-packages')
activate_env=os.path.expanduser('/home/blck/.virtualenvs/djangozone/bin/activate_this.py')
try:
    execfile(activate_env, dict(__file__=activate_env))
except:
    pass


import django.conf
django.conf.ENVIRONMENT_VARIABLE = "DJANGOZONE_SETTINGS_MODULE"
os.environ.setdefault("DJANGOZONE_SETTINGS_MODULE", "djangozone.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
