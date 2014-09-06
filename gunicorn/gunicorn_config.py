command = '/opt/venv/bin/gunicorn'
pythonpath = '/opt/venv/newtest'
#bind = '10.13.37.154:8001'
bind = '127.0.0.1:8001'
#workers = 4
user = 'nobody'
env = 'DJANGO_SETTINGS_MODULE=newtest.settings'

