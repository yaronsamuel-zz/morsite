#!/home/ordercak/djangoenv/bin/python2.6

# setup the virtualenv
import os, sys
os.environ.setdefault('PATH', '/bin:/usr/bin')
os.environ['PATH'] = '/home/ordercak/djangoenv/bin/python:' + os.environ['PATH']
os.environ['VIRTUAL_ENV'] = '/home/ordercak/djangoenv/bin'
os.environ['PYTHON_EGG_CACHE'] = '/home/ordercak/djangoenv/bin'
os.chdir('/home/ordercak/public_html/sweetsamuel.co.il')


# Add a custom Python path.
sys.path.insert(0, "/home/ordercak/public_html/sweetsamuel.co.il")


# Set the DJANGO_SETTINGS_MODULE environment variable to the file in my
# application directory with the db settings etc.
# (filename minus the extension ".py")
os.environ['DJANGO_SETTINGS_MODULE'] = "morsite.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")